"""Отказался от моделей для 5х36 и 6х45

Revision ID: 75139ad255f0
Revises: b18d2e200fec
Create Date: 2024-07-22 21:16:48.143126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75139ad255f0'
down_revision: Union[str, None] = 'b18d2e200fec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index('ix_Sportlotto_6x45_lottery_number', table_name='Sportlotto_6x45')
    op.drop_table('Sportlotto_6x45')
    op.drop_index('ix_Sportlotto_5x36_lottery_number', table_name='Sportlotto_5x36')
    op.drop_table('Sportlotto_5x36')


def downgrade() -> None:
    op.create_table('Sportlotto_5x36',
    sa.Column('lottery_number', sa.INTEGER(), nullable=False),
    sa.Column('event_time', sa.DATETIME(), nullable=False),
    sa.Column('year', sa.SMALLINT(), nullable=False),
    sa.Column('month', sa.SMALLINT(), nullable=False),
    sa.Column('day', sa.SMALLINT(), nullable=False),
    sa.Column('hour', sa.SMALLINT(), nullable=False),
    sa.Column('minute', sa.SMALLINT(), nullable=False),
    sa.Column('num1', sa.SMALLINT(), nullable=False),
    sa.Column('num2', sa.SMALLINT(), nullable=False),
    sa.Column('num3', sa.SMALLINT(), nullable=False),
    sa.Column('num4', sa.SMALLINT(), nullable=False),
    sa.Column('num5', sa.SMALLINT(), nullable=False),
    sa.Column('extend_num', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto_5x36_lottery_number')
    )
    op.create_index('ix_Sportlotto_5x36_lottery_number', 'Sportlotto_5x36', ['lottery_number'], unique=1)
    op.create_table('Sportlotto_6x45',
    sa.Column('lottery_number', sa.INTEGER(), nullable=False),
    sa.Column('event_time', sa.DATETIME(), nullable=False),
    sa.Column('year', sa.SMALLINT(), nullable=False),
    sa.Column('month', sa.SMALLINT(), nullable=False),
    sa.Column('day', sa.SMALLINT(), nullable=False),
    sa.Column('hour', sa.SMALLINT(), nullable=False),
    sa.Column('minute', sa.SMALLINT(), nullable=False),
    sa.Column('num1', sa.SMALLINT(), nullable=False),
    sa.Column('num2', sa.SMALLINT(), nullable=False),
    sa.Column('num3', sa.SMALLINT(), nullable=False),
    sa.Column('num4', sa.SMALLINT(), nullable=False),
    sa.Column('num5', sa.SMALLINT(), nullable=False),
    sa.Column('num6', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('lottery_number'),
    sa.UniqueConstraint('lottery_number', name='_Sportlotto_6x45_lottery_number')
    )
    op.create_index('ix_Sportlotto_6x45_lottery_number', 'Sportlotto_6x45', ['lottery_number'], unique=1)
