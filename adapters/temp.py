import os
import shutil


def get_path(project_name):
    path = os.path.abspath(os.path.join(os.curdir, 'temp', project_name))
    try:
        os.makedirs(path, mode=0o777, exist_ok=False)
    except FileExistsError:
        pass
    return path


def clear(project_name):
    path = os.path.abspath(os.path.join(os.curdir, 'temp', project_name))
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


