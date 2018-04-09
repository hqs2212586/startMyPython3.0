# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import struct
import json

# 格式：struct.pack(fmt, *args)
# 设置格式后，把数字转成固定长度的bytes类型
# fmt='i'指的是整型数字
res = struct.pack('i', 1280)    # 打包
print(res, type(res), len(res))
"""
b'\x00\x05\x00\x00' <class 'bytes'> 4
"""

res1 = struct.pack('i', 1380)
print(res1, type(res1), len(res1))
"""
b'd\x05\x00\x00' <class 'bytes'> 4
"""

obj = struct.unpack('i', res)   # 解包
print(obj)  # obj是元组，第一个值就是打包的值
print(obj[0])
"""
(1280,)
1280
"""

# 第二种模式，长整型模式：
# res_i = struct.pack('i', 123000000000)
# print(res_i, len(res_i))
"""
struct.error: 'i' format requires -2147483648 <= number <= 2147483647
"""
res_l = struct.pack('l', 123000000000)  # l模式下，数字8个bytes，范围更大。
print(res_l, len(res_l))
"""
b'\x00\x0e_\xa3\x1c\x00\x00\x00' 8
"""


# 利用json处理特别长的数据
header_dic = {
    'filename': 'a.txt',
    'md5': 'xxdxxx',
    'total_size': 7678685767586786686876868687565756576655657565675657657657656757657565756757557575
}
header_json = json.dumps(header_dic)
# print(type(header_json))  # <class 'str'>
header_bytes = header_json.encode('utf-8')
#print(type(header_bytes))   # <class 'bytes'>

struct.pack('i', len(header_bytes))  # 把报头的长度打成固定长度
