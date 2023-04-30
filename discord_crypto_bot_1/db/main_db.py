"""
Локальный модуль для упращения взаимодействия с БД на postgres.

Взаимодействие происходит через экземпляр класса Database(Base_db).
Подключение осуществляется через переменные окружения.
До начала работы необходимо создать пользователя и БД.
"""


# requirements imports begin {

import os as _os
from dotenv import load_dotenv as _load_dotenv

# } requirements imports end



# relative imports begin {

if __name__ == '__main__':
    _load_dotenv()

    from base_db import Base_db
    
else:
    from .base_db import Base_db

# } relative imports end



# file body begin {

class Database(Base_db):
	def __init__(self, /, **kwargs):
		super().__init__(**kwargs)

		# self.execute("""
			# CREATE TABLE IF NOT EXISTS currencies(
				# id SERIAL PRIMARY KEY,
				# payload TEXT
			# )
		# """)


# } file body end



# other begin {

__all__ = [n for n in globals() if n[:1] != '_']

# } other end