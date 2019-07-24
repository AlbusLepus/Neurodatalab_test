from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError

from testservice.models import Base
from testservice import config
from testservice.api.user import user_blueprint


def configure_app(app, config):
    app.config.from_object(config)


def create_app(config=config.Configuration):
    app = Flask(__name__)
    configure_app(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_DBNAME}:{config.POSTGRES_PORT}/{config.POSTGRES_DBNAME}'
    app.config['RABBITMQ_URI'] = f'amqp://{config.RABBITMQ_USER}:{config.RABBITMQ_PASSWORD}'
    app.app_context().push()
    app.db = SQLAlchemy(app, model_class=Base,
                        engine_options={"convert_unicode": True},
                        session_options={"autocommit": False, "autoflush": False})
    app.db.init_app(app)

    # app.url_map.strict_slashes = False

    @app.before_first_request
    def before_first_request():
        if app.config.get('DB_CREATE_TABLES', False):
            app.db.create_all()

    @app.after_request
    def session_commit(response):
        if response.status_code < 400:
            try:
                app.logger.info("Session commit")
                app.db.session.commit()
            except DatabaseError:
                app.logger.info("Session rollback")
                app.db.session.rollback()
                raise
        return response

    @app.errorhandler(HTTPException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    app.register_blueprint(user_blueprint)

    return app
