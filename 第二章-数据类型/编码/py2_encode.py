# python2.7测试用
# -*- coding:utf-8 -*-
"""
s = "武汉武昌"
print s

s2 = s.decode("utf-8")
print s2
print type(s2)

s3 = s2.encode("gbk")
s4 = s2.encode("utf-8")
print s3
print s4
"""

'''
    py3 文件默认编码是utf-8
        字符串 编码是unicode
        
    py2 文件默认编码是ascii
        字符串 编码默认是ascii
        如果文件头声明了gbk，那字符串的编码就是gbk
'''