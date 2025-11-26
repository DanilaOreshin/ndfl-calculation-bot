from aiogram.filters import CommandObject
from aiogram.types import Message

from src.texts import messages as m
from src.utils.gross_func import get_gross_text
from src.utils.logger import logger
from src.utils.net_func import get_net_text


async def start_command_handler(message: Message):
    text = m.WELCOME_TEXT
    await message.answer(text)


async def about_command_handler(message: Message):
    text = m.ABOUT_TEXT
    await message.answer(text)


async def net_command_handler(message: Message, command: CommandObject):
    inner_value = command.args
    logger.info(f'Inner value = {inner_value}')
    text = await get_net_text(inner_value)
    await message.answer(text)


async def gross_command_handler(message: Message, command: CommandObject):
    inner_value = command.args
    logger.info(f'Inner value = {inner_value}')
    text = await get_gross_text(inner_value)
    await message.answer(text)
