from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsTrueContact(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.contact.user_id == message.from_user.id
