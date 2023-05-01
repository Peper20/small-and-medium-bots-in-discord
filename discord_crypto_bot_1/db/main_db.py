"""
Локальный модуль для упращения взаимодействия с БД на postgres.

Взаимодействие происходит через экземпляр класса Database(Base_db).
Подключение осуществляется через переменные окружения.
До начала работы необходимо создать пользователя и БД.
"""


# requirements imports begin {

import os as _os


from dotenv import load_dotenv as _load_dotenv
from loguru import logger as _logger

# } requirements imports end



# relative imports begin {

from .base_db import Base_db

# } relative imports end



# file body begin {

class Database(Base_db):
	def __init__(self, /, **kwargs):
		super().__init__(**kwargs)

		_logger.success('The new connection is probably opened successfully (If there were no exceptions and/or other logs, and this log was recorded, most likely the program does not work correctly)')

		self.execute("""
			CREATE TABLE IF NOT EXISTS currencies(
				id SERIAL PRIMARY KEY,
				payload TEXT
			)
		""")

		self.execute("""
			INSERT INTO currencies (id, payload)
			VALUES (1, '')
			ON CONFLICT DO NOTHING
		""")
		self.commit()


	def update(self, payload):
		self.execute(f"""
			UPDATE currencies SET
			payload='{payload}'
			WHERE id={1}
		""")

		self.commit()


# } file body end



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end