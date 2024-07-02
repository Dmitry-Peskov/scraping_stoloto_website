"""create table Sportlotto7x49

Revision ID: 9b51dd2546ff
Revises: 
Create Date: 2024-07-02 22:36:15.008020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9b51dd2546ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Sportlotto7x49',
    sa.Column('lottery_number', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('event_time', sa.DateTime(), nullable=False),
    sa.Column('year', sa.SmallInteger(), nullable=False),
    sa.Column('month', sa.SmallInteger(), nullable=False),
    sa.Column('day', sa.SmallInteger(), nullable=False),
    sa.Column('hour', sa.SmallInteger(), nullable=False),
    sa.Column('minute', sa.SmallInteger(), nullable=False),
    sa.Column('n1', sa.SmallInteger(), nullable=False),
    sa.Column('n2', sa.SmallInteger(), nullable=False),
    sa.Column('n3', sa.SmallInteger(), nullable=False),
    sa.Column('n4', sa.SmallInteger(), nullable=False),
    sa.Column('n5', sa.SmallInteger(), nullable=False),
    sa.Column('n6', sa.SmallInteger(), nullable=False),
    sa.Column('n7', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto7x49_lottery_number')
    )
    op.create_index(op.f('ix_Sportlotto7x49_lottery_number'), 'Sportlotto7x49', ['lottery_number'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_Sportlotto7x49_lottery_number'), table_name='Sportlotto7x49')
    op.drop_table('Sportlotto7x49')
