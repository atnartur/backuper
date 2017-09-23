import os
import shutil


def getPath(projectName):
    path = os.path.abspath('../temp/' + projectName)
    try:
        os.makedirs('../temp/' + projectName, mode=0o777, exist_ok=False)
        return path
    except FileExistsError:
        pass


def clear(projectName):
    try:
        shutil.rmtree('../temp/' + projectName)
    except FileNotFoundError:
        pass

