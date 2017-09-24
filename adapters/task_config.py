import os
from yaml import load
from app import tasks_dir_path


def task_config(name):
    return load(open(os.path.join(tasks_dir_path, name + '.yml')))
