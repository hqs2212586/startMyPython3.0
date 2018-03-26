f = open("兼职.txt", mode="r+", encoding="gbk")

f.fileno() # 返回文件句柄在内核中的索引值，做IO多路复用可以用到

f.flush()  # 把文件从内存buffer里强制刷新到硬盘

f.readable()  # 判断是否可读

f.readline()  # 只读一行，遇到\r  \n 为止

f.seek()      # 把操作文件的光标移到指定位置（按字节）
f.seek(0)     # 光标移动到文首

f.seekable()  # 判断文件是否可进行seek操作

f.tell()      # 返回当前文件操作光标位置（按字节）

f.truncate()  # 按指定长度截断文件（需要写权限），从光标当前位置开始往后截断
f.truncate(6) # 加上数字是从头开始截取6位字节

f.writable()  # 判断文件是否可写

f.read()      # 按字符，注意和tell和seek的区别
