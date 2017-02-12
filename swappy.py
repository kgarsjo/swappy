from datetime import datetime
from git_driver import GitDriver
from git_driver import GitDriverException
from subprocess import CalledProcessError
from subprocess import call
from subprocess import check_call
from swap_exception import SwapException
from swappy_logger import SwappyLogger
		
class Swappy(object):

	def __init__(self, gitPath):
		self.logger = SwappyLogger()
		self.git = GitDriver(gitPath)
		
	def afterSwitch(self, namespace):
		self.logger.success('Switched to namespace ' + namespace)

	def createRequestedNamespace(self, namespace):
		self.logger.info('Creating branch for namespace ' + namespace)
		self.git.createBranch(namespace)
		self.git.removeAll()
		self.git.commit(self.getCommitMessage())
		
	def closeCurrentNamespace(self):
		self.logger.info('Closing current namespace branch')
		self.git.addAll()
		self.git.commit(self.getCommitMessage())
	
	def initCurrent(self):
		self.logger.info('Initing git project if none exists');
		self.git.init();
		
	def getCommitMessage(self):
		now = datetime.now().isoformat()
		return 'Commit: ' + now;
	
	def openRequestedNamespace(self, namespace):
		self.logger.info('Attempting to switch to branch ' + namespace)
		try:
			self.git.checkout(namespace)
		except GitDriverException as e:
			self.createRequestedNamespace(namespace)
	
	def switchTo(self, namespace):
		try:
			self.initCurrent()
			self.closeCurrentNamespace()
			self.openRequestedNamespace(namespace)
			self.afterSwitch(namespace)
		except SwapException as e:
			self.logger.error(str(e))