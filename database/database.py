from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from cnfg import cnfg
from custom_type import LotteryNumber
from .models import Sportlotto_7x49


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

    async def get_number_latest_lottery(self) -> LotteryNumber:
        """
        Получить номер последнего записанного в БД тиража для выбранной лотереи


        :return: номер последнего тиража в БД, если в базе нет ни одного тиража, будет возвращен 0
        """
        async with self.session() as session:
            query = select(Sportlotto_7x49).order_by(Sportlotto_7x49.lottery_number.desc()).limit(1)
            result = await session.execute(query)
            lottery = result.scalar()
            if lottery:
                return lottery.lottery_number
            return LotteryNumber(0)

    async def write_ticket(
            self,
            lottery_ticket: Sportlotto_7x49
    ):
        """
        Записать билет в БД

        :param lottery_ticket: экземпляр конкретного лотерейного билета
        :return:
        """
        async with self.session() as session:
            session.add(lottery_ticket)
            await session.commit()
