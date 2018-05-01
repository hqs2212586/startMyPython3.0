# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
一、为什么要有操作系统
    现代的计算机系统主要是由一个或者多个处理器，主存，硬盘，键盘，鼠标，显示器，打印机，网络接口及其他输入输出设备组成。
    程序员无法把所有的硬件操作细节都了解到，管理这些硬件并且加以优化使用是非常繁琐的工作，这个繁琐的工作就是操作系统来干的，
    有了他，程序员就从这些繁琐的工作中解脱了出来，只需要考虑自己的应用软件的编写就可以了，应用软件直接使用操作系统提供的功能来间接使用硬件。

二、什么是操作系统
    操作系统就是一个协调、管理和控制计算机硬件资源和软件资源的控制程序。
    操作系统位于计算机硬件与应用软件之间，本质也是一个软件。
    操作系统由操作系统的内核（运行于内核态，管理硬件资源）以及系统调用（运行于用户态，为应用程序员写的应用程序提供系统调用接口）两部分组成

三、操作系统发展史
    1、第一代计算机（1940~1955）：真空管和穿孔卡片
    这个时期的电脑没有操作系统，所有程序设计都是直接操控硬件。程序员拿着他的插件版到机房里，将自己的插件板街道计算机里，这几个小时内他独享整个计算机资源，后面的一批人都得等着
    优点：在申请时间段内独享资源，即时调试程序。
    缺点：浪费计算机资源，一个时间段只有一个人用。
    
    2、第二代计算机（1955~1965）：晶体管和批处理系统
    程序员在穿孔卡片上写好程序，然后放在读卡机上，收集足够后，这些卡片读进磁带。机房管理人员把磁带装到磁带机上，
    操作人员装入一个特殊程序，它从磁带读取作业并运行输出到第二盘磁带，当作业全完成，
    取下输入和输出的磁带，把输出磁带拿到1401机器上进行脱机打印。
    1401：I/O操作  7094：计算操作
    特点：输入攒一大波、仍是顺序计算、输出攒一大波
    优点：批处理，节省时间
    缺点：1.流程需要人参与控制；2.计算过程仍然是顺序计算--》串行计算
         3.程序员等待结果和重新调试的过程都需要等同批次的其他程序都运作完才可以。（影响开发效率）
    
    3、第三代计算机（1965~1980）：集成电路芯片和多道程序设计
    由于第二代计算机有两套机型：
    7094大型科学计算机：主要用于科学计算和工程计算。（面向字）
    1401商用计算机：主要用于银行和保险从事磁带归档和打印服务。（面向字符）
    IBM通过system/360系列来同时满足上述要求，低档机与1401相当，高档机与7094相当。
    （1）解决人为参与问题：
    将作业从卡片读入磁盘，于是任何时刻当一个作业结束时，操作系统就能将一个作业从磁带读出，装进空出来的内存区域运行，这种技术叫做
    同时的外部设备联机操作：SPOOLING
    （2）解决串行计算问题：
    cpu运行的速度远远快于读取硬盘数据的速度，因此引入了内存，CPU可以非常快速地读取内存的数据。
    多道技术：多道指得是多个程序，解决多个程序竞争或共享同一个资源的有序调度问题，解决方式是多路复用。
             多路复用分时间复用和空间上的复用。
    空间上的复用：复用内存空间，内存同时存多个程序
        空间复用存在的问题：必须保证物理层面上多个程序的内存是互相隔离的。否则会丧失安全性和稳定性。
                正是由于内存物理隔离的问题，第三代计算机操作系统依然是批处理
    时间上的复用：大家共享cpu的时间，当一个程序在等待I/O时，另一个程序可以使用cpu，如果内存中可以同时存放足够多的作业，
                则cpu的利用率可以接近100%，类似于小学数学所学的统筹方法。
                这种切换（1）会在一个进程遇到io时进行；（2）一个进程占用cpu时间过长也会切换，或者说被操作系统夺走cpu的执行权限。
    （3）解决像第一代一样即时调试自己的程序
    分时操作系统：多个联机终端+多道技术，索引计算机能够为许多用户提供快速的交互式服务，所有的用户都以为自己独享了计算机资源
    UNIX:Ken Thompson开发了一个简易、单用户版本的MULTICS，为了使程序能在任何版本的unix上运行，IEEE提出了一个unix标准，即posix（可移植的操作系统接口Portable Operating System Interface）
    minix:教学用系统
    Linux:芬兰学生Linus Torvalds基于minix它编写
    
    4、第四代计算机（1980~至今）：个人计算机
    
四、总结
    1、操作系统的作用：
        1.隐藏丑陋复杂的硬件接口，提供良好的抽象接口
        2.管理、调度进程，并将多个进程对硬件的竞争变得有序。
        
    2、多道技术
        1.产生的背景：针对单核，实现并发（看起来多个进程像在同时运行，注意和并行的区别）  
            现在的主机一般是多核（几个核最多可以几个并行），那么每个核都会利用多道技术
            有4个cpu，运行于cpu1的某个程序遇到io阻塞，会等到io结束再重新调度，会被调度到4个
            cpu中的任意一个，具体由操作系统调度算法决定。
        2.空间上的复用：内存中同时有多道程序
        3.时间上的复用：复用一个cpu的时间片
            注意：遇到io切，占用cpu时间过长也切，核心在于切之前将进程的状态保存下来，这样
                 才能保证下次切换回来时，能基于上次切走的位置继续运行
"""