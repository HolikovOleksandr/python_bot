import json
from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f'<b>Hello {message.from_user.first_name}</b>')
  await message.answer(f'<s>Hello {message.from_user.first_name}</s>')
  await message.reply(f'<tg-spoiler>Hello {message.from_user.first_name}</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
  await message.answer('Ooo image?? Om nom nom nom, delicious data...')
  file = await bot.get_file(message.photo[-1].file_id)
  await bot.download_file(file.file_path, 'photo.jpg')


async def get_greeting(message: Message, bot: Bot):
  await message.answer('Hello!')
  json_str = json.dumps(message.dict(), default=str)
  print(json_str)