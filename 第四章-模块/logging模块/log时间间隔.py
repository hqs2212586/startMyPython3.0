import logging
from logging import handlers


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
# ch.setLevel(logging.DEBUG)  # 屏幕debug级别
# fh = logging.FileHandler("web.log")
fh = handlers.TimedRotatingFileHandler("web_jd.log", when="S", interval=5, backupCount=3)
# fh.setLevel(logging.WARNING)  # 文件设置WARNING级别
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
logger.debug("test log db backup 3")
