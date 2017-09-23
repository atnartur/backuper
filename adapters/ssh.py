import paramiko
import logging

host = '192.168.0.8'
user = 'login'
secret = 'password'
port = 22

logging.basicConfig(filename='../log/ssh.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


def ssh(host, user, password, port=22):
    logging.info(u'SSHClient')
    client = paramiko.SSHClient()
    logging.info(u'set_missing_host_key_policy')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    logging.info(u'Connecting')
    client.connect(hostname=host, username=user, password=password, port=port)
    return client

