import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG, format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')


def getPath(projectName):
    try:
        os.makedirs('./' + projectName, mode=0o777, exist_ok=False)
        logging.info(u'Created folder')
        return os.path.abspath('./' + projectName)
    except FileExistsError:
        logging.error(u'File exists error while creating folder')


def clear(projectName):
    try:
        for file in os.listdir(path="./" + projectName):
            os.remove('./' + projectName + '/' + file)
        os.removedirs('./' + projectName)
        logging.info(u'Folder deleted')
    except FileNotFoundError:
        logging.error(u'File not found error while deleting folder')
