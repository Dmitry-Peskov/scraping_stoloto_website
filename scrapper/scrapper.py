import datetime
from custom_type import LotteryNames, LotteryNumber, DateTimeElements, Numbers7x49
from bs4 import BeautifulSoup


class TextConverter:
    __months = {
            "января": 1,
            "февраля": 2,
            "марта": 3,
            "апреля": 4,
            "мая": 5,
            "июня": 6,
            "июля": 7,
            "августа": 8,
            "сентября": 9,
            "октября": 10,
            "ноября": 11,
            "декабря": 12
        }

    @classmethod
    def __get_num_month_by_title(cls, title: str) -> int:
        number = cls.__months.get(title)
        if number:
            return number
        raise ValueError("Не удалось получить номер месяца для {0}".format(title))

    @classmethod
    def __clear_datetime_string(cls, number: LotteryNumber, text: str) -> str:
        """
        Строку вида "Результаты тиража № 114617 «Спортлото «5 из 36», 7 июля 2024 в 20:15" приводит к виду "7 июля 2024 20:15"
        """
        mask = "Результаты тиража № {0} «Спортлото «7 из 49»,  "
        deleted = mask.format(number)
        datetime_string = text.replace(deleted, "").replace(" в", "")
        return datetime_string

    @classmethod
    def extract_date_elements_from_text(cls, lottery: LotteryNames, number: LotteryNumber, html: BeautifulSoup) -> DateTimeElements:
        text = html.find("div", {"class": "cleared game_567 game_7x49"}).find("h1").text
        date_element = cls.__clear_datetime_string(number, text).split()
        day = int(date_element[0])
        month = cls.__get_num_month_by_title(date_element[1])
        year = int(date_element[2])
        hour_minutes = date_element[3].split(":")
        hour, minute = int(hour_minutes[0]), int(hour_minutes[1])
        dt = datetime.datetime(year, month, day, hour, minute)
        return DateTimeElements(dt, year, month, day, hour, minute)

    @classmethod
    def extract_numbers_from_text(cls, html: BeautifulSoup) -> Numbers7x49:
        numbers_rows = html.find_all("p", {"class": "number"})
        numbers = [int(row.text) for row in numbers_rows]
        numbers.sort()
        return Numbers7x49(*numbers)
