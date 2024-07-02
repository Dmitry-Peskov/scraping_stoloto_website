import os
from dataclasses import dataclass
import logging


@dataclass
class cnfg:
    @dataclass
    class db:
        DSN: str = f"sqlite+aiosqlite:///{os.getcwd()}\\database\\stoloto_database.sqlite3"
        ECHO: bool = True
        AUTOFLUSH: bool = True
        EXPIRE_ON_COMMIT: bool = True

    @dataclass
    class logging:
        FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"
        LEVEL: int = logging.INFO
