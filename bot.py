from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from core.handlers.basic import get_start, get_photo, get_greeting
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from core.utils.commands import set_commands
from core.settings import settings
import logging
import asyncio



async def start_bot(bot: Bot):
  await bot.send_message(settings.bots.admin, 'Bot Administrator was started!')

async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin, 'Bot Administrator was stoped!')



async def start():
  format_type = '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
  logging.basicConfig(level=logging.INFO, format=format_type)
  
  bot = Bot(settings.bots.bot, parse_mode='HTML')
  dp = Dispatcher()

  await set_commands(bot)

  dp.startup.register(start_bot)
  dp.shutdown.register(stop_bot)
  
  dp.message.register(get_start, CommandStart())
  dp.message.register(get_photo, F.photo)
  dp.message.register(get_true_contact, F.contact, IsTrueContact())
  dp.message.register(get_fake_contact, F.contact)

  dp.message.register(get_greeting, F.text == 'Hello')

  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()



if __name__ == '__main__':
  asyncio.run(start())

