from alembic import op
import sqlalchemy as sa

revision = 'init_quote'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'quote',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_number', sa.String(length=50), nullable=True),
        sa.Column('price', sa.Numeric(10, 2), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('quote')
