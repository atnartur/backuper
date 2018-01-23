from os import listdir, environ, path
import logging
import time

logging.basicConfig(level=logging.INFO, format= u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')

tasks_dir_path = environ.get('TASKS_DIR', 'tasks')
yadisk_token = environ.get('YADISK_TOKEN')
yadisk_dir = environ.get('YADISK_DIR', 'backupstore')

if __name__ == '__main__':
    tasks_dir = []
    try:
        tasks_dir = listdir(tasks_dir_path)
    except FileNotFoundError:
        logging.error(u'Task dir not found')
        exit(1)

    print('starting')
    start_time = time.time()
    tasks_count = 0

    for task_file in tasks_dir:
        if path.isfile(path.join(tasks_dir_path, task_file)) and task_file.endswith('.py') and not task_file.endswith('__init__.py'):
            task_name = task_file[:-3]
            logging.info(u'starting %s' % task_name)
            task = __import__(tasks_dir_path + '.' + task_name, globals(), locals(), ['run'])
            task.run()
            tasks_count += 1

    print('finished: %s tasks processed on %.2f seconds' % (tasks_count, time.time() - start_time))
