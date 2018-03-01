# a是追加模式
f = open('兼职联系信息.txt', 'ab')
f.write("\n白百何  北京  167  55  13523230322".encode("gbk"))   # 换行追加
f.close()

