
"""
正则匹配语法：
    re.match 从头开始匹配
    re.search 匹配包含
    re.findall 把所有匹配到的字符放到以列表中的元素返回
    re.split 以匹配到的字符当做列表分隔符
    re.sub 匹配字符并替换
    re.fullmatch 全部匹配
    re.compile  公式编译好，直接调用，提升效率
"""

# re.split()
"""
>>> s = 'alex22123jack233rain213jinxin5040'
>>> re.split('\d',s)  # 按数字分割
['alex', '', '', '', '', 'jack', '', '', 'rain', '', '', 'jinxin', '', '', '', '']
>>> re.split('\d+',s)
['alex', 'jack', 'rain', 'jinxin', '']
>>> s = 'alex22123jack233rain213jinxin5040|mack-Oldboy'
>>> re.split('\d+|\|' ,s)  # '|'是或     '\|'是转义
['alex', 'jack', 'rain', 'jinxin', '', 'mack-Oldboy']

>>> s = '8-2*4+1233/3*99*4*232+1232+10*234/14'
>>> re.split('[-\*/+]',s)
['8', '2', '4', '1233', '3', '99', '4', '232', '1232', '10', '234', '14']

"""

# re.sub() 字符替换
# re.sub(pattern, repl, string, count=0, flags=0)
# 控制替换操作次数
"""
>>> s = 'alex22123jack233rain213jinxin5040|mack-Oldboy'
>>> re.sub('\d+','-',s)
'alex-jack-rain-jinxin-|mack-Oldboy'
>>> re.sub('\d+','-',s,count=2)
'alex-jack-rain213jinxin5040|mack-Oldboy'
"""

# re.fullmatch  全部匹配
# re.fullmatch(pattern, string, flags=0)
# 整个字符串匹配成功就返回re object, 否则返回None
"""
>>> re.fullmatch('alex123','alex123')
<_sre.SRE_Match object; span=(0, 7), match='alex123'>
>>> re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboyedu.cn")  # (com|cn|edu)任选一个匹配
<_sre.SRE_Match object; span=(0, 17), match='alex@oldboyedu.cn'>
"""

# re.compile()  公式编译好了，直接拿去匹配提升效率
"""
>>> pattern = re.compile('\w+@\w+\.(com|cn|edu)')
>>> pattern.fullmatch('alex@oldboyedu.cn')
<_sre.SRE_Match object; span=(0, 17), match='alex@oldboyedu.cn'>
"""