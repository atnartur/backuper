import paramiko
import logging

def ssh(host, user, password, port=22, *args, **kwargs):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    logging.info(u'SSH connecting')
    client.connect(hostname=host, username=user, password=password, port=port, *args, **kwargs)
    return client
