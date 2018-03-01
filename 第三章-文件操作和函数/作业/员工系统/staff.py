
"""
1.可进行模糊查询，语法至少支持下面3种查询语法:

find name,age from staff_table where age > 22

find * from staff_table where dept = "IT"

find * from staff_table where enroll_date like "2013"
2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增

语法: add staff_table Alex Li,25,134435344,IT,2015-10-29
3.可删除指定员工信息纪录，输入员工id，即可删除

语法: del from staff where  id=3
4.可修改员工信息，语法如下:

UPDATE staff_table SET dept="Market" WHERE  dept = "IT" 把所有dept=IT的纪录的dept改成Market
UPDATE staff_table SET age=25 WHERE  name = "Alex Li"  把name=Alex Li的纪录的年龄改成25
5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、修改语句就显示修改了多少条等。
"""
from tabulate import tabulate   # pip3 install tabulate
import os

DB_FILE = "staff.db"
COLUMNS = ['id', 'name', 'age', 'phone', 'dept', 'enrolled_data']  # 根据文件结构定义数据


def print_log(msg,log_type="info"):
    """
    :param msg: 字符串
    :param log_type:  'info' 或者 'error'
    :return:
    """
    if log_type == 'info':
        print("\033[32;1m%s\033[0m"%msg)   # 绿色
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m"%msg)   # 红色


def load_db(db_file):
    """
    加载员工信息表，并转成指定格式
    :param db_file:
    :return: data  数据在内存中存储
    """
    data = {}           # 空集合
    for i in COLUMNS:
        data[i] = []
    # data = {'id': [], 'name': [], 'age': [], 'phone': [], 'dept': [], 'enrolled_data': []}
    f = open(db_file,mode="r")    # 读取文件staff.db
    for line in f:
        staff_id,name,age,phone,dept,enrolled_date = line.split(",")  # 按","分隔
        data['id'].append(staff_id)
        data['name'].append(name)
        data['age'].append(age)
        data['phone'].append(phone)
        data['dept'].append(dept)
        data['enrolled_data'].append(enrolled_date)

    f.close
    return data


def save_db():
    """
    把内存数据存回硬盘
    :return:
    """
    f = open("%s.new"%DB_FILE,"w",encoding="utf-8")  # 生成新文件staff.db.new
    for index,staff_id in enumerate(STAFF_DATA['id']):  # index:0/1/2... staff_id:"1"/"2"/"3"...
        row = [staff_id]
        for col in COLUMNS:    # col: 'id'/'name'/'age'/'phone'/'dept'/'enrolled_data' 一行的每一项依次取值
            row.append( STAFF_DATA[col][index] )

        raw_row = ",".join(row)  # 按照自定义方法连接列表为字符串  eg. 1,Alex Li,25,13651054608,开发部,2013-04-01\n
        f.write(raw_row+"\n")

    f.close()

    # os.rename("%s.new"%DB_FILE,DB_FILE)  # 文件名修改，节省内存空间
    os.replace("%s.new"%DB_FILE,DB_FILE)   # 改用replace方法可以支持Windows平台使用

STAFF_DATA = load_db(DB_FILE)  # 加载文件信息先于main()执行


def op_gt(column,condtion_val):
    """

    :param column: eg. age
    :param condtion_val: eg. 22
    :return:[[id,name,age,phone],...]
    """
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):  # "age":['22', '28',...'22', '20', '26']
        if float(val) > float(condtion_val):      # 匹配上了
            # print("match",val)
            # matched_records.append(STAFF_DATA['id'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    # print("matched_records",matched_records)
    return matched_records


def op_lt(column,condtion_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):  # "age":['22', '28',... '22', '20', '26']
        if float(val) < float(condtion_val):  # 匹配上了
            # print("match", val)
            # matched_records.append(STAFF_DATA['id'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    # print("matched_records",matched_records)
    return matched_records


def op_eq(column, condtion_val):   # column='id'  condition_val='3'
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):  # "age":['22', '28',...'20', '26']  "id":['1','2',...,'10']
        if val == condtion_val:  # 匹配上了,可能是字符串对比    '3' == '3'
            # matched_records.append(STAFF_DATA['id'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)   # 得出id=3这一条的员工信息
    # print("matched_records",matched_records)
    return matched_records


def op_like(column, condtion_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):  # "age":['22', '28',...'22', '20', '26']
        if condtion_val in val:  # condition是条件
            print("match", val)
            # matched_records.append(STAFF_DATA['id'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    # print("matched_records",matched_records)
    return matched_records


def syntax_where(clause):  # del中  clause=' id=3'
    """
    解析where条件，并过滤数据
    :param clause: eg. age>22
    :return:
    """
    operators = {
        '>': op_gt,
        '<': op_lt,
        '=': op_eq,
        'like': op_like
    }

    for op_key,op_func in operators.items():  # op_key一一对应>,<,=,like    op_func一一对应op_gt\op_lt\op_eq\op_like
        if op_key in clause:    # e.g  '=' in '  id=3' 返回true
            print("clasuse", clause)
            column, val = clause.split(op_key)  # '  id=3'.split('=')  ————> [' id','3']分别对应column和val
            matched_data = op_func(column.strip(),val.strip())  # 去除截取语句前后的空格   id 和 3传入op_eq
            # print_log(matched_data)
            return matched_data

    else:   # 在for执行完成，且中间未被break情况下执行
        # 没匹配上任何条件公式
        print_log("syntax error!! where条件只能支持[>,<,=,like]",'error')

def syntax_find(data_set,query_clause):
    """
    解析查询语句并从data_set中打印指定的列
    :param data_set:  eg.<class 'list'>: [['1', 'Alex Li', '19', '13651054608', '开发部', '2013-04-01\n'], ['2', 'Jack Wang', '19', '13451024608', 'HR', '2015-01-07\n'], ['3', 'Rain Wang', '19', '13451054608', '开发部', '2017-04-01\n'], ['4', 'Mack Qiao', '19', '15653354208', 'Sales', '2016-02-01\n'], ['5', 'Rachel Chen', '19', '13351024606', '开发部', '2013-03-16\n'], ['6', 'Eric Liu', '19', '18531054602', 'Marketing', '2012-12-01\n'], ['7', 'Chao Zhang', '19', '13235324334', 'Administration', '2011-08-08\n'], ['8', 'Kevin Chen', '19', '13151054603', 'Sales', '2013-04-01\n'], ['9', 'Shit Wen', '19', '13351024602', '开发部', '2017-07-03\n'], ['10', 'Shanshan Du', '19', '13698424612', 'Operation', '2017-07-02']]
    :param query_clause: eg. 'find name,age from staff_table'
    :return:
    """
    filter_cols_tmp = query_clause.split("from")[0][4:].split(',')  # filter_cols_tmp = {list}<class 'list'>: [' name', 'age ']
    filter_cols = [i.strip() for i in filter_cols_tmp]   # filter_cols = {list}<class 'list'>: ['name', 'age']  去除了字符串的空格
    if '*' in filter_cols[0]:            # 带 * 就不需要检查下面的条件
        print(tabulate(data_set,headers=COLUMNS,tablefmt="grid"))
    else:
        reformat_data_set = []  # reformat_data_set = {list}<class 'list'>: [['Alex Li', '19'], ['Jack Wang', '19'], ['Rain Wang', '19']...]
        for row in data_set:     # eg. row={list}<class 'list'>: ['1', 'Alex Li', '19', '13651054608', '开发部', '2013-04-01\n']
            filtered_vals = []  # 把要打印的字段放在列表里  e.g filtered_vals = {list}<class 'list'>: ['Jack Wang', '19']
            for col in filter_cols:    # eg. col = {str}'name' or 'age' ...
                col_index = COLUMNS.index(col)  # 拿到列的索引，依此取出每条记录里对应索引的值  e.g col_index = {int} 1 or 2...
                filtered_vals.append( row[col_index] )
            reformat_data_set.append(filtered_vals)

        # for r in reformat_data_set:# 最终匹配到的数据
        #     print(r)
        print(tabulate(reformat_data_set,headers=filter_cols,tablefmt="grid"))   # 美化打印方式
    print_log("匹配到%s条数据！"%len(data_set))

def syntax_delete(data_set,query_clause):
    """

    :param data_set:  matched_records=[['3', 'Rain Wang', '19', '13451054608', '开发部', '2017-04-01\n']]
    :param query_clause: query_clause='del from staff '
    :return:
    """
    filter_cols_tmp = query_clause.split("from")[1].strip().split(',')   # ['staff']
    if filter_cols_tmp[0] == 'staff':
        for index, col in enumerate(COLUMNS):  # 刨去id一一对应  COLUMNS = ['id','name','age','phone','dept','enrolled_data']
            STAFF_DATA[col].remove(data_set[0][index])
    else:
        print_log("仅存在staff表" , 'error')

    print(tabulate(STAFF_DATA, headers=COLUMNS))
    save_db()
    print_log("成功从staff_table表删除1条记录")

def syntax_update(data_set,query_clause):
    """

    :param data_set: eg. [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01\n'],...]
    :param query_clause: eg. update staff_table set age=25
    :return:
    """
    formula_raw = query_clause.split('set')
    if len(formula_raw) > 1: # 有set关键字
        col_name,new_val = formula_raw[1].strip().split('=')  # age=25
        # col_index = COLUMNS.index(col_name)
        # 循环data_set取到每条记录的id，依据id到STAFF_DATA['id'] 里找对应id的索引，
        # 再根据索引去STAFF_DATA['age']列表里，改对应的值

        for matched_row in data_set:
            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        # print(STAFF_DATA) # 验证修改已经在内存内生效

        save_db() # 把修改后的数据刷到硬盘上
        print_log("成功修改了%s条数据"%len(data_set))
    else:
        print_log("语法错误：未检测到set关键字！",'error')


def syntax_add(data_set,query_clause):
    """

    :param data_set: [['1', 'Alex Li', '19', '13651054608', '开发部', '2013-04-01\n'], ['2', 'Jack Wang', '19', '13451024608', 'HR', '2015-01-07\n'], ['3', 'Rain Wang', '19', '13451054608', '开发部', '2017-04-01\n'], ['4', 'Mack Qiao', '19', '15653354208', 'Sales', '2016-02-01\n'], ['5', 'Rachel Chen', '19', '13351024606', '开发部', '2013-03-16\n'], ['6', 'Eric Liu', '19', '18531054602', 'Marketing', '2012-12-01\n'], ['7', 'Chao Zhang', '19', '13235324334', 'Administration', '2011-08-08\n'], ['8', 'Kevin Chen', '19', '13151054603', 'Sales', '2013-04-01\n'], ['9', 'Shit Wen', '19', '13351024602', '开发部', '2017-07-03\n'], ['10', 'Shanshan Du', '19', '13698424612', 'Operation', '2017-07-02']]
    :param query_clause: eg. add staff_table hqs,24,123122123,IT,2018-02-20
    :return:
    """
    column_vals_tmp = query_clause.split("staff_table")[1].split(',')    # e.g <class 'list'>: [' hqs', '24', '123122123', 'IT', '2018-02-20']
    column_vals = [i.strip() for i in column_vals_tmp]
    if len(column_vals) == len(COLUMNS[1:]):  # 不包含id,id是自增

        # find max id first , and then plus one , becomes the  id of this new record
        init_staff_id = 0
        for i in STAFF_DATA['id']:
            if int(i) > init_staff_id:
                init_staff_id = int(i)

        init_staff_id += 1  # 当前最大id再+1
        STAFF_DATA['id'].append(str(init_staff_id))
        for index, col in enumerate(COLUMNS[1:]):  # 刨去id一一对应
            STAFF_DATA[col].append(column_vals[index])

    else:
        print_log("提供的字段数据不足，必须字段%s" % COLUMNS[1:], 'error')

    print(tabulate(STAFF_DATA, headers=COLUMNS))
    save_db()
    print_log("成功添加1条记录到staff_table表")


def syntax_parser(cmd):    # e.g cmd = 'del from staff where  id=3'
    '''
    解析语句并执行
    :param cmd:
    :return:
    '''
    syntax_list = {
        'find': syntax_find,
        'del': syntax_delete,
        'update': syntax_update,
        'add': syntax_add
    }

    # find name,age from staff_table where age > 22
    # cmd.split() = ['del','from','staff','where','id=3']
    if cmd.split()[0] in ('find','add','del','update'):
        if 'where' in cmd:    # 如果命令中有where返回true
            query_clause,where_clause = cmd.split("where")  # query_clause='del from staff '; where_clause='  id=3'
            matched_records = syntax_where(where_clause)   # <class 'list'>: [['1', 'Alex Li', '19', '13651054608', '开发部', '2013-04-01\n'], ['2', 'Jack Wang', '19', '13451024608', 'HR', '2015-01-07\n'], ['3', 'Rain Wang', '19', '13451054608', '开发部', '2017-04-01\n'], ['4', 'Mack Qiao', '19', '15653354208', 'Sales', '2016-02-01\n'], ['5', 'Rachel Chen', '19', '13351024606', '开发部', '2013-03-16\n'], ['6', 'Eric Liu', '19', '18531054602', 'Marketing', '2012-12-01\n'], ['7', 'Chao Zhang', '19', '13235324334', 'Administration', '2011-08-08\n'], ['8', 'Kevin Chen', '19', '13151054603', 'Sales', '2013-04-01\n'], ['9', 'Shit Wen', '19', '13351024602', '开发部', '2017-07-03\n'], ['10', 'Shanshan Du', '19', '13698424612', 'Operation', '2017-07-02']]
        else:
        # query_clause,where_clause = cmd.split("where")  # 前半部分
        # print(query_clause,where_clause)
            matched_records = []    # 命令中没有where
            for index,staff_id in enumerate(STAFF_DATA['id']):  # staff_id索引
                record = []           # record = {list}<class 'list'>: ['1','Alex Li'...,'2013-04-01\n']
                for col in COLUMNS:   # col = {str}'id'('name'/.../'enrolled_data')
                    record.append(STAFF_DATA[col][index])
                matched_records.append(record)
            query_clause = cmd
        cmd_action = cmd.split()[0]   # eg. cmd_action = 'del from staff where id=3'.split()[0]  ——》'del'
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records,query_clause)   # e.g 跳入syntax_del函数执行

    else:
        # \033[31;1msysntax error!\033[0m  ——》红色
        print_log("syntax error!\n[find\\add\del\\update] [column,...] from [staff_table] [where]\
         [column] [>,<,...] [condition]",'error')


def main():
    """
    程序主入口
    :return:
    """
    while True:
        cmd = input("[staff_db]:").strip()   # e.g cmd ='del from staff where id=3'
        if not cmd: continue

        syntax_parser(cmd.strip())


main()  # 开始程序
