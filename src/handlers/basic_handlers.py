from aiogram.types import Message

from src.texts import messages as m


async def default_handler(message: Message):
    text = m.DEFAULT_TEXT
    await message.answer(text)
