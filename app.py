from os import listdir, environ, path
from yaml import load


try:
    config = load(open('config.yml'))
except FileNotFoundError:
    print('config not found')
    exit(1)

tasks_dir_path = environ.get('TASKS_DIR', 'tasks')


if __name__ == '__main__':
    tasks_dir = []
    try:
        tasks_dir = listdir(tasks_dir_path)
    except FileNotFoundError:
        print('tasks dir not found')
        exit(1)

    for task_file in tasks_dir:
        if path.isfile(path.join(tasks_dir_path, task_file)) and task_file.endswith('.py') and not task_file.endswith('__init__.py'):
            task_name = task_file[:-3]
            print('starting %s' % task_name)
            task = __import__(tasks_dir_path + '.' + task_name, globals(), locals(), ['run'])
            task.run()
