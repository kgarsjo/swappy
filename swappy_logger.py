class SwappyLogger(object):
	
	ERROR_TAG = '[FAIL]: '
	INFO_TAG = '[INFO]: '
	SUCCESS_TAG = '[DONE]: '
	
	def _log(self, tag, msg):
		print '\r\n' + tag + msg
	
	def error(self, msg):
		self._log(SwappyLogger.ERROR_TAG, msg)

	def info(self, msg):
		self._log(SwappyLogger.INFO_TAG, msg) 
	
	def success(self, msg):
		self._log(SwappyLogger.SUCCESS_TAG, msg)