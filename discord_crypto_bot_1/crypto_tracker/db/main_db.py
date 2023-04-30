import os as _os


from .base_db import Base_db
from json import dumps




class Database(Base_db):
	def __init__(self, *args, **kwargs):
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

