import logging
import os
import subprocess
import datetime
from app import yadisk_dir, yadisk_token

def upload(local_path, project_name):
    for file in os.listdir(local_path):
        logging.info(u'Uploading ' + file)
        src = os.path.join(local_path, file)
        today = datetime.date.today()
        dest = os.path.join(yadisk_dir, project_name + '/', '%s-%s-%s/' % (today.year, today.month, today.day))

        try:
            subprocess.run('YDCMD_TOKEN=%s ydcmd put %s %s --verbose' % (yadisk_token, src, dest), shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error('ydcmd error %s %s' % (e.stdout, e.stderr))

