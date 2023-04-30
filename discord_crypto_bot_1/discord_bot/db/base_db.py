import psycopg2




class Base_db:
	connection = None


	def __init__(self, host, user, password, database):
		self.connection = psycopg2.connect(
			host=host,
			user=user,
			password=password,
			database=database,
		)


	def fetchone(self, command):
		answer = None

		with self.connection.cursor() as cursor:
			cursor.execute(command)
			answer = cursor.fetchone()

		return answer


	def fetchall(self, command):
		answer = None

		with self.connection.cursor() as cursor:
			cursor.execute(command)
			answer = cursor.fetchall()

		return answer


	def execute(self, command):
		answer = None

		with self.connection.cursor() as cursor:
			answer = cursor.execute(command)

		return answer

	def commit(self):
		return self.connection.commit()

