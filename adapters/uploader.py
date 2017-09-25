import logging
import os
import subprocess
from app import yadisk_dir, yadisk_token

def upload(local_path, project_name):
    for file in os.listdir(local_path):
        logging.info(u'Uploading ' + file)
        src = os.path.join(local_path, file)
        dest = os.path.join(yadisk_dir, project_name + '/')
        print(dest)
        try:
            subprocess.run('YDCMD_TOKEN=%s ydcmd put %s %s --verbose' % (yadisk_token, src, dest), shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error('ydcmd error %s %s' % (e.stdout, e.stderr))

