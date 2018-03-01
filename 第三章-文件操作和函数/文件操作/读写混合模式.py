
f = open('兼职联系信息.txt','r+',encoding="gbk")
data = f.read()
print("content",data)

f.write("\nnewline 1老师")
f.write("\nnewline 2老师")
f.write("\nnewline 3老师")
f.write("\nnewline 4老师")

print("new content", f.read())
# read不到结果，因为写入后光标已经移到末尾

f.close()
