import requests

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

	def Info(self, pair_list):
		return self.__Info(self, pair_list)

bot = TradeBot()

pair_list = ['btc_usd','hcc_btc','maze_btc']

charlie = bot.Info(pair_list)

charlie.new_request()
print(charlie.history)