from adapters.task_config import *
from adapters.ssh import *

def run():
    print('task "test" executed')

    res = task_config('test')
    print(res)

    client = ssh(res['ssh']['host'], res['ssh']['user'], res['ssh']['pass'])
    stdin, stdout, stderr =  client.exec_command('ls -l')
    print(stdout.read() + stderr.read())
    client.close()