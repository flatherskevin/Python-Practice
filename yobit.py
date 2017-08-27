import requests
import json
import time
from decimal import *

class YoBit:
	def __init__(self, type):

		self.__link = 'https://yobit.net/api/3/ticker/{type}'.format(type=type)
		self.__request = requests.get(self.__link)
		self.__type = type
		self.__json = self.__request.json()[self.__type]


	@property
	def JSON(self):
		return self.__json

	@property
	def coin_type(self):
		return self.__type

	@property
	def request(self):
		return self.__request

	def print(self, type='json'):
		print('Gathering data from {url}...'.format(url=self.__request.url))
		if type == 'status':
			print(self.__request)
		elif type == 'json':
			for key in self.__json:
				if key != 'updated':
					value = self.__json[key]
					if key in ['buy','sell','high','low','avg','last']:
						value = '{0:.10f}'.format(value)
				else:
					value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(self.__json[key])))
				
				print('{key}: {value}'.format(key=key,value=value))
			print('...')
			print('Current Difference: {result}'.format(result=format(Decimal(self.__json['buy']) - Decimal(self.__json['sell']), '.10f')))


charlie = YoBit('maze_btc')
charlie.print()