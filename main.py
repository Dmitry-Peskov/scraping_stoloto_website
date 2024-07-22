import asyncio
import aiohttp

import cnfg
from database.database import DataBase
from database.models import Sportlotto_7x49
from custom_type import LotteryNumber
from scrapper import TextConverter
from bs4 import BeautifulSoup


async def search_tickets(
        session: aiohttp.client.ClientSession,
        db: DataBase,
        num: LotteryNumber,
        url: str
):
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, "lxml")
            dt = TextConverter.extract_date_elements_from_text(num, soup)
            numbers = TextConverter.extract_numbers_from_text(soup)
            ticket = Sportlotto_7x49(
                lottery_number=num,
                event_time=dt.datetime,
                year=dt.year,
                month=dt.month,
                day=dt.day,
                hour=dt.hour,
                minute=dt.minute,
                num1=numbers.num1,
                num2=numbers.num2,
                num3=numbers.num3,
                num4=numbers.num4,
                num5=numbers.num5,
                num6=numbers.num6,
                num7=numbers.num7
            )
            await db.write_ticket(ticket)
            print("Записан тираж {0}".format(num))
        else:
            pass


async def main() -> None:
    db = DataBase()
    base_url = "https://www.stoloto.ru/7x49/archive/{0}"
    last_number_in_db = await db.get_number_latest_lottery()
    tasks = []
    async with aiohttp.ClientSession(headers=cnfg.HTTP_HEADERS) as client:
        for num in range(last_number_in_db + 1, last_number_in_db + 10_001):
            url = base_url.format(num)
            task = asyncio.create_task(
                search_tickets(
                    session=client,
                    db=db,
                    num=LotteryNumber(num),
                    url=url
                )
            )
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
