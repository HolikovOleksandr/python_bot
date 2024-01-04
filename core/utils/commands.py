from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Start bot'),
        BotCommand(command='help', description='Bot functional hints'),
        BotCommand(command='cancel', description='Cancel'),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())