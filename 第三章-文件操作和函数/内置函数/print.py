

# print()   # 打印
"""
>>> s = 'hey, my name is alex\n, from shandong'
>>> print('haifeng','gangsf',sep='<-')
haifeng<-gangsf
"""

msg = "回到最初的起点"
f = open("print_tofile","w")
print(msg,"记忆里青涩的脸",sep="|",end="",file=f)
print(msg,"已经不忍直视了",sep="|",end="",file=f)