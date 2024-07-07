from collections import namedtuple
from typing import NewType


LotteryNumber = NewType("LotteryNumber", int)
DateTimeElements = namedtuple("DateTimeElements", "datetime year month day hour minute")
Numbers7x49 = namedtuple("Numbers7x49", "num1 num2 num3 num4 num5 num6 num7")
Numbers6x45 = namedtuple("Numbers6x45", "num1 num2 num3 num4 num5 num6")
Numbers5x36 = namedtuple("Numbers5x36", "num1 num2 num3 num4 num5 extend_num")
