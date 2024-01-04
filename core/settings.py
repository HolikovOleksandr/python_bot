from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot: str
    admin: int


@dataclass
class Settings:
    bots: Bots


def get_setting(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot=env.str('BOT'),
            admin=env.int('ADMIN')
        )
    )

settings = get_setting('input')