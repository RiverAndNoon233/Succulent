"""empty message

Revision ID: d76c59d3d199
Revises: 8516e093e009
Create Date: 2018-01-17 21:45:17.528991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd76c59d3d199'
down_revision = '8516e093e009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('beauti_essay', sa.Column('time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('beauti_essay', 'time')
    # ### end Alembic commands ###