import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.types import DateTime, Integer, SmallInteger
from sqlalchemy import UniqueConstraint


class BaseTicketModel(AsyncAttrs, DeclarativeBase):
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


class Sportlotto7x49(BaseTicketModel):

    n1: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n2: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n3: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n4: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n5: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n6: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    n7: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
