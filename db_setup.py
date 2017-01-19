import logging
import sqlite3

from configuration.settings import COMPANY_TABLENAME, SOURCE_TABLENAME

logger = logging.getLogger('DATABASE')

conn = sqlite3.connect('test.db')
logger.info("Opened database successfully")

sql = '''SELECT name FROM sqlite_master WHERE type='table' AND name={};'''.format(COMPANY_TABLENAME)
if not conn.execute(sql):
    conn.execute('''CREATE TABLE {}
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL)'''.format(COMPANY_TABLENAME))

sql = '''SELECT name FROM sqlite_master WHERE type='table' AND name={};'''.format(SOURCE_TABLENAME)
if not conn.execute(sql):
    conn.execute('''CREATE TABLE IF NOT EXISTS {}
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL)'''.format(SOURCE_TABLENAME))

print "Table created successfully";
