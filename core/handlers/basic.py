import json
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard



async def get_start(mes: Message, bot: Bot):
  ans = f'<tg-spoiler>Hello {mes.from_user.first_name}</tg-spoiler>'
  await mes.answer(ans, reply_markup=get_reply_keyboard())



async def get_location(mes: Message, bot: Bot):
  ans = 'Wow, you\'ve ended up in the middle of nowhere!'
  await mes.answer(ans)



async def get_photo(mes: Message, bot: Bot):
  await mes.answer('Ooo image?? Om nom nom nom, delicious data...')
  file = await bot.get_file(mes.photo[-1].file_id)
  await bot.download_file(file.file_path, 'photo.jpg')



async def get_greeting(mes: Message, bot: Bot):
  await mes.answer('Hello!')
  json_str = json.dumps(mes.dict(), default=str)
  print(json_str)
