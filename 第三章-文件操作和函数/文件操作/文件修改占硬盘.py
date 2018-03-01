import os

f_name = "兼职模特联系方式.txt"

f_new_name = "%s.new" %f_name
old_str = "白雪"
new_str = "白百合"

f = open(f_name,mode='r',encoding='utf-8')
f_new = open(f_new_name,'w',encoding='utf-8')

for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)

    f_new.write(line)
f.close()
f_new.close()

os.rename(f_new_name,f_name)    # 新文件替代旧文件

