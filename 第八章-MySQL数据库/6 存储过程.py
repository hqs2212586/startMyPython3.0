# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import pymysql

# 1、无参
# # 建立链接
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='1234',
#     db='db2',
#     charset='utf8'    # mysql指定utf-8的格式是没有杠的
# )
#
# # 拿游标
# cursor=conn.cursor()
#
# # 执行sql——存储过程
# cursor.callproc('p1')
# print(cursor.fetchall())
#
# # 仅仅是一个查询操作，不需要commit
#
# # 关闭链接
# cursor.close()
# conn.close()
"""
((1, '张磊老师'), (2, '李平老师'), (3, '刘海燕老师'), (4, '朱云海老师'), (5, '李杰老师'))
"""

# 2、有参
# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    db='db2',
    charset='utf8'    # mysql指定utf-8的格式是没有杠的
)

# 拿游标
cursor=conn.cursor()

# 执行sql——存储过程
cursor.callproc('p2',(2,4,0))
print(cursor.fetchall())
"""
((3, '刘海燕老师'),)
"""
# 得到返回值
cursor.execute('select @_p2_2')
print(cursor.fetchall())
"""
((1,),)
"""

# 仅仅是一个查询操作，不需要commit

# 关闭链接
cursor.close()
conn.close()