from __future__ import with_statement
from alembic import context
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from logging.config import fileConfig
from testservice.config import Configuration
from testservice.models import Base
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    url = f'postgresql+psycopg2://{Configuration.POSTGRES_USER}:{Configuration.POSTGRES_PASSWORD}@' \
        f'{Configuration.POSTGRES_DBNAME}:{Configuration.POSTGRES_PORT}/{Configuration.POSTGRES_DBNAME}'
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    url = f'postgresql+psycopg2://{Configuration.POSTGRES_USER}:{Configuration.POSTGRES_PASSWORD}@' \
        f'{Configuration.POSTGRES_DBNAME}:{Configuration.POSTGRES_PORT}/{Configuration.POSTGRES_DBNAME}'
    connectable = create_engine(url)
    if not database_exists(connectable.url):
        create_database(connectable.url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
