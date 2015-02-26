"""update User Model

Revision ID: 23d9f68ecd3
Revises: 4ad6e783ba8
Create Date: 2015-02-17 09:26:52.033484

"""

# revision identifiers, used by Alembic.
revision = '23d9f68ecd3'
down_revision = '4ad6e783ba8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    ### end Alembic commands ###