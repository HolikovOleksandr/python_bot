from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f'<b>Hello {message.from_user.first_name}</b>')
  await message.answer(f'<s>Hello {message.from_user.first_name}</s>')
  await message.reply(f'<tg-spoiler>Hello {message.from_user.first_name}</tg-spoiler>')
