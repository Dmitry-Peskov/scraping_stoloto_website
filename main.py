import asyncio
import aiohttp

import cnfg
from database.database import DataBase
from custom_type import LotteryNames, LotteryNumber
from scrapper import TextConverter
from bs4 import BeautifulSoup

from utils import get_base_url


async def search_tickets(
        session: aiohttp.client.ClientSession,
        db: DataBase,
        lottery: LotteryNames,
        num: LotteryNumber,
        url: str
):
    async with session.get(url) as response:
        html = await response.text()
        if html:
            soup = BeautifulSoup(html, "lxml")
            dt = TextConverter.extract_date_elements_from_text(lottery, num, soup)
            numbers = TextConverter.extract_numbers_from_text(lottery, soup)
            await db.write_ticket(lottery, num, dt, numbers)


async def main(lottery: LotteryNames) -> None:
    db = DataBase()
    last_number_in_db = await db.get_number_latest_lottery(lottery)
    base_url = get_base_url(lottery)
    tasks = []
    async with aiohttp.ClientSession(headers=cnfg.HTTP_HEADERS) as client:
        for num in range(last_number_in_db+2, last_number_in_db+100):
            url = base_url.format(num)
            task = asyncio.create_task(search_tickets(client, db, lottery, LotteryNumber(num), url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main("Sportlotto_7x49"))
