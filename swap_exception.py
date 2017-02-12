class SwapException(Exception):
	def __init__(self, error):
		self.value = error
	
	def __str__(self):
		return repr(self.value)