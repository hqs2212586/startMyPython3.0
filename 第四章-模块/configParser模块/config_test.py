# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import configparser

conf = configparser.ConfigParser()  # 准备去处理文件
conf.read('config.ini')

print(conf.items('alex'))

