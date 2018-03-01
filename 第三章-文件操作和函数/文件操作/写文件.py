
# f = open(file='兼职.txt',mode='w',encoding='gbk')
# f.write('美女按摩服务，电话号：adfs123')
# f.close()

# w模式是创建新文件，如果文件存在则清空重写
f = open('兼职2.txt','wb')  # 写二进制
f.write("美女陪聊！".encode("gbk"))
f.close()