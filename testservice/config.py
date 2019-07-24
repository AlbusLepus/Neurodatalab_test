from confi import BaseEnvironConfig, ConfigField, BooleanConfig, IntConfig


class Configuration(BaseEnvironConfig):
    # Flask configs
    DEBUG = BooleanConfig(default=True)
    SECRET_KEY = ConfigField(default=__name__)

    # DB configs
    POSTGRES_HOST = ConfigField(default='db')
    POSTGRES_PORT = IntConfig(default=5432)
    POSTGRES_DBNAME = ConfigField(default='db')
    POSTGRES_USER = ConfigField(default='user')
    POSTGRES_PASSWORD = ConfigField(default='pwd')
    DB_CREATE_TABLES = BooleanConfig(default=False)

    # SQLALCHEMY_DATABASE_URI = ConfigField(default='postgresql+psycopg2://user:pwd@db:5432/db')
    # SQLALCHEMY_DATABASE_URI.load(f'{POSTGRES_HOST}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DBNAME}:{POSTGRES_PORT}/{POSTGRES_DBNAME}')

    # Broker configs
    RABBITMQ_HOST = ConfigField()
    RABBITMQ_USER = ConfigField(default='rabbitmq')
    RABBITMQ_PASSWORD = ConfigField(default='pwd')
    RABBITMQ_VHOST = ConfigField(default='/')
    RABBITMQ_PORT = IntConfig(default=5672)
    RABBITMQ_CP_PORT = IntConfig(default=15672)
    RABBITMQ_EXCHANGE = ConfigField(default='')
    RABBITMQ_QUEUE = ConfigField(default='')

    # RABBITMQ_URI = ConfigField()
    # RABBITMQ_URI.load(f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}')

    # Custom configs
    LOG_LEVEL = IntConfig(default=30)
