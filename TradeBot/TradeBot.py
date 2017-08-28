import requests
import time
import itertools

class TradeBot:
	def __init__(self, api_version='3'):
		self.__api_version = api_version
		self.__url = 'https://yobit.net/api/{api_version}/'.format(api_version=self.__api_version)

	def get_url(self):
		return self.__url



	class __Info:
		def __init__(self, parent):
			assert list(pair_list)
			self.__parent = parent
			self.__url = '{super_url}info'.format(super_url=self.__parent.get_url())
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
			#self.__set_url(self.__pair_list)
			#print(self.__url)
			self.__request = None
			self.__request_json = {}
			self.__history = []
			self.__chunksize = 20

		@property
		def data(self):
			return self.__request_json

		@data.setter
		def data(self, value):
			self.__request_json = value

		@property
		def chunksize(self):
			return self.__chunksize

		@chunksize.setter
		def chunksize(self, value):
			self.__chunksize = value

		def new_request(self):
			for item in [self.__pair_list[i:i + self.__chunksize] for i in range(0, len(self.__pair_list), self.__chunksize)]:
				print('Request compiling for: {item}'.format(item=item))
				self.__set_url(item)
				__new = requests.get(self.__url)
				print('Status code: {code}'.format(code=__new.status_code))
				assert (__new.status_code == 200), 'URL status code error: {code}'.format(code=__new.status_code)
				print('Response gathered')
				for subitem in __new.json():
					self.__request_json[subitem] = __new.json()[subitem]
				print('Response added to master list\n\n')


			self.__history.append(self.__request_json)
			
		def __set_url(self, group):
			self.__url = '{super_url}ticker/{pair}'.format(super_url=self.__parent.get_url(),pair='-'.join(group))
			print('URL created: {url}'.format(url=self.__url))

		def __grouper(self, in_list, chunk=5):
			for i in range(0, len(in_list), chunk):
				yield in_list[i:i + chunk]

		@property
		def history(self):
			return self.__history

		def print_pretty(self, to_print=None, print_type='batch'):
			def __print(item):
				pass

			print('\n')
			if print_type == 'batch':
				#if to_print == None:
				#	to_print = self.__request_json
				#for item in to_print:
				#	__print(item)
				pass
			elif print_type == 'single':
				if to_print == None:
					to_print = 'html_btc'
				print('***{to_print}***'.format(to_print=to_print))
				print(to_print)
				for subitem in to_print:
					if subitem in ['buy','sell','high','low','avg','last']:
						to_print[subitem] = '{0:.10f}'.format(to_print[subitem])
					elif subitem == 'updated':
						to_print[subitem] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(to_print[subitem])))
					print('{key}	:	{value}'.format(key=subitem,value=to_print[subitem]))
				print('\n')

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
#jackie.print_pretty()
jackie.print_pretty(to_print=jackie.data['eth_btc'], print_type='single')