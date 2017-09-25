import os
import shutil


def get_path(project_name):
    path = os.path.abspath(os.path.join('temp', project_name))
    try:
        return os.makedirs(path, mode=0o777, exist_ok=False)
    except FileExistsError:
        return path


def clear(project_name):
    path = os.path.abspath(os.path.join('temp', project_name))
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


