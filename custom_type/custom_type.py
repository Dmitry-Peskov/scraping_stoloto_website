from collections import namedtuple
from typing import NewType


LotteryNumber = NewType("LotteryNumber", int)
DateTimeElements = namedtuple("DateTimeElements", "datetime year month day hour minute")