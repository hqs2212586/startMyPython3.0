# 动态参数
# 形式参数中出现*，传递的参数就可以不再是固定个数，会将传过来的所有参数打包为元组
def send_alert(msg,*users):
    for u in users:
        print('报警发送给',u)

# 方式一：
# 报警，十个运维人员
send_alert('注意系统资源别浪了','Alex','jack','tracy','wood')


# 方式二：
# send_alert('注意内存紧张',['alex','jack','tracy','wood'])  # 传入的参数是数据
send_alert('注意内存紧张',*['alex','jack','tracy','wood'])   # 传入的参数是数组内的元素
# 传入的参数由(['alex','jack','tracy','wood']) ————>('alex','jack','tracy','wood')


# 如果动态参数后还有参数
# 方法一：
def send_redalert(msg,*users,age):
    for u in users:
        print('CPU紧张',u)
# send_redalert("alex","rain",22)   # 22也会传递给*users
send_redalert("alex","rain",age=22)


def func(name, *args, **kwargs):
    # 方法二：
    # *args代表位置参数，它会接收任意多个参数并把这些参数作为元组传递给函数。
    # **kwargs代表的关键字参数，允许你使用没有事先定义的参数名，
    # 另外，位置参数一定要放在关键字参数的前面。
    print(name,args,kwargs)

func('Alex', 22, 'tesla', '500w', addr='湖北', num=123332313)
# Alex (22, 'tesla', '500w') {'addr': '湖北', 'num': 123332313}

d = {'degree':'primary school'}
func('Peiqi', **d)