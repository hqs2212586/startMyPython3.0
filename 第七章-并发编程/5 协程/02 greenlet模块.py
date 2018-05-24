# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
greenlet模块：比generator更加便捷的切换方式，多个任务间很方便的切换。
             但不能监测I/O，因此比yield强一点，但不是研究的重点。
安装greenlet:pip3 install greenlet
"""
# from greenlet import greenlet
#
# def eat(name):
#     print("%s eat 1" % name)
#     g2.switch("hqs")
#     print("%s eat 2" % name)
#     g2.switch()
#
# def play(name):
#     print("%s play 1" % name)
#     g1.switch()
#     print("%s paly 2" % name)
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
#
# g1.switch('egon')   #可以在第一次switch时传入参数，以后都不需要
"""
egon eat 1
hqs play 1
egon eat 2
hqs paly 2
"""

# 检查greenlet面对i/o的情况是否可以切换:不能切换，无法提升效率
from greenlet import greenlet
import time

def eat(name):
    print("%s eat 1" % name)
    time.sleep(10)
    g2.switch("hqs")
    print("%s eat 2" % name)
    g2.switch()

def play(name):
    print("%s play 1" % name)
    g1.switch()
    print("%s paly 2" % name)

g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch('egon')
"""
egon eat 1   # 这一步卡了足足10秒
hqs play 1
egon eat 2
hqs paly 2
"""