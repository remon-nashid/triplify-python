import MySQLdb
from MySQLdb import constants
import datetime
import string
import config
conn = MySQLdb.connect(user='root', passwd='mysql', db='blog_database')
cursor = conn.cursor()

digits = {1:'one', 2:'two', 3:'three'}
for i in range(1, len(digits) + 1):
    print digits[i]
 