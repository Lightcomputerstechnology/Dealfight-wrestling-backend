import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Add the app folder to import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import models and Base
from app.core.database import Base
from app import models

# Alembic Config
config = context.config
fileConfig(config.config_file_name)

# Metadata from your Base model
target_metadata = Base.metadata

# Read URL from environment or fallback to config file
from dotenv import load_dotenv
load_dotenv()
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL', 'sqlite:///./app.db'))

def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
