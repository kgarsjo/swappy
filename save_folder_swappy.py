from datetime import datetime
from swappy import Swappy

class SaveFolderSwappy(Swappy):
	def __init__(self, savesPath):
		super(SaveFolderSwappy, self).__init__(savesPath)
	
	def getCommitMessage(self):
		now = datetime.now().isoformat();
		return 'Save from: ' + now;