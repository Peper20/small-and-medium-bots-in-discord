"""
Локальный модуль для упращения взаимодействия с БД на postgres.

Взаимодействие происходит через экземпляр класса Database(Base_db).
Подключение осуществляется через переменные окружения.
До начала работы необходимо создать пользователя и БД.
"""


# requirements imports begin {

import os as _os

# } requirements imports end



# relative imports begin {

from .base_db import Base_db

# } relative imports end



# file body begin {

class Database(Base_db):
	def __init__(self, /, **kwargs):
		super().__init__(*args, **kwargs)

		# self.execute("""
			# CREATE TABLE IF NOT EXISTS currencies(
				# id SERIAL PRIMARY KEY,
				# payload TEXT
			# )
		# """)


database = Database(
	host=_os.getenv('DB_HOST'),
	user=_os.getenv('DB_USER'),
	password=_os.getenv('DB_PASSWORD'),
	database=_os.getenv('DB_NAME'),
)

# } file body end



# other begin {

__all__ = [n for n in globals() if n[:1] != '_']

# } other end