from os import listdir, environ, path
from yaml import load
import logging


logging.basicConfig(level=logging.DEBUG, format= u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')

try:
    config = load(open('config.yml').read())
except FileNotFoundError:
    logging.error(u'Config not found')
    exit(1)

tasks_dir_path = environ.get('TASKS_DIR', 'tasks')


if __name__ == '__main__':
    tasks_dir = []
    try:
        tasks_dir = listdir(tasks_dir_path)
    except FileNotFoundError:
        logging.error(u'Task dir not found')
        exit(1)

    for task_file in tasks_dir:
        if path.isfile(path.join(tasks_dir_path, task_file)) and task_file.endswith('.py') and not task_file.endswith('__init__.py'):
            task_name = task_file[:-3]
            logging.error(u'starting %s' % task_name)
            task = __import__(tasks_dir_path + '.' + task_name, globals(), locals(), ['run'])
            task.run()

