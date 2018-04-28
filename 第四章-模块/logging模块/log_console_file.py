import logging


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""

    def filter(self, record):  # 固定写法
        return "db backup" not in record.getMessage()  # 字段不在日志消息内


# 生成logger对象
logger = logging.getLogger("web")
logger.setLevel(logging.DEBUG)  # 不设置日志级别，默认日志级别是warning
# 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

# 生成handler对象
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 屏幕debug级别
fh = logging.FileHandler("web.log")
fh.setLevel(logging.WARNING)  # 文件设置WARNING级别
# 把handler对象绑定到logger对象
logger.addHandler(ch)
logger.addHandler(fh)
# 生成formatter对象
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
# 把formatter对象绑定hander对象
ch.setFormatter(console_formater)
fh.setFormatter(file_formater)

logger.debug("test_log")
logger.warning("test_log_2")
logger.debug("test log db backup 3")  # filter测试，不记录这条日志
"""
在全局日志级别：info （不设置默认级别是warning,一般可以把全局设低把其他级别设高）
屏幕日志级别：debug
文件日志级别：warning
这种情况下，屏幕日志级别不生效，依然按照全局日志级别仅输出一条：
2018-03-03 16:27:28,508 - web - WARNING - 23 - test_log_2

全局设置为DEBUG后，console_handler设置为INFO，若输出的日志级别为DEBUG，则不会再屏幕显示

"""
