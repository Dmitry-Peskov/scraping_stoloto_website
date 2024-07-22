import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.types import DateTime, Integer, SmallInteger
from sqlalchemy import UniqueConstraint


class BaseTicketModel(AsyncAttrs, DeclarativeBase):
    """
    Базовая модель для любого лоттерейного билета.
    Содержит в себе свойства ряд свойств, которые свойственны любому билету.
    Основным из которых является:

    ``lottery_number`` - номер тиража (первичный ключ с ограничением уникальности)

    """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    @declared_attr
    def __table_args__(cls):
        return (UniqueConstraint('lottery_number', name=f'_{cls.__name__}_lottery_number'),)

    lottery_number: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=False
    )
    event_time: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    year: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    month: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    day: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    hour: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    minute: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    def __str__(self) -> str:
        return f"""Билет "{self.__class__.__name__}" тиража №{self.lottery_number}"""


class Sportlotto_7x49(BaseTicketModel):

    num1: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num2: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num3: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num4: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num5: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num6: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    num7: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
