# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


import pymysql
# conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',database='egon')
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    db='db9',
    charset='utf8'    # mysql指定utf-8的格式是没有杠的
)

cursor=conn.cursor()

sql='insert into userinfo(user,pwd) values("xxx","123");'
rows=cursor.execute(sql)
print(cursor.lastrowid)   # 插入之前id走到的数字（下一条即将插入的记录的id）

conn.commit()

cursor.close()
conn.close()
"""
11
+----+--------+------+
| id | user   | pwd  |
+----+--------+------+
|  1 | egon   | 123  |
|  2 | alex   | 456  |
|  3 | hqs    | 123  |
|  5 | wxx    | 123  |
|  8 | yxx    | 123  |
|  9 | egon1  | 123  |
| 10 | zurong | 123  |
+----+--------+------+
"""