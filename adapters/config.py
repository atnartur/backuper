import os
import logging
from yaml import load
from app import tasks_dir_path

logging.basicConfig(level=logging.DEBUG, format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')


def config(name):
    logging.info(u'Opening config file')
    return load(open(os.path.join(tasks_dir_path, name + '.yml')))
