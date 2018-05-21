# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 通过Navicat创建一个db9数据库并创建userinfo表：
"""
mysql> desc userinfo;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| user  | char(16) | NO   |     | NULL    |                |
| pwd   | char(20) | YES  |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+

mysql> select * from userinfo;
+----+------+------+
| id | user | pwd  |
+----+------+------+
|  1 | egon | 123  |
|  2 | alex | 456  |
+----+------+------+
"""
"""
# 登录数据库，允许远程访问
mysql> grant all on *.* to 'root'@'%' identified by '1234'; 
Query OK, 0 rows affected, 1 warning (0.01 sec)

# 立即刷新数据库，配置立即生效
mysql> flush privileges;
Query OK, 0 rows affected (0.01 sec)
"""