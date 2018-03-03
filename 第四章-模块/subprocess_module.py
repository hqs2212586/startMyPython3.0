"""
除了os.system可以调用系统命令，commands,popen2等也可以，比较乱。
于是官方推出了subprocess,目地是提供统一的模块来实现对系统命令或脚本的调用
"""
import subprocess

# subprocess.run(['df', '-h'])  # df -h 执行立刻返回结果
"""
>>> a = subprocess.run(['df', '-h'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> a.stdout
输出并拿到结果
>>> a = subprocess.run(['df', '-sdfh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> a.stderr
b'df: illegal option -- s\n
usage: df [-b | -H | -h | -k | -m | -g | -P] [-ailn] [-T type] [-t] [filesystem ...]\n'

# 带管道符的情况,不要用列表（解析不了）；shell=True不做解析直接把整个命令交给shell处理
>>> a = subprocess.run('df -h | grep disk1',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
>>> a.stdout
b'/dev/disk1s1   233Gi   62Gi  168Gi    28%  871372 9223372036853904435    0%   /
/dev/disk1s4   233Gi  3.0Gi  168Gi     2%       3 9223372036854775804    0%   /private/var/vm\n'

>>> a = subprocess.run(['df','-ususidih'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
提示出现CalledProcessError报错
"""


# call方法
# 命令
"""
# 执行命令，返回命令执行状态， 0或非0
>>> retcode = subprocess.call(["ls", "-l"])
total 0
drwx------+  9 huangqiushi  staff   288  3  2 13:32 Desktop
drwx------+  4 huangqiushi  staff   128  3  1 08:17 Documents
...
drwxr-xr-x   7 huangqiushi  staff   224  3  2 20:26 PycharmProjects
>>> retcode
0

# 执行命令，如果命令结果为0，就正常返回，否则抛异常
>>> subprocess.check_call(["ls","-l"])
0
"""
# 字符串格式命令
"""
# 接收字符串格式命令，返回元组格式，第1个元素是执行状态，第2个是命令结果
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')

# 接收字符串格式命令，并返回结果(无状态)
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'
"""
# 执行命令，并返回结果（注意返回结果，不是打印）
"""
>>> res = subprocess.check_output(['du','-sh'])
>>> res
b' 27G\t.\n'
"""

# Popen方法（最重要、最底层）
"""
常用参数：
    args：shell命令，可以是字符串或者序列类型（如：list，元组）
    stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
    preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
    shell：shell=True的意思是这条命令直接交给系统去执行，不需要python负责解析
    cwd：用于设置子进程的当前目录
    env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
"""
# Popen发起一个新进程不影响子程序,run是当前进程执行，Popen是后台执行
"""
def sayhi():
    print('run...hahah')
>>> a = subprocess.Popen('sleep 10',shell=True,stdout=subprocess.PIPE,preexec_fn=sayhi)
>>> a.stdout  
<_io.BufferedReader name=3>
>>> a.stdout.read() 
b'run...hahah\n'
# cwd设置当前目录
>>> a = subprocess.Popen('echo $PWD;sleep 2',shell=True,cwd="/tmp",stdout=subprocess.PIPE,preexec_fn=sayhi)
>>> a.stdout.read()
b'run...hahah\n/private/tmp\n'
"""
def sayhi():
    print('run...hahah')
a = subprocess.Popen('echo $PWD;sleep 2',shell=True,cwd="/tmp",stdout=subprocess.PIPE,preexec_fn=sayhi)
a.poll()  # 检查子程序是否终止，返回返回值
a.wait()  # 等待子程序终止，返回返回值
a.terminate()  # kill进程
a.pid # 拿到所启动进程的进程号
"""
>>> a = subprocess.Popen('sleep 100',shell=True,stdout=subprocess.PIPE) 
>>> a.pid
14939
>>> a.terminate()  # 停掉不强制，进程没有停掉

>>> a = subprocess.Popen('for i in $(seq 1 100);do sleep 1;echo $i >> /tmp/sleep.log;done',shell=True,stdout=subprocess.PIPE)
>>> a.pid
15056
>>> a.kill()
"""

# 与启动的进程交互，发送数据到stdin,并从stdout接收输出，然后等待任务结束
# 需要用bytes进行交互、且只能交互一次
a.communicate()
"""
>>> a = subprocess.Popen('python3 guessAge.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
>>> a.communicate(b'1234')  # 需要和bytes进行交互
(b'guess age: try smaller,you have 3 chance\n
guess age: ', b'Traceback (most recent call last):\n
  File "guessAge.py", line 19, in <module>\n
      guess_age = int(input("guess age: "))\n
      EOFError: EOF when reading a line\n')
"""

# 发送系统信号
import signal
a = subprocess.Popen('sleep 100',stdout=subprocess.PIPE,shell=True)
a.send_signal(signal.SIGKILL)


