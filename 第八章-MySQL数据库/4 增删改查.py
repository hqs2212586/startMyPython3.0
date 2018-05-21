# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import pymysql

# 1、增删改
# # 建立链接
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='1234',
#     db='db9',
#     charset='utf8'    # mysql指定utf-8的格式是没有杠的
# )
#
# # 拿游标
# cursor=conn.cursor()
#
# # 执行sql
# # 增删改
# sql='insert into userinfo(user,pwd) values(%s,%s);'
# # 单一操作
# # res=cursor.execute(sql,("wxx","123")) #执行sql语句，返回sql影响成功的行数
# # print(res)
#
# # 批量操作
# cursor.executemany(sql,[('yxx','123'), ('egon1','123'), ('zurong','123')])
#
#
# conn.commit()   # 注意：提交后记录才会插入成功
# # 关闭链接
# cursor.close()
# conn.close()
"""
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

# 2、查

# （1）查看记录
# 建立链接
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='1234',
#     db='db9',
#     charset='utf8'    # mysql指定utf-8的格式是没有杠的
# )
#
# # 拿游标
# cursor=conn.cursor()
#
# # 执行sql查询
# rows = cursor.execute('select * from userinfo;')    # 把sql发给服务端
# # print(rows)   # 显示的仅仅是受影响的行数
#
# # 为了得到执行结果，需要使用fetchone()函数，一次得到一条服务端执行记录
# print(cursor.fetchone())
# print(cursor.fetchone())
# """
# (1, 'egon', '123')
# (2, 'alex', '456')
# """
#
# conn.commit()   # 注意：提交后记录才会插入成功
# # 关闭链接
# cursor.close()
# conn.close()


# （2）转变为字典模式，查看记录
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    db='db9',
    charset='utf8'    # mysql指定utf-8的格式是没有杠的
)

# 拿游标
cursor=conn.cursor(pymysql.cursors.DictCursor)   # 基于字典的游标

# 执行sql查询
rows = cursor.execute('select * from userinfo;')
print(cursor.fetchall())   # 先移动到最后
# 游标移动——相对绝对位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动——从结果最开始起到第2条数据结尾
print(cursor.fetchone())
print(cursor.fetchone())
"""
[{'id': 1, 'user': 'egon', 'pwd': '123'}, ...]
{'id': 3, 'user': 'hqs', 'pwd': '123'}
{'id': 5, 'user': 'wxx', 'pwd': '123'}
"""
# 游标移动——相对当前位置移动
cursor.scroll(2,mode='relative') # 相对当前位置移动——从id=5这个结果开始，移动到id=9最后
print(cursor.fetchone())
print(cursor.fetchone())
"""
{'id': 10, 'user': 'zurong', 'pwd': '123'}
None    # 没有数据了还查询，即返回None
"""


conn.commit()   # 注意：提交后记录才会插入成功
# 关闭链接
cursor.close()
conn.close()
"""
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