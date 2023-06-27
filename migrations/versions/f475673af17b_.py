"""empty message

Revision ID: f475673af17b
Revises: dd109aa18270
Create Date: 2021-10-08 09:21:13.394761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f475673af17b'
down_revision = 'dd109aa18270'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute("UPDATE todolists SET completed = False WHERE completed IS NULL")

    op.alter_column('todolists', 'completed', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###