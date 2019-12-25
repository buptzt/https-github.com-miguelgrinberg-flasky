from pymysql import *
import json


try:
    db = connect("127.0.0.1", "root", "123456", "EmicallDev_system",charset='utf8')

    c = db.cursor()
    c.execute("select * from config where id < 200")

    results = c.fetchall()
    print(type(results))

    print(results)
    fields = ['id', 'configName','configValue']
    records = []
    for result in results:
        records.append(dict(zip(fields, result)))
    print(records)
    c.close()
except Exception as e:
    print(e)


