# ndfl-calculation-bot

Бот-калькулятор, который может вычислить сумму ЗП, получаемую сотрудником на руки, по сумме до вычета налогов или наоборот с учетом прогрессивной шкалы налогообложения РФ.

Для запуска необходимо:
1. Заполнить переменные конфигурации в файле /core/config/config.py
2. Запустить install_bot.bat и дождаться его завершения
3. Запустить бота, выполнив run_bot.bat 

### Команды:
- /net {число в формате 123.12}
- /gross {число в формате 123.12}

Например, если вы знаете сумму net (на руки), например, 100000.00, то команда /net 100000.00 преобразует ее в 114942.53 (т.е. gross).