from datetime import  datetime
import pytz
def getBrHour():
    tz = pytz.timezone('America/Sao_Paulo')
    now = datetime.now(tz).strftime("%d/%m/%Y %H:%M:%S")
    return str(now)

from prisma import Prisma
db = Prisma()

import sqlite3
def sqlite3RawQueryWithNoParams(query):
    dbSqlite = sqlite3.connect("./prisma/clinica.db")
    cursor = dbSqlite.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    dbSqlite.close()
    return list(res)

def sqlite3RawQueryWithParams(query, params):
    dbSqlite = sqlite3.connect("./prisma/clinica.db")
    cursor = dbSqlite.cursor()
    cursor.execute(query, (params))
    res = cursor.fetchone()
    cursor.close()
    dbSqlite.close()
    return list(res)

def sqlite3RawQueryWithParams2One(query, params):
    dbSqlite = sqlite3.connect("./prisma/clinica.db")
    cursor = dbSqlite.cursor()
    cursor.execute(query, (params))
    res = cursor.fetchone()
    cursor.close()
    dbSqlite.close()
    return res


