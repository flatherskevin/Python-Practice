import requests as re


class DataPull:

	def __init__(self, url, file, chunk_size=2000):
		self.__url = url
		self.__request = re.get(self.url, stream=True)
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

	@chunk_size.setter
	def file(self, value):
		self.__file = value

	@property
	def chunk_size(self):
		return self.__chunk_size

	@chunk_size.setter
	def chunk_size(self, value):
		assert int(value)
		self.__chunk_size = value

	def resend_request(self):
		self.request = re.get(self.url, stream=True)

	def download(self):
		with open('temp/{file}'.format(file=self.file)) as file:
			for chunk in re.iter_content(self.__chunk_size)