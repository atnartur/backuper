import os
import shutil


def getPath(projectName):
    path = os.path.abspath('./' + projectName)
    try:
        os.makedirs(path, mode=0o777, exist_ok=False)
    except FileExistsError:
        pass
    return path

def clear(projectName):
    try:
        for file in os.listdir(path="./" + projectName):
            os.remove('./' + projectName + '/' + file)
        os.removedirs('./' + projectName)
    except FileNotFoundError:
        logging.error(u'File not found error while deleting temp folder')
