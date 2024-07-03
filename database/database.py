from typing import Type

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from cnfg import cnfg
from custom_type import LotteryName
from .models import *


class ModelsLib:
    """
    Библиотека моделей лотерейных билетов.

    Предоставляет интерфейс ``get_model(name: LotteryName)``
    позволяющий получить по литералу конкретную модель.
    """
    __lib: dict[LotteryName, Type[BaseTicketModel]] = {
        "Sportlotto_7x49": Sportlotto_7x49,
        "Sportlotto_6x45": Sportlotto_6x45,
        "Sportlotto_5x36": Sportlotto_5x36
    }

    @classmethod
    def get_model(cls, name: LotteryName) -> Type[BaseTicketModel]:
        model = cls.__lib.get(name)
        if model:
            return model
        raise ModuleNotFoundError("Модель с именем {0} не существует".format(name))


class DataBase:
    def __init__(self):
        self.engine = create_async_engine(
            url=cnfg.db.DSN,
            echo=cnfg.db.ECHO,
        )
        self.session = async_sessionmaker(
            self.engine,
            expire_on_commit=cnfg.db.EXPIRE_ON_COMMIT,
            autoflush=cnfg.db.AUTOFLUSH
        )
