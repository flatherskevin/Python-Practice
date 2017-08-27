import requests
import time
import itertools

class TradeBot:
	def __init__(self, api_version='3'):
		self.__api_version = api_version
		self.__url = 'https://yobit.net/api/{api_version}/'.format(api_version=self.__api_version)

	def get_url(self):
		return self.__url

	def __grouper(self, n, iterable, fillvalue=''):
		args = [iter(iterable) * n]
		return itertools.zip_longest(fillvalue=fillvalue, *args)

	class __Info:
		def __init__(self, parent):
			assert list(pair_list)
			self.__parent = parent
			self.__url = '{super_url}info'.format(super_url=parent.get_url())
			print(self.__url)
			self.__request = None
			self.__history = []
			self.__pairs = []

		def new_request(self):
			self.__request = requests.get(self.__url).json()
			self.__history.append(self.__request)
			self.__pairs_to_list()

		def __pairs_to_list(self):
			for item in self.__request['pairs']:
				self.__pairs.append(item)

		def print_pretty(self, type='current'):
			def __print(data):
				print('\n')
				for item in data['pairs']:
					print(item)

			if type == 'current':
				__print(self.__request)
			elif type == 'history':
				for item in self.__history:
					__print(item)

		@property
		def pairs(self):
			return self.__pairs


	class __Ticker:
		def __init__(self, parent, pair_list):
			assert list(pair_list)
			self.__parent = parent
			self.__pair_list = pair_list
			self.__set_url()
			print(self.__url)
			self.__request = None
			self.__request_json = {}
			self.__history = []

		def new_request(self):
			self.__request = requests.get(self.__url)
			if self.__request.status_code == 200:
				self.__request_json = self.__request.json()
			elif self.__request.status_code == 414:
				for item in self.__parent.__grouper(10, self.__pair_list):
					self.__set_url()
					self.__request_json = self.__request_json.append(requests.get(self.__url).json())

			self.__history.append(self.__request)
			
		def __set_url(self):
			self.__url = '{super_url}ticker/{pair}'.format(super_url=self.__parent.get_url(),pair='-'.join(self.__pair_list))

		@property
		def history(self):
			return self.__history

		def print_pretty(self, type='current'):
			def __print(data):
				print('\n')
				for item in data:
					print('***{item}***'.format(item=item))
					for subitem in data[item]:
						if subitem in ['buy','sell','high','low','avg','last']:
							data[item][subitem] = '{0:.10f}'.format(data[item][subitem])
						elif subitem == 'updated':
							data[item][subitem] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(data[item][subitem])))
						print('{key}	:	{value}'.format(key=subitem,value=data[item][subitem]))
					print('\n')
			if type == 'current':
				__print(self.__request_json)
			elif type == 'history':
				for item in self.__history:
					__print(item)

	def Ticker(self, pair_list):
		return self.__Ticker(self, pair_list)

	def Info(self):
		return self.__Info(self)



#######################################################################

bot = TradeBot()

pair_list = ['btc_usd','html5_btc','maze_btc']

charlie = bot.Info()


charlie.new_request()
#print(charlie.pairs)
#jackie = bot.Ticker(pair_list)
jackie = bot.Ticker(charlie.pairs)
jackie.new_request()
jackie.print_pretty()