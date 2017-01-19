import os
import yaml

DEBUG = True

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURR_DIR)
LOG_DIR = '{}/logs'.format(BASE_DIR)

CONFIG_FILE = '{}/{}'.format(
    CURR_DIR,
    'dev.yml' if DEBUG else 'prod.yml'
)


with open(CONFIG_FILE, 'r') as f:
    config = yaml.load(f)

SERVER = config['server']
USER = config['user_name']
PASSWORD = config['password']
PORT = config['port']
COMPANY_TABLENAME = 'company'
SOURCE_TABLENAME = 'login_source'
