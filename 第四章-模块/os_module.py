import os
# os模块提供了很多允许你的程序与操作系统直接交互的功能

os.getcwd()  # 得到当前工作目录，即当前Python解释器的目录路径
"""
vi /Users/huangqiushi/PycharmProjects/checkServer/test_os.py
import os
print(os.getcwd())

cd /
python /Users/huangqiushi/PycharmProjects/checkServer/test_os.py
输出：/
"""

os.listdir()  # 返回指定目录下所有文件和目录名
"""
>>> os.listdir(".")
['.idea', 'checkCpu.py', 'checkServer.py', 'home', 'test_new.py']
"""

os.remove()   # 函数用来删除一个文件
os.removedirs()   # 删除多个目录

os.path.isfile()  # 判断是否是一个文件
os.path.isdir()   # 判断是否是一个目录
os.path.isabs()   # 判断是否是绝对路径
os.path.exists()  # 检验路径是否真地存在（文件或目录）

os.path.split()   # 返回一个路径的目录名和文件名
"""
vi /Users/huangqiushi/PycharmProjects/checkServer/test_os.py
import os
print(os.path.split(os.getcwd()))

python test.py
输出：('/Users/huangqiushi/PycharmProjects', 'checkServer')
"""
os.path.splitext()  # 分离扩展名
"""
import os
print(os.path.splitext("Users/huangqiushi/PycharmProjects/checkServer/test.py"))

输出：('Users/huangqiushi/PycharmProjects/checkServer/test', '.py')
"""

os.path.dirname()  # 获取当前路径名
"""
>>> os.path.dirname('/home')
'/'
"""

os.path.abspath()   # 获取绝对路径
os.path.basename()  # 获取文件名

os.system()         # 执行shell命令，保存的是执行结果，0或1
"""
>>> os.system('df -h')
Filesystem      Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk1     112Gi   64Gi   47Gi    58% 16897618 12424108   58%   /
devfs          179Ki  179Ki    0Bi   100%      621        0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%        0        0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%        0        0  100%   /home
0   # linux命令执行返回值
"""
os.popen('df -h')  # 将系统交互内容保存到内存中



os.getenv("HOME")   # 读取操作系统环境变量HOME的值
os.environ   # 返回操作系统所有的环境变量
"""
>>> os.environ
environ({'TERM_PROGRAM': 'iTerm.app', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'CLICOLOR': '1', 
....
': '/Users/huangqiushi/Applications/anaconda3/bin/Python', 'OLDPWD': '/'})
"""
os.environ.setdefault('HOME','/home/hqs')  # 添加字典，没有就添加，有就会返回

os.linesep   # 返回当前平台使用的行终止符
"""
>>> os.linesep
'\n'   # Linux/OS X都是使用'\n'   windows使用'\r\n'
"""

os.name      # 提示正在使用的平台
"""
>>> os.name
'posix'     # 对于Linux/Unix用户，都是"posix"   windows是"nt"
"""
os.rename()  # 对一个文件改名
"""
>>> os.listdir(os.getcwd())
['.idea', 'checkCpu.py', 'checkServer.py', 'test_os.py']
>>> os.rename('test_os.py','test_new.py')
>>> os.listdir(os.getcwd())
['.idea', 'checkCpu.py', 'checkServer.py', 'test_new.py']
"""

os.makedirs()  # 创建多级目录
"""
>>> os.makedirs('home/hqs/test/test.py')
>>> os.listdir('home/hqs/test/')
['test.py']
"""
os.mkdir()    # 创建单个目录（不会递归，父目录不存在将报错）

os.stat('file')    # 获取文件属性  (主要是用来获取文件大小)
"""
>>> os.listdir(".")
['.idea', 'checkCpu.py', 'checkServer.py', 'home', 'test_new.py']
>>> os.stat(".")
os.stat_result(st_mode=16877, st_ino=6423017, st_dev=16777220, st_nlink=7, st_uid=501, st_gid=20, st_size=238, st_atime=1519638374, st_mtime=1519638170, st_ctime=1519638170)
>>> os.stat("test_new.py")
os.stat_result(st_mode=33188, st_ino=8278124, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=91, st_atime=1519634046, st_mtime=1519634046, st_ctime=1519634046)
"""

os.chmod('file')   # 修改文件权限和时间戳
"""
>>> os.chmod("test_new.py",755)
"""
os.path.getsize("filename")   # 获取文件大小
"""
>>> os.path.getsize('test_new.py')
91
"""
os.path.join('dir','filename')   # 结合目录名和文件名
"""
>>> os.path.join('root','test','test.py')
'root/test/test.py'
"""

os.chdir('dirname')  # 改变工作目录到dirname
"""
>>> os.getcwd()
'/Users/huangqiushi/PycharmProjects/checkServer'
>>> os.chdir('/tmp')
>>> os.getcwd()
'/private/tmp'
"""

os.get_terminal_size()  # 获取终端大小
"""
>>> os.get_terminal_size()
os.terminal_size(columns=80, lines=25)  # 能写25行，每行可以写入80个字符
"""

os.kill()  # 杀死进程
import signal
"""
>>> os.system('sleep 100000')
>>> os.system('ps aux|grep sleep')
huangqiushi      5164   0.0  0.0  2434840    776 s000  S+    6:10下午   0:00.00 grep sleep
huangqiushi      5162   0.0  0.0  2444652   1072 s000  S+    6:10下午   0:00.01 sh -c ps aux|grep sleep
huangqiushi      5141   0.0  0.0  2434824    364 s000  S     6:04下午   0:00.00 sleep 100000
>>> os.kill(5164,signal.SIGILL)
"""

