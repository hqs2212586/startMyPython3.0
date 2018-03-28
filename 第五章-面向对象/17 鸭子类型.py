# 什么像鸭子，那它就是鸭子

# class File:
#     def read(self):
#         pass
#
#     def write(self):
#         pass
#
# class Disk:
#     def read(self):
#         print('disk read')
#
#     def write(self):
#         print('disk write')
#
# class Text:
#     def read(self):
#         print('text read')
#
#     def write(self):
#         print('text write')
#
#
# disk = Disk()
# text = Text()
#
# disk.read()
# disk.write()
#
# text.read()
# text.write()


# 序列类型：列表list、元组tuple、字符串str
l = list([1, 2, 3])
t = tuple(('a', 'b'))
s = str('hello')

print(l.__len__())
print(t.__len__())
print(s.__len__())


# python崇尚一种鸭子类型，类与类之间不用共同继承一个父类，只需要将它们做得像一种事物即可。
