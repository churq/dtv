import os

DEBUG = True

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURR_DIR)
LOG_DIR = '{}/logs'.format(BASE_DIR)

COMPANY_TABLENAME = 'company'
SOURCE_TABLENAME = 'login_source'
