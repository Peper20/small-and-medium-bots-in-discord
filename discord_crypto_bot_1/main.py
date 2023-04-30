"""
Файл для быстрого запуска проекта. Запуск происходит в функции await main.

Проект использует зависимости определённые в requirements.txt (pip install -r requirements.txt)

Для корректной работы проекта требуется определить следующие переменные окружения:
	@DISCORD_BOT_TOKEN: токен для бота в дискорде
	@CRYPTO_RANKS_API_TOKEN: токен для api coinranking.com
	@DB_HOST: адрес для подключение к БД на postgres
	@DB_USER: юзер для подключение к БД на postgres
	@DB_PASSWORD: пароль для подключение к БД на postgres
	@DB_NAME: БД для подключение к БД на postgres

Желательно сделать это в файле .env в корневой папке проекта.
Для загрузки переменных окружения используется dotenv.load_dotenv (смотрите main.py, file body, await main)
"""



# requirements imports begin {

import os


from dotenv import load_dotenv as _load_dotenv
from asyncio import run as _run

# } requirements imports end



# file body begin {

async def main():
	"""
	Функция для быстрого запуска проекта.
	Запускает в 2 потоках бота и крипто-трекер

	@return:
		None, если закончилось успешно,
		Иначе бросает исключение.
		Может выполняться вечно (ничего не вернуть)
	"""


	_load_dotenv()


# } file body end



# other begin {

if __name__ == '__main__':
	_run(main())


__all__ = [n for n in globals() if n[:1] != '_']

# } other end
