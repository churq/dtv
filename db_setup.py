import logging
import sqlite3
import log
from constants import COMPANY_CODE, LOGIN_SOURCE_CODE

from configuration.settings import COMPANY_TABLENAME, SOURCE_TABLENAME

log.init()
logger = logging.getLogger('DATABASE')


logger.info("Opened database successfully")

def db_setup(tablename, code):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    def create_table():
        cur.execute('''CREATE TABLE {}
                       (ID TEXT PRIMARY KEY     NOT NULL,
                       NAME TEXT UNIQUE NOT NULL)'''.format(tablename))
        for item in code:
            cur.execute("INSERT INTO {}(ID, NAME) VALUES (?,?);".format(tablename), item)
        logger.info("Table created successfully")

    cur.execute('DROP TABLE IF EXISTS {}'.format(tablename))
    create_table()
    conn.commit()
    cur.close()
    conn.close()

def acquire_code(table_name, name):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    sql = '''select id from {} where name='{}';'''.format(table_name, name)
    response = cur.execute(sql)
    code = response.fetchall()
    cur.close()
    conn.close()

    return code[0][0] if code else None

if __name__ == '__main__':
    logger.info('setup database...')
    db_setup(SOURCE_TABLENAME, LOGIN_SOURCE_CODE)
    db_setup(COMPANY_TABLENAME, COMPANY_CODE)
    logger.info('Finish')
