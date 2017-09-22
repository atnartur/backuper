if __name__ == '__main__':
    from os import listdir, environ, path

    tasks_dir_path = environ.get('TASKS_DIR', 'tasks')

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
            __import__(tasks_dir_path + '.' + task_name, globals(), locals())
