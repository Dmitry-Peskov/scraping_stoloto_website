import os
from dataclasses import dataclass
import logging


@dataclass
class config:
    @dataclass
    class db:
        DSN: str = f"sqlite+aiosqlite:///{os.getcwd()}\\stoloto_database.sqlite3"
        ECHO: bool = True

    @dataclass
    class logging:
        FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"
        LEVEL: int = logging.INFO
