def logger(filename, channel='file'):
    """
    日志方法
    :param filename: log filename
    :param channel: 输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
    :return:
    """



# 调用
log_obj = logger(filename="web.log", channel='both')
log_obj.__next__()
log_obj.send('user alex login success')