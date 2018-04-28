# python的logging模块提供标准的日志接口，可以用它存储各种格式的日志
"""
logging的日志分为debug()、info()、warning()、error()、critical()五个级别
    debug() 调试模式（详细）
    info() 记录（无错误）
    warning() 无错误但可能有潜在的危险
    error() 出现错误
    critical() 严重问题
"""
import logging

# 基本使用：日志打印
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")
"""
WARNING:root:user [alex] attempted wrong password more than 3 times
CRITICAL:root:server is down
"""

# 日志模块基本配置
# level=logging.INFO是把日志记录设置为INFO，只输入INFO或者比INFO级别更高的日志(日志级别过滤)
# logging.basicConfig(filename='log_test.log', level=logging.INFO)
#
# logging.debug("This message should go to the log file")
# logging.info("so should this")
# logging.warning("And this,too")
"""
log_test.log中仅写入了warning和info信息
"""


# 自定义日志格式
# 添加时间格式
logging.basicConfig(filename='log_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(name)s-%(filename)s-%(funcName)s-%(lineno)d-%(message)s',  # 参数固定格式
                    datefmt='%m/%d/%Y %I:%M:%S %p')

def sayhi():
    logging.error("from sayhi....")
sayhi()
logging.debug("This message should go to the log file")
logging.info("so should this")
logging.warning("And this,too")
"""
参数格式介绍：
%(name)s     # Logger的名字（用户名root）
    03/03/2018 11:20:55 AM-root-This message should go to the log file
%(levelno)s  # 打印数字形式的日志级别(10对应debug，20对应info，30对应warning)
    03/03/2018 11:18:13 AM-30-And this,too
%(levelname)s  # 打印文本形式的日志级别 
    03/03/2018 11:19:30 AM-WARNING-And this,too
%(pathname)s  # 调用日志输出函数的模块的完整路径名
%(filename)s  # 调用日志输出函数的模块的文件名

%(module)s  # 调用日志输出函数的模块名
%(funcName)s  # 调用日志输出函数的函数名
%(lineNo)d  # 调用日志输出函数的语句所在的代码行(44)
    03/03/2018 11:37:39 AM-root-logging_module.py-<module>-44-And this,too

%(created)f # 当前时间，用UNIX标准的表示是时间（一般时间用datafmt即可）
%(relaticeCreated)d  # 输出日志信息时，自Logger创建以来的毫秒数

%(asctime)s  # 字符串形式的当前时间，默认格式"2003-08-08 16:32:21,878",逗号后为毫秒数

%(thread)d  # 线程ID
%(threadName)s  # 线程名
%(process)d  # 进程ID

%(message)s  # 用户输出的消息
"""