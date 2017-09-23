import os
import logging
from yaml import load
from app import tasks_dir_path

logging.basicConfig(filename='../log/config.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


def config(name):
    logging.info(u'Opening config file')
    return load(open(os.path.join(tasks_dir_path, name + '.yml')))