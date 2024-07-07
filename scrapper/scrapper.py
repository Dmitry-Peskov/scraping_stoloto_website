import datetime
from custom_type import LotteryNames, LotteryNumber, DateTimeElements


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
    __lottery_mask = {
        "Sportlotto_7x49": "Результаты тиража № {0} «Спортлото «7&nbsp;из&nbsp;49»,  ",
        "Sportlotto6x45": "Результаты тиража № {0} «Спортлото «6&nbsp;из&nbsp;45»,  ",
        "Sportlotto_5x36": "Результаты тиража № {0} «Спортлото «5&nbsp;из&nbsp;36»,  "
    }

    @classmethod
    def __get_num_month_by_title(cls, title: str) -> int:
        number = cls.__months.get(title)
        if number:
            return number
        raise ValueError("Не удалось получить номер месяца для {0}".format(title))

    @classmethod
    def __clear_datetime_string(cls, lottery: LotteryNames, number: LotteryNumber, text: str) -> str:
        mask = cls.__lottery_mask.get(lottery)
        if mask:
            deleted = mask.format(number)
            datetime_string = text.replace(deleted, "").replace(" в", "")
            return datetime_string
        raise ValueError("Для лоттереи {0} не реализована поддержка".format(lottery))

    @classmethod
    def extract_date_elements_from_text(cls, lottery: LotteryNames, number: LotteryNumber, text: str) -> DateTimeElements:
        date_element = cls.__clear_datetime_string(lottery, number, text).split()
        day = int(date_element[0])
        month = cls.__get_num_month_by_title(date_element[1])
        year = int(date_element[2])
        hour_minutes = date_element[3].split(":")
        hour, minute = int(hour_minutes[0]), int(hour_minutes[1])
        dt = datetime.datetime(year, month, day, hour, minute)
        return DateTimeElements(dt, year, month, day, hour, minute)
