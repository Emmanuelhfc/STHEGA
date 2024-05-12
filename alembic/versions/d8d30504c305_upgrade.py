"""upgrade

Revision ID: d8d30504c305
Revises: ba42a5372397
Create Date: 2024-05-11 16:05:54.390338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8d30504c305'
down_revision: Union[str, None] = 'ba42a5372397'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delta_sb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Dn_max', sa.Float(), nullable=False),
    sa.Column('Dn_min', sa.Float(), nullable=False),
    sa.Column('Dn_max_inch', sa.Float(), nullable=False),
    sa.Column('Dn_min_inch', sa.Float(), nullable=False),
    sa.Column('Delta_sb', sa.Float(), nullable=False),
    sa.Column('Delta_sb_inch', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delta_sb')
    # ### end Alembic commands ###
