"""init quote

Revision ID: 20250518_170156
Revises: 
Create Date: 2025-05-18T17:01:56.672450

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20250518_170156'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('quote',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_number', sa.String(length=50), nullable=True),
        sa.Column('product_desc', sa.Text(), nullable=True),
        sa.Column('overall_dim', sa.String(length=50), nullable=True),
        sa.Column('material', sa.String(length=120), nullable=True),
        sa.Column('finish', sa.String(length=120), nullable=True),
        sa.Column('loading', sa.Float(), nullable=True),
        sa.Column('price', sa.Numeric(10, 2), nullable=True),
        sa.Column('color', sa.String(length=50), nullable=True),
        sa.Column('fob_location', sa.String(length=60), nullable=True),
        sa.Column('package_type', sa.String(length=60), nullable=True),
        sa.Column('set_per_carton', sa.Integer(), nullable=True),
        sa.Column('carton_size', sa.String(length=50), nullable=True),
        sa.Column('cuft', sa.Float(), nullable=True),
        sa.Column('net_weight', sa.Float(), nullable=True),
        sa.Column('gross_weight', sa.Float(), nullable=True),
        sa.Column('max_load_40gp', sa.Integer(), nullable=True),
        sa.Column('moq', sa.Integer(), nullable=True),
        sa.Column('feature_1', sa.String(length=200), nullable=True),
        sa.Column('feature_2', sa.String(length=200), nullable=True),
        sa.Column('feature_3', sa.String(length=200), nullable=True),
        sa.Column('img_url', sa.String(length=500), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('quote')
