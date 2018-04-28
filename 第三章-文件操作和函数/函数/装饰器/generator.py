# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

def run():
    count = 0
    while True:
        n = yield count
        print("--", n, count)
        count += 1


g =run()

g.__next__()
g.send("alex")
g.send("egon")
g.send("jack")
