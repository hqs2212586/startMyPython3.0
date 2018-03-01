# 写读是以创建的模式打开（将原来的东西覆盖），可以读取写入的内容
f = open("兼职联系信息.txt",'w+',encoding="gbk")
data = f.read()
print("content", data)

f.write("\nnewline 1学生")
f.write("\nnewline 2学生")
f.write("\nnewline 3学生")
f.write("\nnewline 4学生")

print("new content",f.read())

f.close()