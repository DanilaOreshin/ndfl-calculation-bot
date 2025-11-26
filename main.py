import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from src.config.bot_config import config as cfg
from src.config.menu_config import set_commands
from src.handlers import command_handlers as ch
from src.handlers.basic_handlers import default_handler


async def set_up(bot: Bot):
    await set_commands(bot)


async def start():
    bot = Bot(token=cfg.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    # add /start and /about commands to menu
    dp.startup.register(set_up)

    # command handlers
    dp.message.register(ch.start_command_handler, Command(commands=['start']))
    dp.message.register(ch.about_command_handler, Command(commands=['about']))
    dp.message.register(ch.net_command_handler, Command(commands=['net']))
    dp.message.register(ch.gross_command_handler, Command(commands=['gross']))

    # default handlers
    dp.message.register(default_handler)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
