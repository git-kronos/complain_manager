"""empty message

Revision ID: d97ff5e68cb0
Revises: 
Create Date: 2022-06-05 00:20:20.041531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd97ff5e68cb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=13), nullable=True),
    sa.Column('role', sa.Enum('approver', 'complainer', 'admin', name='rolltype'), server_default='complainer', nullable=False),
    sa.Column('iban', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('complaints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('photo_url', sa.String(length=200), nullable=True),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('status', sa.Enum('pending', 'approved', 'rejected', name='state'), server_default='pending', nullable=False),
    sa.Column('complainer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['complainer_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('complaints')
    op.drop_table('users')
    # ### end Alembic commands ###