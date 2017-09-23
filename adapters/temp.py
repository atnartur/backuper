import os
import logging
import shutil


def getPath(projectName):
    path = os.path.abspath('./' + projectName)
    try:
        os.makedirs('./' + projectName, mode=0o777, exist_ok=False)
        logging.info(u'Created folder')
        return path
    except FileExistsError:
        logging.error(u'File exists error while creating folder')
        pass


def clear(projectName):
    try:
        shutil.rmtree('./' + projectName)
        logging.info(u'Folder deleted')
    except FileNotFoundError:
        pass

