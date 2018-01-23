#  -*- coding: utf-8 -*-
import paramiko
import logging

def ssh(host, user, password, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    logging.info(u'SSH connecting')
    client.connect(hostname=host, username=user, password=password, port=port)
    return client
