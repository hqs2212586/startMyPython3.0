import re
"""
Flags标志符
    re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
    M(MULTILINE): 多行模式，改变'^'和'$'的行为
    S(DOTALL): 改变'.'的行为,make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
    X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，下面这2个意思一样
"""

# re.I 忽视大小写
"""
>>> re.search('a', 'Alex')
>>> re.search('a', 'Alex',re.I)
<_sre.SRE_Match object; span=(0, 1), match='A'>
"""

# re.M 改变收尾匹配行为
"""
>>> re.search('foo.$','foo1\nfoo2\nfoo3\n')  # '$'匹配行尾
<_sre.SRE_Match object; span=(10, 14), match='foo3'>
>>> re.search('foo.$','foo1\nfoo2\nfoo3\n',re.M)
<_sre.SRE_Match object; span=(0, 4), match='foo1'>
"""

# re.S 改变'.'的行为
"""
>>> re.search('.','\n')  # '.'默认匹配除\n之外的任意一个字符
>>> re.search('.','\n', re.S)
<_sre.SRE_Match object; span=(0, 1), match='\n'>
"""

# re.X 允许给表达式写注释，使其可读
"""
>>> re.search('.  #test', 'alex', re.X)
<_sre.SRE_Match object; span=(0, 1), match='a'>
"""
a = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""",
                re.X)

b = re.compile(r"\d+\.\d*")