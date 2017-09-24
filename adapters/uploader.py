import logging
import os
from subprocess import call
from app import yadisk_dir, yadisk_token

def upload(local_path, project_name):
    for file in os.listdir(local_path):
        logging.info(u'Uploading ' + file)
        src = os.path.join(local_path, file)
        dest = os.path.join(yadisk_dir, project_name)
        logging.info(u'Result: ' + call(["YDCMD_TOKEN=" + yadisk_token + " python ydcmd.py put " + src + " " + dest]))