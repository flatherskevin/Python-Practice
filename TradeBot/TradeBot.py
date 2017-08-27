import requests
import time

class TradeBot:
	def __init__(self, api_version='3'):
		self.__api_version = api_version
		self.__url = 'https://yobit.net/api/{api_version}/'.format(api_version=self.__api_version)

	def get_url(self):
		return self.__url

	class __Info:
		def __init__(self, parent, pair_list):
			assert list(pair_list)
			self.__parent = parent
			self.__url = '{super_url}ticker/{pair}'.format(super_url=parent.get_url(),pair='-'.join(pair_list))
			print(self.__url)
			self.__request = None
			self.__history = []

		def new_request(self):
			self.__request = requests.get(self.__url).json()
			self.__history.append(self.__request)
			
		@property
		def history(self):
			return self.__history

		def print_pretty(self, type='current'):
			def __print(data):
				print('\n\n')
				for item in self.__request:
					print('***{item}***'.format(item=item))
					for subitem in self.__request[item]:
						if subitem in ['buy','sell','high','low','avg','last']:
							self.__request[item][subitem] = '{0:.10f}'.format(self.__request[item][subitem])
						elif subitem == 'updated':
							self.__request[item][subitem] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(self.__request[item][subitem])))
						print('{key}	:	{value}'.format(key=subitem,value=self.__request[item][subitem]))
					print('\n\n')
			if type == 'current':
				__print(self.__request)
			elif type == 'history':
				for item in self.__history:
					__print(item)

	def Info(self, pair_list):
		return self.__Info(self, pair_list)

bot = TradeBot()

pair_list = ['btc_usd','html5_btc','maze_btc']

charlie = bot.Info(pair_list)

charlie.new_request()
charlie.print_pretty()