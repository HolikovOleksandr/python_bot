import json
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard
from core.keyboards.inline import inline_buttons



async def get_inline(msg: Message, bot: Bot):
  ans = f'<b>Choose your future laptop: </b>'
  await msg.answer(ans, reply_markup=inline_buttons)



async def get_start(msg: Message, bot: Bot):
  ans = f'<tg-spoiler>Hello {msg.from_user.first_name}</tg-spoiler>'
  await msg.answer(ans, reply_markup=get_reply_keyboard())



async def get_location(msg: Message, bot: Bot):
  ans = 'Wow, you\'ve ended up in the middle of nowhere!'
  await msg.answer(ans)



async def get_photo(msg: Message, bot: Bot):
  await msg.answer('Ooo image?? Om nom nom nom, delicious data...')
  file = await bot.get_file(msg.photo[-1].file_id)
  await bot.download_file(file.file_path, 'photo.jpg')



async def get_greeting(msg: Message, bot: Bot):
  await msg.answer('Hello!')
  json_str = json.dumps(msg.dict(), default=str)
  print(json_str)
