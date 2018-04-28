import logging

logger = logging.getLogger("access")
logger.setLevel(logging.ERROR)
# handler对象
ch = logging.StreamHandler()
fh = logging.FileHandler("access.log")
# 把handler对象绑定到logger对象
logger.addHandler(ch)
logger.addHandler(fh)
# 生成formatter对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 把formatter对象绑定handler对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.error("account [1234] too many login attempts")