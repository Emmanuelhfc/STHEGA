"""upgrade

Revision ID: ba42a5372397
Revises: 7728836ef19c
Create Date: 2024-05-11 15:46:59.799124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba42a5372397'
down_revision: Union[str, None] = '7728836ef19c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('constants_for_ab', sa.Column('Re_max', sa.Float(), nullable=False))
    op.add_column('constants_for_ab', sa.Column('Re_min', sa.Float(), nullable=False))
    op.drop_column('constants_for_ab', 'Re')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('constants_for_ab', sa.Column('Re', sa.FLOAT(), nullable=False))
    op.drop_column('constants_for_ab', 'Re_min')
    op.drop_column('constants_for_ab', 'Re_max')
    # ### end Alembic commands ###
