import os
import shutil


def getPath(projectName):
    path = os.path.abspath('../temp/' + projectName)
    try:
        os.makedirs(path, mode=0o777, exist_ok=False)
        return path
    except FileExistsError:
        pass


def clear(projectName):
    path = os.path.abspath('../temp/' + projectName)
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass

