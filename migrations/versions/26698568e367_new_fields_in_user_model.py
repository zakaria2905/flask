"""new fields in user model

Revision ID: 26698568e367
Revises: 74bc9bdbe96a
Create Date: 2023-06-03 18:50:20.998371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26698568e367'
down_revision = '74bc9bdbe96a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
