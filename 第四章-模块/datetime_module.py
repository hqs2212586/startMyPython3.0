
# datetime模块
# 相比time模块，datetime模块的接口更直观，更容易调用

import datetime
"""
datetime模块定义了下面几个类：
    1、datetime.date：表示日期的类，常用的属性有year,month,day
    2、datetime.time：表示时间的类，常用的属性有hour,minute,second,microsecond
    3、datetime.datetime：表示日期时间
    4、datetime.timedelta：表示时间间隔，即两个时间点之间的长度
    5、datetime.tzinfo：与时区相关信息
"""

a = datetime.datetime.now()
# datetime.datetime(2018, 2, 26, 12, 8, 18, 805166)

import time
d2 = datetime.date.fromtimestamp(time.time())  # 时间戳转化为年月日
# datetime.date(2018, 2, 26)

d2.timetuple()   # 转化为时间对象
# time.struct_time(tm_year=2018, tm_mon=2, tm_mday=26, tm_hour=0, \
#                   tm_min=0, tm_sec=0, tm_wday=0, tm_yday=57, tm_isdst=-1)


# 时间运算
'''
>>> a = datetime.datetime.now()
>>> t1 = datetime.timedelta(1)
>>> a - t1
datetime.datetime(2018, 2, 25, 13, 37, 13, 812339)

>>> a - datetime.timedelta(days=1)
datetime.datetime(2018, 2, 25, 13, 37, 13, 812339)
>>> a - datetime.timedelta(days=3)
datetime.datetime(2018, 2, 23, 13, 37, 13, 812339)
# 还支持hours、minutes、secends的运算
>>> a - datetime.timedelta(hours=3)
datetime.datetime(2018, 2, 26, 10, 37, 13, 812339)
>>> a + datetime.timedelta(hours=3)
datetime.datetime(2018, 2, 26, 16, 37, 13, 812339)
'''

# 时间替换
"""
>>> n = datetime.datetime.now()
>>> n.replace(year=2016)
datetime.datetime(2016, 2, 26, 13, 45, 26, 863002)
>>> n.replace(year=2017,month=4)
datetime.datetime(2017, 4, 26, 13, 45, 26, 863002)
>>> n.replace(year=2017,month=4,day=13)
datetime.datetime(2017, 4, 13, 13, 45, 26, 863002)
"""