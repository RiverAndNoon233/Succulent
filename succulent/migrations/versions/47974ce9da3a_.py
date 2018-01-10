"""empty message

Revision ID: 47974ce9da3a
Revises: 86c0cca85f59
Create Date: 2018-01-10 18:41:11.236277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47974ce9da3a'
down_revision = '86c0cca85f59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=True),
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###
