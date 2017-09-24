import logging
import os
from subprocess import call
from app import config


def upload(local_path, project_name):
    for file in os.listdir(local_path):
        logging.info(u'Uploading ' + file)
        logging.info(u'Result: ' + call(["YDCMD_TOKEN=" + config['yandex_disk']['token'] + " python ydcmd.py put " + os.path.join(local_path, file) + " " + os.path.join(config['yandex_disk']['dir'], project_name)]))