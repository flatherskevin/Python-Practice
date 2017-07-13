"""
User Profile
"""


class Profile(object):
	__default_properties = {
		'f_name': '',
		'l_name': '',
		'dob': '',
		'email': ''
	}

	def __init__(self):
		self.__properties = {
			'f_name': '',
			'l_name': '',
			'dob': '',
			'email': ''
		}

	@property
	def properties(self):
		return self.__properties

	@properties.setter
	def properties(self,value):
		self.__properties = value

	@property
	def default_properties(self):
		return self.__default_properties

	def __str__(self):
		return str(self.__properties)
