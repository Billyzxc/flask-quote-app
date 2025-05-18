from __future__ import with_statement
from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, pool
from alembic import context

from app import create_app, db
from app.models import quote  # ← 加入你的模型這行

# Alembic Config 物件
config = context.config
fileConfig(config.config_file_name)

# 取得 SQLAlchemy metadata
app = create_app()
with app.app_context():
    target_metadata = db.metadata

def run_migrations_offline():
    context.configure(
        url=os.getenv("DATABASE_URL"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
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
