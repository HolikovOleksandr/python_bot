from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start
from core.settings import settings
import logging
import asyncio



async def start_bot(bot: Bot):
  await bot.send_message(settings.bots.admin, 'Bot Administrator was started!')


async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin, 'Bot Administrator was stoped!')


async def start():
  logging.basicConfig(level=logging.INFO, 
                      format='%(asctime)s - [%(levelname)s] - %(name)s - '
                      '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
  
  bot = Bot(settings.bots.bot, parse_mode='HTML')
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

