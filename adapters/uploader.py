import logging
import os
import subprocess
import datetime
from app import yadisk_dir, yadisk_token

def upload(local_path, project_name):
    for file in os.listdir(local_path):
        logging.info(u'Uploading ' + file)
        src = os.path.join(local_path, file)
        today = '{:%Y-%m-%d}'.format(datetime.date.today())
        dest = os.path.join(yadisk_dir, project_name + '/', today, file).replace(os.path.sep, "/")

        try:
            my_env = os.environ.copy()
            my_env["YDCMD_TOKEN"] = yadisk_token
            proc = subprocess.Popen('ydcmd put %s %s --verbose' % (src, dest), shell=True, env=my_env)
            outs, errs = proc.communicate()
        except subprocess.CalledProcessError as e:
            logging.error('ydcmd error %s %s' % (e.stdout, e.stderr))

