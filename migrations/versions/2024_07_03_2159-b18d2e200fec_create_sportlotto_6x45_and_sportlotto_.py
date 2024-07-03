"""create Sportlotto_6x45 and Sportlotto_5x36 models, edit Sportlotto_7x49

Revision ID: b18d2e200fec
Revises: 9b51dd2546ff
Create Date: 2024-07-03 21:59:21.312153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'b18d2e200fec'
down_revision: Union[str, None] = '9b51dd2546ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Sportlotto_5x36',
    sa.Column('lottery_number', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('event_time', sa.DateTime(), nullable=False),
    sa.Column('year', sa.SmallInteger(), nullable=False),
    sa.Column('month', sa.SmallInteger(), nullable=False),
    sa.Column('day', sa.SmallInteger(), nullable=False),
    sa.Column('hour', sa.SmallInteger(), nullable=False),
    sa.Column('minute', sa.SmallInteger(), nullable=False),
    sa.Column('num1', sa.SmallInteger(), nullable=False),
    sa.Column('num2', sa.SmallInteger(), nullable=False),
    sa.Column('num3', sa.SmallInteger(), nullable=False),
    sa.Column('num4', sa.SmallInteger(), nullable=False),
    sa.Column('num5', sa.SmallInteger(), nullable=False),
    sa.Column('extend_num', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto_5x36_lottery_number')
    )
    op.create_index(op.f('ix_Sportlotto_5x36_lottery_number'), 'Sportlotto_5x36', ['lottery_number'], unique=True)
    op.create_table('Sportlotto_6x45',
    sa.Column('lottery_number', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('event_time', sa.DateTime(), nullable=False),
    sa.Column('year', sa.SmallInteger(), nullable=False),
    sa.Column('month', sa.SmallInteger(), nullable=False),
    sa.Column('day', sa.SmallInteger(), nullable=False),
    sa.Column('hour', sa.SmallInteger(), nullable=False),
    sa.Column('minute', sa.SmallInteger(), nullable=False),
    sa.Column('num1', sa.SmallInteger(), nullable=False),
    sa.Column('num2', sa.SmallInteger(), nullable=False),
    sa.Column('num3', sa.SmallInteger(), nullable=False),
    sa.Column('num4', sa.SmallInteger(), nullable=False),
    sa.Column('num5', sa.SmallInteger(), nullable=False),
    sa.Column('num6', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto_6x45_lottery_number')
    )
    op.create_index(op.f('ix_Sportlotto_6x45_lottery_number'), 'Sportlotto_6x45', ['lottery_number'], unique=True)
    op.create_table('Sportlotto_7x49',
    sa.Column('lottery_number', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('event_time', sa.DateTime(), nullable=False),
    sa.Column('year', sa.SmallInteger(), nullable=False),
    sa.Column('month', sa.SmallInteger(), nullable=False),
    sa.Column('day', sa.SmallInteger(), nullable=False),
    sa.Column('hour', sa.SmallInteger(), nullable=False),
    sa.Column('minute', sa.SmallInteger(), nullable=False),
    sa.Column('num1', sa.SmallInteger(), nullable=False),
    sa.Column('num2', sa.SmallInteger(), nullable=False),
    sa.Column('num3', sa.SmallInteger(), nullable=False),
    sa.Column('num4', sa.SmallInteger(), nullable=False),
    sa.Column('num5', sa.SmallInteger(), nullable=False),
    sa.Column('num6', sa.SmallInteger(), nullable=False),
    sa.Column('num7', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto_7x49_lottery_number')
    )
    op.create_index(op.f('ix_Sportlotto_7x49_lottery_number'), 'Sportlotto_7x49', ['lottery_number'], unique=True)
    op.drop_index('ix_Sportlotto7x49_lottery_number', table_name='Sportlotto7x49')
    op.drop_table('Sportlotto7x49')


def downgrade() -> None:
    op.create_table('Sportlotto7x49',
    sa.Column('lottery_number', sa.INTEGER(), nullable=False),
    sa.Column('event_time', sa.DATETIME(), nullable=False),
    sa.Column('year', sa.SMALLINT(), nullable=False),
    sa.Column('month', sa.SMALLINT(), nullable=False),
    sa.Column('day', sa.SMALLINT(), nullable=False),
    sa.Column('hour', sa.SMALLINT(), nullable=False),
    sa.Column('minute', sa.SMALLINT(), nullable=False),
    sa.Column('n1', sa.SMALLINT(), nullable=False),
    sa.Column('n2', sa.SMALLINT(), nullable=False),
    sa.Column('n3', sa.SMALLINT(), nullable=False),
    sa.Column('n4', sa.SMALLINT(), nullable=False),
    sa.Column('n5', sa.SMALLINT(), nullable=False),
    sa.Column('n6', sa.SMALLINT(), nullable=False),
    sa.Column('n7', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto7x49_lottery_number')
    )
    op.create_index('ix_Sportlotto7x49_lottery_number', 'Sportlotto7x49', ['lottery_number'], unique=1)
    op.drop_index(op.f('ix_Sportlotto_7x49_lottery_number'), table_name='Sportlotto_7x49')
    op.drop_table('Sportlotto_7x49')
    op.drop_index(op.f('ix_Sportlotto_6x45_lottery_number'), table_name='Sportlotto_6x45')
    op.drop_table('Sportlotto_6x45')
    op.drop_index(op.f('ix_Sportlotto_5x36_lottery_number'), table_name='Sportlotto_5x36')
    op.drop_table('Sportlotto_5x36')
