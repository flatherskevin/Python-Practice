import sqlite3
import pandas as pd

class CSV2DB:

	def __init__(self, file, nrows=None, table='test', db='test.db'):
		self.file = file
		self.__db = db
		self.__table = table
		self.__nrows = nrows
		self.db_connect()
		self.csv_to_db()
		self.db_commit()
		self.db_close()

	def csv_to_db(self):
		print('Insertion into {table} started...'.format(table=self.__table))
		try:
			pd.read_csv(self.file, nrows=self.__nrows, encoding='latin-1').to_sql(self.__table, self.__conn)
		except Exception as err:
			print(err)
		print('Insertion into {table} complete'.format(table=self.__table))

	def db_connect(self):
		self.__conn = sqlite3.connect(self.__db)
		self.__c = self.__conn.cursor()
		print('Connected to {db}...'.format(db=self.__db))

	def db_commit(self):
		self.__conn.commit()
		print('Changes to {table} committed'.format(table=self.__table))

	def db_close(self):
		self.__conn.close()
		print('Connection to {db} closed'.format(db=self.__db))