import requests as re


class DataPull:

	def __init__(self, url, file='log.txt', chunk_size=2000):
		self.__url = url
		self.send_request()
		self.__file = file
		self.__chunk_size = chunk_size

	@property
	def url(self):
		return self.__url

	@property
	def request(self):
		return self.__request

	@property
	def file(self):
		return self.__file

	@file.setter
	def file(self, value):
		self.__file = value

	@property
	def chunk_size(self):
		return self.__chunk_size

	@chunk_size.setter
	def chunk_size(self, value):
		assert int(value)
		self.__chunk_size = value

	def send_request(self):
		print('Sending request to {url}...'.format(url=self.__url))
		self.__request = re.get(self.__url)
		print('Request received...')

	def download(self):
		with open(self.__file, 'wb') as file:
			for count,chunk in enumerate(iter(self.__request)):
				print('Writing chunk {chunk}...'.format(chunk=count))
				file.write(chunk)
