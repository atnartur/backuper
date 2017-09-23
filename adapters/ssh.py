import paramiko

host = '192.168.0.8'
user = 'login'
secret = 'password'
port = 22

def ssh(host, user, password, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    client.connect(hostname=host, username=user, password=password, port=port)
    return client

