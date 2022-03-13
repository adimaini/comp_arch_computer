import logging
from logging.config import fileConfig
from os import path

# import the logging.ini file
basepath = path.dirname(__file__)
logging_ini_filepath = path.abspath(path.join(basepath, "..", "logging.ini"))
#logging_ini_filepath = 'C:\\Users\\will9\\OneDrive\\Desktop\\simulator\\logging.ini'
fileConfig(logging_ini_filepath)
logger = logging.getLogger()


