"""
Локальный модуль для базовой логики класса .main_db, file body, Database(Base_db)
"""


# requirements imports begin {

from functools import wraps as _wraps
import psycopg2 as _psycopg2

# } requirements imports end



# file body begin {

class Base_db:
	connection = None


	@_wraps(_psycopg2.connect)
	def __init__(self, /, **kwargs):
		self.connection = _psycopg2.connect(**kwargs)


	def fetchone(self, /, command):
		answer = None

		with self.connection.cursor() as cursor:
			cursor.execute(command)
			answer = cursor.fetchone()

		return answer


	def fetchall(self, /, command):
		answer = None

		with self.connection.cursor() as cursor:
			cursor.execute(command)
			answer = cursor.fetchall()

		return answer


	def execute(self, /, command):
		answer = None

		with self.connection.cursor() as cursor:
			answer = cursor.execute(command)

		return answer

	def commit(self, /):
		return self.connection.commit()

# } file body end



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end
