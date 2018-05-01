# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
参考博客：http: // www.cnblogs.com / Anker / p / 3271773.
html

一：僵尸进程（有害）
　　僵尸进程：一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵死进程。详解如下

我们知道在unix / linux中，正常情况下子进程是通过父进程创建的，子进程在创建新的进程。子进程的结束和父进程的运行是一个异步过程, 即父进程永远无法预测子进程到底什么时候结束，如果子进程一结束就立刻回收其全部资源，那么在父进程内将无法获取子进程的状态信息。

因此，UNⅨ提供了一种机制可以保证父进程可以在任意时刻获取子进程结束时的状态信息：
1、在每个进程退出的时候，内核释放该进程所有的资源，包括打开的文件，占用的内存等。但是仍然为其保留一定的信息（包括进程号the
process
ID，退出状态the
termination
status
of
the
process，运行时间the
amount
of
CPU
time
taken
by
the
process等）
2、直到父进程通过wait / waitpid来取时才释放.但这样就导致了问题，如果进程不调用wait / waitpid的话，那么保留的那段信息就不会释放，其进程号就会一直被占用，但是系统所能使用的进程号是有限的，如果大量的产生僵死进程，将因为没有可用的进程号而导致系统不能产生新的进程.此即为僵尸进程的危害，应当避免。

　　任何一个子进程(init除外)
在exit()
之后，并非马上就消失掉，而是留下一个称为僵尸进程(Zombie)
的数据结构，等待父进程处理。这是每个子进程在结束时都要经过的阶段。如果子进程在exit()
之后，父进程没有来得及处理，这时用ps命令就能看到子进程的状态是“Z”。如果父进程能及时
处理，可能用ps命令就来不及看到子进程的僵尸状态，但这并不等于子进程不经过僵尸状态。  如果父进程在子进程结束之前退出，则子进程将由init接管。init将会以父进程的身份对僵尸状态的子进程进行处理。
"""

"""
二：孤儿进程（无害）

　　孤儿进程：一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)
所收养，并由init进程对它们完成状态收集工作。

　　孤儿进程是没有父进程的进程，孤儿进程这个重任就落到了init进程身上，init进程就好像是一个民政局，专门负责处理孤儿进程的善后工作。每当出现一个孤儿进程的时候，内核就把孤
儿进程的父进程设置为init，而init进程会循环地wait()
它的已经退出的子进程。这样，当一个孤儿进程凄凉地结束了其生命周期的时候，init进程就会代表党和政府出面处理它的一切善后工作。因此孤儿进程并不会有什么危害。

我们来测试一下（创建完子进程后，主进程所在的这个脚本就退出了，当父进程先于子进程结束时，子进程会被init收养，成为孤儿进程，而非僵尸进程），文件内容

import os
import sys
import time

pid = os.getpid()
ppid = os.getppid()
print
'im father', 'pid', pid, 'ppid', ppid
pid = os.fork()
# 执行pid=os.fork()则会生成一个子进程
# 返回值pid有两种值：
#    如果返回的pid值为0，表示在子进程当中
#    如果返回的pid值>0，表示在父进程当中
if pid > 0:
    print
    'father died..'
    sys.exit(0)

# 保证主线程退出完毕
time.sleep(1)
print
'im child', os.getpid(), os.getppid()

执行文件，输出结果：
im
father
pid
32515
ppid
32015
father
died..
im
child
32516
1

看，子进程已经被pid为1的init进程接收了，所以僵尸进程在这种情况下是不存在的，存在只有孤儿进程而已，孤儿进程声明周期结束自然会被init来销毁。
"""
"""
三：僵尸进程危害场景：

　　例如有个进程，它定期的产生一个子进程，这个子进程需要做的事情很少，做完它该做的事情之后就退出了，因此这个子进程的生命周期很短，但是，父进程只管生成新的子进程，至于子进程
退出之后的事情，则一概不闻不问，这样，系统运行上一段时间之后，系统中就会存在很多的僵死进程，倘若用ps命令查看的话，就会看到很多状态为Z的进程。 严格地来说，僵死进程并不是问题的根源，罪魁祸首是产生出大量僵死进程的那个父进程。因此，当我们寻求如何消灭系统中大量的僵死进程时，答案就是把产生大
量僵死进程的那个元凶枪毙掉（也就是通过kill发送SIGTERM或者SIGKILL信号啦）。枪毙了元凶进程之后，它产生的僵死进程就变成了孤儿进
程，这些孤儿进程会被init进程接管，init进程会wait()
这些孤儿进程，释放它们占用的系统进程表中的资源，这样，这些已经僵死的孤儿进程就能瞑目而去了。
"""
# 四：测试
# 1、产生僵尸进程的程序test.py内容如下

# coding:utf-8
from multiprocessing import Process
import time, os


def run():
    print('子', os.getpid())


if __name__ == '__main__':
    p = Process(target=run)
    p.start()

    print('主', os.getpid())
    time.sleep(1000)

# 2、在unix或linux系统上执行
"""
[root @ vm172 - 31 - 0 - 19 ~]  # python3  test.py &
[1]
18652
[root @ vm172 - 31 - 0 - 19 ~]  # 主 18652
子
18653

[root @ vm172 - 31 - 0 - 19 ~]  # ps aux |grep Z
USER
PID % CPU % MEM
VSZ
RSS
TTY
STAT
START
TIME
COMMAND
root
18653
0.0
0.0
0
0
pts / 0
Z
20: 02
0: 00[python3] < defunct >  # 出现僵尸进程
root
18656
0.0
0.0
112648
952
pts / 0
S + 20: 02
0: 00
grep - -color = auto
Z

[root @ vm172 - 31 - 0 - 19 ~]  # top #执行top命令发现1zombie
top - 20: 03:42
up
31
min, 3
users, load
average: 0.01, 0.06, 0.12
Tasks: 93
total, 2
running, 90
sleeping, 0
stopped, 1
zombie
% Cpu(s): 0.0
us, 0.3
sy, 0.0
ni, 99.7
id, 0.0
wa, 0.0
hi, 0.0
si, 0.0
st
KiB
Mem: 1016884
total, 97184
free, 70848
used, 848852
buff / cache
KiB
Swap: 0
total, 0
free, 0
used.
782540
avail
Mem

PID
USER
PR
NI
VIRT
RES
SHR
S % CPU % MEM
TIME + COMMAND
root
20
0
29788
1256
988
S
0.3
0.1
0: 01.50
elfin
"""
# 3、
# 等待父进程正常结束后会调用wait／waitpid去回收僵尸进程
# 但如果父进程是一个死循环，永远不会结束，那么该僵尸进程就会一直存在，僵尸进程过多，就是有害的
# 解决方法一：杀死父进程
# 解决方法二：对开启的子进程应该记得使用join，join会回收僵尸进程
# 参考python2源码注释


class Process(object):
    def join(self, timeout=None):
        '''
        Wait until child process terminates
        '''
        assert self._parent_pid == os.getpid(), 'can only join a child process'
        assert self._popen is not None, 'can only join a started process'
        res = self._popen.wait(timeout)
        if res is not None:
            _current_process._children.discard(self)


# join方法中调用了wait，告诉系统释放僵尸进程。discard为从自己的children中剔除

# 解决方法三：http: // blog.csdn.net / u010571844 / article / details / 50419798