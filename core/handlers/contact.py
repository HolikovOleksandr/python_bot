
from aiogram import Bot
from aiogram.types import Message



async def get_true_contact(message: Message, bot: Bot):
    await message.answer('That is <b>your</b> contact!')


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer('That is <b>not your</b> contact!')