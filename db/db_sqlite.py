import sqlite3
import os

dbPath = 'data.sqlite'

if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)

    cur = conn.cursor()
    cur.execute('''create table persons (
                                        id INT PRIMARY KEY  not null,
                                        name  TEXT          not null,
                                        age   INT           not null,
                                        addr  char(50),
                                        salary   real); ''') 
    conn.commit()
    conn.close()
    print("create sqlite db success")


conn = sqlite3.connect(dbPath)
cur = conn.cursor()

cur.execute("delete from persons")

cur.execute("insert into persons (id, name ,age, addr, salary)values(1,'zt', 27, 'nanjing', 20000.01)")
cur.execute("insert into persons (id, name ,age, addr, salary)values(2,'lnp', 56, 'hefei', 30000.01)")
cur.execute("insert into persons (id, name ,age, addr, salary)values(3,'zys', 57, 'shanghai', 40000.01)")
cur.execute("insert into persons (id, name ,age, addr, salary)values(4,'zz', 30,'beijing', 50000.01)")
conn.commit()

print("insert  4 msg success!")


persons = cur.execute("select * from persons order by age")

print (type(persons))

result = []

for person in persons:
    value = {}
    value['name'] = person[1]
    value['age'] = person[2]
    value['addr'] = person[3]
    value['salary'] = person[4]
    result.append(value)
conn.close()
print (result)

import json

resultJsonStr = json.dumps(result)
print(resultJsonStr)
