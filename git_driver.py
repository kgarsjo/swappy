from subprocess import CalledProcessError
from subprocess import call
from subprocess import check_call
from swap_exception import SwapException

class GitDriverException(SwapException):
	def __init__(self, error):
		self.value = error
	
	def __str__(self):
		return repr(self.value)

class GitDriver(object):
	GIT = 'git'
	GITPATH_FLAG = '-C'
	
	def __init__(self, gitPath):
		self.gitPath = gitPath
	
	def addAll(self):
		self.gitInvoke(['add', '-A'])
	
	def checkout(self, namespace):
		try:
			self.gitInvoke(['checkout', namespace], checkStatus = True)
		except CalledProcessError:
			raise GitDriverException('Unable to checkout ' + namespace)
	
	def commit(self, msg):
		self.gitInvoke(['commit', '-m', msg])
	
	def createBranch(self, namespace):
		try: 
			self.gitInvoke(['checkout', '-b', namespace], checkStatus = True)
		except CalledProcessError:
			raise GitDriverException('Unable to create ' + namespace)
	
	def gitInvoke(self, commandArgs, **kwargs):
		checkStatus = kwargs.get('checkStatus') or False
		gitBaseArgs = [GitDriver.GIT, GitDriver.GITPATH_FLAG, self.gitPath]
		self.invoke(gitBaseArgs + commandArgs, checkStatus)
	
	def init(self):
		try:
			self.gitInvoke(['init'])
		except CalledProcessError:
			raise GitDriverException('Unable to git-init');
	
	def invoke(self, args, checkStatus):
		if (checkStatus):
			check_call(args, shell = True)
		else:
			call(args, shell = True)
	
	def removeAll(self):
		self.gitInvoke(['rm', '-r', '*'])