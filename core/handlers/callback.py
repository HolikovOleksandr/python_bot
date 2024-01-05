from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_inline_button(cb: CallbackQuery, bot: Bot):
  model = cb.data.split('_')[1]  
  size = cb.data.split('_')[2]  
  chip = cb.data.split('_')[3]  
  year = cb.data.split('_')[4]

  ans = f'{cb.message.from_user.first_name} you select Apple Macbook {model} with {size} diagonal on {chip} processor, {year} fabric edition'
  
  await cb.message.answer(ans)
  await cb.answer()

