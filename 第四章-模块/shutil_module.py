import shutil   # 需要研究每个功能的源码
# shutil  是高级的 文件、文件夹、压缩包 处理模块

# shutil.copyfileobj('fsrc','fdst','length')  # 将文件内容拷贝到另一个文件
"""
# 源代码：
def copyfileobj(fsrc, fdst, length=16*1024): 
    # copy data from file-like object fsrc to file-like object fdst
    while 1:  # 死循环
        buf = fsrc.read(length)   # 每次读这么长，直到读完
        if not buf:
            break
        fdst.write(buf)   # 写入目标文件
"""
f1 = open("sheve_test.py","r")
f2 = open("sheve_test_new.py","w")
shutil.copyfileobj(f1,f2)

"""
shutil.copyfile('src','dst')  # 拷贝文件

shutil.copymode('src','dst')  # 仅拷贝权限。内容、组、用户均不变

shutil.copystat('src','dst')  # 拷贝状态的信息。包括：mode、bits、atime、mtime、flags

shutil.copy('src','dst')   # 拷贝文件和权限 copyfile和copymode

shutil.copy2('src','dst')  # 拷贝文件和状态信息  copyfile和copystat
"""
"""
# 两个一起使用实现递归的拷贝
shutil.ignore_patterns(*patterns)
shutil.copytree(src,dst,symlinks=False,ignore=None)  # symlinks是软链接  ignore是忽略
"""
shutil.copytree('packages','pack2')
shutil.copytree('packages','pack3',ignore=shutil.ignore_patterns("__init__.py","view.py"))

# shutil.rmtree(path[,ignore_errors[,onerror]])   # 递归地去删除文件
shutil.rmtree("pack2")

# shutil.move(src,dst)  # 递归地去移动文件（剪切）
shutil.move("pack3","pack4")


# 文件压缩
"""
# shutil.make_archive(base_name,format,...)  # 创建压缩包并返回文件路径，例如：zip、tar
    base_name:压缩包名或路径 ，默认是当前目录
    format:压缩包种类
    root_dir:要压缩的文件夹路径，默认是当前目录
"""
ret = shutil.make_archive("/tmp/test_www",'gztar',root_dir='/Users/huangqiushi/PycharmProjects/checkServer/')
# 打包文件生成：/tmp/test_www.tar.gz