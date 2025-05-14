import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

import core.bot_config as cfg
import core.handlers as h
from core.menu_config import set_commands


async def set_up(bot: Bot):
    await set_commands(bot)


async def start():
    bot = Bot(token=cfg.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    # add /start and /about commands to menu
    dp.startup.register(set_up)

    # command handlers
    dp.message.register(h.start_command_handler, Command(commands=['start']))
    dp.message.register(h.about_command_handler, Command(commands=['about']))
    dp.message.register(h.net_command_handler, Command(commands=['net']))
    dp.message.register(h.gross_command_handler, Command(commands=['gross']))

    # default handlers
    dp.message.register(h.default_handler)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
