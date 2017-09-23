import os
import shutil


def getPath(projectName):
    path = os.path.abspath(os.path.join('..', 'temp', projectName))
    try:
        os.makedirs(path, mode=0o777, exist_ok=False)
    except FileExistsError:
        pass
    return path


def clear(projectName):
    path = os.path.abspath(os.path.join('..', 'temp', projectName))
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
