if __name__ == '__main__':
    import os

    tasks_dir_path = os.environ.get('TASKS_DIR', 'tasks')

    tasks_dir = []
    try:
        tasks_dir = os.listdir(tasks_dir_path)
    except FileNotFoundError:
        print('tasks dir not found')
        exit(1)

    print(tasks_dir)

    for task_file in tasks_dir:
        if task_file.endswith('.py') and not task_file.endswith('__init__.py'):
            task_name = task_file[:-3]
            print('starting %s' % task_name)
            __import__(tasks_dir_path + '.' + task_name, globals(), locals())
