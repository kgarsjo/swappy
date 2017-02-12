import getopt
import sys
from save_folder_swappy import SaveFolderSwappy

opts, args = getopt.getopt(sys.argv[1:], '')
savesPath = args[0];
namespace = args[1]
swappy = SaveFolderSwappy(savesPath)
swappy.switchTo(namespace)

