from aiogram.filters import CommandObject
from aiogram.types import Message

import core.functions as f
from core import messages as m


# handlers
async def start_command_handler(message: Message):
    text = m.welcome_text
    await message.answer(text)


async def about_command_handler(message: Message):
    text = m.about_text
    await message.answer(text)


async def net_command_handler(message: Message, command: CommandObject):
    net_sum = float(command.args.replace(" ", ""))
    gross_sum = f.calculate_gross_sum(net_sum)
    result_list = f.calculate_net_by_month(gross_sum)
    text = f.get_report_text(gross_sum, net_sum, result_list)
    await message.answer(text)


async def gross_command_handler(message: Message, command: CommandObject):
    gross_sum = float(command.args.replace(" ", ""))
    net_sum = f.calculate_net_sum(gross_sum)
    result_list = f.calculate_net_by_month(gross_sum)
    text = f.get_report_text(gross_sum, net_sum, result_list)
    await message.answer(text)


async def default_handler(message: Message):
    text = m.default_text
    await message.answer(text)
