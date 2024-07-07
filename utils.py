from custom_type import LotteryNames


def get_base_url(lottery: LotteryNames) -> str:
    template = {
        "Sportlotto_7x49": "https://www.stoloto.ru/7x49/archive/{0}",
        "Sportlotto6x45": "https://www.stoloto.ru/6x45/archive/{0}",
        "Sportlotto_5x36": "https://www.stoloto.ru/5x36plus/archive/{0}"
    }
    return template.get(lottery)
