import os
import logging
import shutil

logging.basicConfig(filename='../log/folder.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


def create():
    try:
        os.makedirs('./temp', mode=0o777, exist_ok=False)
        logging.info(u'Created folder')
    except FileExistsError:
        logging.error(u'File exists error while creating folder')


def delete():
    try:
        os.removedirs('./temp')
        logging.info(u'Folder deleted')
    except FileNotFoundError:
        logging.error(u'File not found error while deleting folder')


def listdir():
    try:
        temp = os.listdir(path="./temp")
        logging.info(u'Listdir returned')
        return temp
    except FileNotFoundError:
        logging.error(u'File not found error while listdir')


def __add__(file):
    try:
        shutil.copy2(file, "./temp",  follow_symlinks=True)
        logging.info(u'File: ' + file + ' added')
    except FileNotFoundError:
        logging.error(u'File not found error while adding file: ' + file)


def clear():
    for file in os.listdir(path="./temp"):
        os.remove('./temp/' + file)
    logging.info(u'Folder cleared')
