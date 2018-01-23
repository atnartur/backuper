from os import listdir, environ, path
import logging
import time
import importlib.util
import sys

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

    # добавляем папку с задачами в список для поиска импортируемых файлов
    sys.path.insert(0, tasks_dir_path)

    print('starting')
    start_time = time.time()
    tasks_count = 0

    task_name = None

    # если указано название задачи, обрабатываем только ее
    if (len(sys.argv) > 1):
        task_name = sys.argv[1]

    for task_file in tasks_dir:
        if (task_name is not None):
            if (task_file != task_name + '.py'):
                continue

        if path.isfile(path.join(tasks_dir_path, task_file)) and task_file.endswith('.py') and not task_file.endswith('__init__.py'):
            task_name = task_file[:-3]
            logging.info(u'starting %s' % task_name)
            spec = importlib.util.spec_from_file_location("task", path.join(tasks_dir_path, task_file))
            task = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(task)
            task.run()
            tasks_count += 1

    print('finished: %s tasks processed on %.2f seconds' % (tasks_count, time.time() - start_time))
