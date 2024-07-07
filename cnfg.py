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


HTTP_HEADERS: dict[str, str] = {
    "Accept": "application / json, text / plain, * / *",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}