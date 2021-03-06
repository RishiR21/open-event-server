"""empty message

Revision ID: 1959f5049425
Revises: 5d4c7b24818d
Create Date: 2018-07-16 16:28:18.094078

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1959f5049425'
down_revision = '5d4c7b24818d'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social_links', sa.Column('identifier', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('social_links', 'identifier')
    # ### end Alembic commands ###
