# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# pip3 install pymysql
import pymysql   # 套接字

user = input('user>>:').strip()
pwd = input('pwd>>:').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    db='db9',
    charset='utf8'    # mysql指定utf-8的格式是没有杠的
)

# 拿到游标
cursor=conn.cursor()     # 执行完毕返回的结果集默认以元组显示

# 执行sql语句
sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
rows = cursor.execute(sql)   # 游标的execute接口传入sql语句,返回sql查询成功的记录数

# 资源回收
cursor.close()  # 关闭游标
conn.close()    # 关闭连接

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
"""
user>>:egon
pwd>>:123
登录成功
"""