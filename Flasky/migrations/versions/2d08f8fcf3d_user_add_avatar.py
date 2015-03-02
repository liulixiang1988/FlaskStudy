"""user add avatar

Revision ID: 2d08f8fcf3d
Revises: f8f45ae3a9
Create Date: 2015-02-28 15:22:05.741964

"""

# revision identifiers, used by Alembic.
revision = '2d08f8fcf3d'
down_revision = 'f8f45ae3a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###