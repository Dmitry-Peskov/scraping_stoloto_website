from typing import Type

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from cnfg import cnfg
from custom_type import LotteryNames, LotteryNumber, DateTimeElements, Numbers6x45, Numbers5x36, Numbers7x49
from .models import *


class ModelsLib:
    """
    Библиотека моделей лотерейных билетов.

    Предоставляет интерфейс ``get_model(name: LotteryNames)``
    позволяющий получить по литералу конкретную модель.
    """
    __lib: dict[LotteryNames, Type[BaseTicketModel]] = {
        "Sportlotto_7x49": Sportlotto_7x49,
        "Sportlotto_6x45": Sportlotto_6x45,
        "Sportlotto_5x36": Sportlotto_5x36
    }

    @classmethod
    def get_model(cls, name: LotteryNames) -> Type[BaseTicketModel]:
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

    async def get_number_latest_lottery(
            self,
            name: LotteryNames
    ) -> LotteryNumber:
        """
        Получить номер последнего записанного в БД тиража для выбранной лотереи

        :param name: название лотереи
        :return: номер последнего тиража в БД, если в базе нет ни одного тиража, будет возвращен 0
        """
        lottery = ModelsLib.get_model(name)
        async with self.session() as session:
            query = select(lottery).order_by(lottery.lottery_number.desc()).limit(1)
            result = await session.execute(query)
            lottery = result.scalar()
            if lottery:
                return lottery.lottery_number
            return LotteryNumber(0)

    async def write_ticket(
            self,
            lottery: LotteryNames,
            num: LotteryNumber,
            dt: DateTimeElements,
            numbers: Numbers7x49 | Numbers5x36 | Numbers6x45
    ):
        model = ModelsLib.get_model(lottery)
        ticket = model(num, *dt, *numbers)
        async with self.session() as session:
            session.add(ticket)
            await session.commit()


        
