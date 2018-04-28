# 日志同时输出到屏幕和文件
"""
Python使用logging模块记录日志涉及四个主要类：
    1、logger提供了应用程度可以直接使用的接口；
    2、handler将（logger创建的）日志记录发送到合适的目的输出；
    3、filter对记录的日志过滤决定哪条日志输出；
    4、formatter决定日志记录的最终输出格式。
"""
import logging

# logger
# 每个程序在输出信息前都要获得一个Logger。
# Logger通常对应了程序的模块名。
LOG = logging.getLogger("chat.gui")  # 图形界面模块
LOG2 = logging.getLogger("chat.kernal") # 核心模块
# 指定最低的日志级别
logging.Logger.setLevel() # 低于指定级别将被忽略
# 添加或删除指定的filter
logging.Logger.addFilter()
logging.Logger.removeFilter()
# 添加或删除指定的handler
logging.Logger.addHandler()
logging.Logger.removeHandler()

# 设置日志级别


# handler
# handler对象负责发送相关信息到指定的目的地（控制台、文件、网络）
logging.Handler.setLevel()  # 指定被处理信息级别
logging.Handler.setFormatter()  # 给这个handler选择一个格式
logging.Handler.addFilter() # 新增一个filter对象
logging.Handler.removeFilter() # 删除一个filter对象

logging.StreamHandler # 可以向文件对象(类似sys.strout)输出信息
logging.FileHandler # 向文件输出日志，并且会打开文件

from logging import handlers
# RotatingFileHandler 同FileHandler类似，但可以管理文件大小。
# 当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出。
handlers.RotatingFileHandler()


# formatter组件（可以和handler组合使用）
fh = logging.FileHandler("access.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter) #把formmater绑定到fh上
