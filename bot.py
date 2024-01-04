from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import logging
import asyncio
import os


load_dotenv()
bot_token = os.getenv('BOT')
admin_id = os.getenv('ADMIN')



async def start_bot(bot: Bot):
  await bot.send_message(admin_id, 'Bot Administrator was started!')


async def stop_bot(bot: Bot):
  await bot.send_message(admin_id, 'Bot Administrator was stoped!')



async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f'<b>Hello {message.from_user.first_name}</b>')
  await message.answer(f'<s>Hello {message.from_user.first_name}</s>')
  await message.reply(f'<tg-spoiler>Hello {message.from_user.first_name}</tg-spoiler>')



async def start():
  logging.basicConfig(level=logging.INFO, 
                      format='%(asctime)s - [%(levelname)s] - %(name)s - '
                      '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
  
  bot = Bot(bot_token, parse_mode='HTML')
  dp = Dispatcher()

  dp.startup.register(start_bot)
  dp.message.register(get_start)
  
  dp.shutdown.register(stop_bot)

  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()



if __name__ == '__main__':
  asyncio.run(start())

