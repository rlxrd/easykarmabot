import re
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Filter

from app.database.requests import add_karma

router = Router()


class Search(Filter):
    async def __call__(self, message: Message):
        try:
            return re.search(r'\bспасибо\b', message.text, re.IGNORECASE)
        except:
            return False


@router.message(Search())
async def searcher(message: Message):
    try:
        user = message.reply_to_message.from_user
        if user and not user.is_bot and message.from_user.id != user.id:
            new_karma = await add_karma(user.id)
            await message.reply(f'Вы увеличили карму {user.first_name}, теперь его карма: {new_karma}')
    except:
        await message.answer('Ошибка')
