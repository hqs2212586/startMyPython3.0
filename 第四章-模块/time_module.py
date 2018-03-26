# time模块



import time
time.time()  # 返回当前时间的时间戳（按秒计算的浮点数），从1970到现在的秒数
time.time()/3600/24/365  # 48.1865868219219年

time.localtime()  # 打印本地时间（操作系统时间）
# 输出：time.struct_time(tm_year=2018, tm_mon=2, tm_mday=26, tm_hour=10, \
#                       tm_min=33, tm_sec=26, tm_wday=0, tm_yday=57, tm_isdst=0)
time.localtime(1312344) # 根据参数（秒）计算日期
a = time.localtime()  # 赋值给a（创建时间对象），可以进行各种时间操作
'''
>>> a.tm_year 
2018
>>> '%s-%s-%s'%(a.tm_year,a.tm_mon,a.tm_mday)
'2018-2-26'
'''

time.gmtime()   # 打印格林威治时间（比北京时间晚8个小时）
# time.struct_time(tm_year=2018, tm_mon=2, tm_mday=26, tm_hour=2, tm_min=47, \
#                  ,tm_sec=49, tm_wday=0, tm_yday=57, tm_isdst=0)


time.mktime()   # 把一个时间对象转化为时间戳
'''
>>> time.mktime(a)   # 上面给a赋过值
1519612818.0
'''

time.sleep()   # 线程推迟指定的时间运行，单位为秒

time.asctime()  # 把一个表示时间的元祖或struct time转换表示形式
"""
>>> time.asctime()   # 如果没有参数将time.localtime作为参数传入
'Mon Feb 26 10:59:10 2018'
"""

time.ctime()  # 把一个时间戳转化为time_asctime()形式，默认以time.time()为参数
"""
>>> time.ctime()   # 相当于time.asctime(time.localtime(secs))
'Mon Feb 26 11:06:29 2018'
>>> time.ctime(-231334422)  # 参数可以为负
'Sun Sep  2 20:26:18 1962't
"""

time.strftime(format,a) # 把一个代表时间的元祖或struct time转化为格式化的时间字符串
"""
>>> time.strftime('%Y-%m-%d')
'2018-02-26'
>>> time.strftime('%Y-%m-%d %H:%M:%S')
'2018-02-26 11:19:47'
>>> time.strftime('%Y-%m-%d %H:%M:%S',a)
'2018-02-26 10:40:18'
>>> time.strftime('%Y-%m-%d %H:%M:%S %A',a)
'2018-02-26 10:40:18 Monday'
>>> time.strftime('%Y-%m-%d %H:%M:%S %p')
'2018-02-26 11:21:44 AM'
>>> time.strftime('%Y-%m-%d %H:%M:%S %U')   # 今年的第几周
'2018-02-26 11:21:55 08'
>>> time.strftime('%Y-%m-%d %H:%M:%S %w')   # 0-6,星期日是0
'2018-02-26 11:24:56 1'
"""

time.strptime('string', format)  # 把一个格式化时间字符串转化为struct_time,stftime的逆操作
"""
>>> s = time.strftime('%Y %m-%d %H:%M:%S')
>>> s
'2018 02-26 11:42:16'
>>> time.strptime(s,'%Y %m-%d %H:%M:%S')
time.struct_time(tm_year=2018, tm_mon=2, tm_mday=26, tm_hour=11, tm_min=42, \
                  tm_sec=16, tm_wday=0, tm_yday=57, tm_isdst=-1)
"""