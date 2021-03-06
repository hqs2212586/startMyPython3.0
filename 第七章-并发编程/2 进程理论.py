# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
一、什么是进程
    进程：正在进行的一个过程或者说一个任务，负责执行任务的是cpu。

二、进程和程序的区别
    程序仅仅是一堆代码，进程指的是程序的运行过程。
    以做蛋糕为例的话：
    蛋糕食谱就是程序（适当形式描述的算法）
    蛋糕师就是处理器
    蛋糕的原料就是输入的数据
    进程就是厨师阅读食谱、取各种原料及烘制蛋糕等一系列动作的总和。
    
    注意：同一个程序执行两次，那也是两个进程，比如打开暴风影音同一个软件，一个播放电影一个播放AV

三、并发与并行
    并发：伪并行，即看起来多个进程像在同时运行。单个cpu+多道技术可实现并发。
    
    并行：多个进程同时运行，只有具备多个cpu才能实现。
    
四、进程的创建
    但凡硬件都需要操作系统去管理。有操作系统就有进程，需要有创建进程的方式。
    （一）操作系统只为一个应用程序设计：如微波炉一旦启动，所有进程都已存在。
    （二）对于通用程序，需要有系统允许过程中创建或撤销进程的能力：
        1.系统初始化
        2.运行一个进程的过程中开启一个子进程(subprocess模块)。（并发）
        3.用户交互请求，创建新进程
        4.批处理作业的初始化
    新进程的创建都是由一个已经存在的进程执行了一个用于创建进程的系统调用而创建的！！！
        在UNIX中该系统调用是：fork  进程由操作系统管理。
        在windows中该系统调用是：CreateProcess
        
五、关于创建子进程UNIX和windows对比：
    相同点：进程创建后，父进程和子进程有各自不同的地址空间（多道技术要求物理层面实现进程之间内存的隔离），
           任何一个进程的在其地址空间中的修改都不会影响到另外一个进程。
    不同点：在UNIX中，子进程的初始地址空间是父进程的一个副本，提示：子进程和父进程是可以有只读的共享内存区的。
           但是对于windows系统来说，从一开始父进程与子进程的地址空间就是不同的。

六、进程的终止：
    1、正常退出：exit()
    2、出错退出：python a.py  a.py文件不存在
    3、严重错误：try...except...
    4、被其他进程杀死：kill -9
    
七、进程的层次结构
    相同点：无论UNIX或Windows，进程只有一个父进程。
    不同点：Unix中所有进程都以init进程为根，组成树形结构。
           Windows中没有进程层次概念，进程地位相同。创建进程时，父进程得到句柄，可以控制子进程，句柄可以传给其他子进程，因此没有层次。

八、进程的状态
    进程的状态有三种： 运行——》阻塞——》就绪（着重记住）
    
九、进程并发的实现
    硬件中断一个正在运行的进程，把此时进程运行的所有状态保存下来，为此，操作系统维护一张表格，即进程表（process table），每个进程占用一个进程表项（这些表项也称为进程控制块）。
    表存放了进程状态的重要信息：程序计数器、堆栈指针、内存分配状况、所有打开文件的状态、帐号和调度信息，以及其他在进程由运行态转为就绪态或阻塞态时，必须保存的信息，从而保证该进程在再次启动时，就像从未被中断过一样。
"""