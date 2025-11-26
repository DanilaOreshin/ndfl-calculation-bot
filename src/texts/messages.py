from src.config.bot_config import config as cfg

# default
DEFAULT_TEXT = ('Неверное действие!\n\n'
                'Скорее всего ты видишь это сообщение, потому что пишешь отсебятину, но это не chatGPT 🙃\n\n'
                'Используй только доступные команды:\n'
                '🔸 /start\n'
                '🔸 /about\n'
                '🔸 /net\n'
                '🔸 /gross\n')

# commands
WELCOME_TEXT = ('Добро пожаловать! 🎉\n\n'
                'Краткая инструкция: \n'
                '🔸 Если ты знаешь сумму "на руки", то используй команду /net {число в формате 123456.00}\n\n'
                'Например, <code>/net 300000.00</code>\n\n'
                '🔸 Если ты знаешь сумму до вычета налогов, то используй команду /gross {число в формате 123456.00}\n\n'
                'Например, <code>/gross 250000.00</code>\n')

ABOUT_TEXT = (f'О боте:\n\n'
              f'Версия: {cfg.BOT_VERSION}\n'
              f'Автор: {cfg.BOT_DEVELOPER}\n')

# error
VALIDATION_ERROR_TEXT = ('⛔️ Возникла ошибка при обработке запроса!\n'
                         'Причина: {reason}')

# error reasons
NO_VALUE_REASON_TEXT = 'Число не передано!'

INVALID_FORMAT_REASON_TEXT = 'Неверный формат! Переданное значение не является числом!'

INVALID_RANGE_REASON_TEXT = ('Переданное число выходит за рамки допустимого диапазона!\n'
                             'Переданное число должно быть больше 0 и меньше {max_value}')
