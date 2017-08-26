

class Color:

	class Color:
		pass

	class Hexcode(Color):
		def __init__(self, hexcode):
			try:
				if hexcode[0] == "#":
					self.__hexcode = hexcode[1:]
				else:
				 	self.__hexcode = hexcode
				assert len(self.__hexcode) in [6, 8], "The length of the hexcode is invalid"
				if len(self.__hexcode) == 6:
					self.__hexcode = hex(self.__hexcode)
			except Exception as err:
				self.__hexcode = "00FFFFFF"
				print(err)
				

		@property
		def hexcode(self):
			return self.__hexcode

		def __str__(self):
			return str(self.__hexcode)
	class Hsla(Color):
		pass

	class Rgba(Color):
		pass


jeff = Color.Hexcode("123456")
print(jeff.__str__())