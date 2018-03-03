import re

"""
常用表达式规则：
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
'*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
'{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
'\Z'    匹配字符结尾，同$ 
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
"""
# '.'匹配任意一个字符,默认从头开始找('\n'除外)
"""
>>> s = 'abc1d3e'
>>> s
'abc1d3e'
>>> re.search('.', s)  
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.search('..', s)
<_sre.SRE_Match object; span=(0, 2), match='ab'>
"""

# '^'匹配字符开头
"""
>>> re.search('^ab', 'hisisig')
>>> re.search('^ab', 'abssiif')
<_sre.SRE_Match object; span=(0, 2), match='ab'>
"""

# '$'匹配结尾
"""
>>> re.search('b$','bosojb')
<_sre.SRE_Match object; span=(5, 6), match='b'>
"""

# '*'匹配*前的字符任意次
"""
>>> re.search('b*','bosojb')
<_sre.SRE_Match object; span=(0, 1), match='b'>
>>> re.search('o*','booooojb')
<_sre.SRE_Match object; span=(0, 0), match=''>
>>> re.search('bo*','booooojb')
<_sre.SRE_Match object; span=(0, 6), match='booooo'>
>>> re.search('bo*','booooojb').group()
'booooo'
"""

# '+'匹配字符一次或多次
"""
>>> re.search('o+','booooojb')
<_sre.SRE_Match object; span=(1, 6), match='ooooo'>
>>> re.search('b+','booooojb')
<_sre.SRE_Match object; span=(0, 1), match='b'>
>>> re.search('.+','booooojb')
<_sre.SRE_Match object; span=(0, 8), match='booooojb'>
>>> re.search('ab+','booooojabbbb')
<_sre.SRE_Match object; span=(7, 12), match='abbbb'>
"""

# '?'匹配0次或1次
"""
>>> re.search('ab?','booooojabbbb')
<_sre.SRE_Match object; span=(7, 9), match='ab'>
>>> re.search('b?','booooojabbbb')
<_sre.SRE_Match object; span=(0, 1), match='b'>
"""

# '{m}' 匹配前一个字符m次
"""
>>> re.search('b{3}','booooojabbbb')
<_sre.SRE_Match object; span=(8, 11), match='bbb'>
>>> re.search('a{3}','booooojabbbb')
>>> re.search('[0-9]{3}','booo2213bb')
<_sre.SRE_Match object; span=(4, 7), match='221'>
"""

# '{n,m}'匹配前一个字符n到m次
"""
>>> re.search('[a-z]{3}','booo2213bb')
<_sre.SRE_Match object; span=(0, 3), match='boo'>
>>> re.search('[a-z]{2,5}','booo2213bb')
<_sre.SRE_Match object; span=(0, 4), match='booo'>
>>> re.search('[a-z]{2}','alex')
<_sre.SRE_Match object; span=(0, 2), match='al'>
>>> re.search('[a-z]{1,2}','alex')
<_sre.SRE_Match object; span=(0, 2), match='al'>
>>> re.search('[a-z]{1,2}','a2lex')
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.search('[a-z]{1,2}','2lex')
<_sre.SRE_Match object; span=(1, 3), match='le'>
"""

# '|'匹配左或右的字符
"""
>>> re.search('alex|Alex', 'Alex')
<_sre.SRE_Match object; span=(0, 4), match='Alex'>
>>> re.search('alex|Alex', 'alex')
<_sre.SRE_Match object; span=(0, 4), match='alex'>
>>> re.search('[a|A]lex', 'alex')  # 变化的部分用或【a|A】，实现简写
<_sre.SRE_Match object; span=(0, 4), match='alex'>
"""

# '(...)'分组匹配
"""
>>> re.search('[a-z]+', 'alex123213')
<_sre.SRE_Match object; span=(0, 4), match='alex'>
>>> re.search('([a-z]+)([0-9]+)', 'alex123213').group()
'alex123213'
>>> re.search('([a-z]+)([0-9]+)', 'alex123213').groups()
('alex', '123213')
"""

# '\'转义
# '\A' 从字符开头匹配  等同  '^'
"""
>>> re.search('\Aalex', 'alexadwwd')
<_sre.SRE_Match object; span=(0, 4), match='alex'>
"""

# '\Z'匹配字符结尾  等同'$'

# '\d'匹配数字0-9
# '\d+'贪婪匹配，匹配任意个
"""
>>> re.search('\d','booo2213bb')
<_sre.SRE_Match object; span=(4, 5), match='2'>
>>> re.search('\d+','booo2213bb')
<_sre.SRE_Match object; span=(4, 8), match='2213'>
"""

# '\D'匹配非数字
# '\D+'贪婪匹配
"""
>>> re.search('\D','booo2213bb')
<_sre.SRE_Match object; span=(0, 1), match='b'>
>>> re.search('\D+','booo2213bb')
<_sre.SRE_Match object; span=(0, 4), match='booo'>
"""

# '\w' 匹配[A-Za-z0-9]
"""
>>> re.search('\w+','booo2213bb')
<_sre.SRE_Match object; span=(0, 10), match='booo2213bb'>
>>> re.search('\w','booo2213bb')
<_sre.SRE_Match object; span=(0, 1), match='b'>
"""

# '\W' 匹配非[A-Za-z0-9]（特殊字符）
"""
>>> re.search('\W','%$#^&((*hhga')
<_sre.SRE_Match object; span=(0, 1), match='%'>
>>> re.search('\W+','%$#^&((*hhga')
<_sre.SRE_Match object; span=(0, 8), match='%$#^&((*'>
"""

# '\s' 匹配空白字符
"""
>>> s = 'hssis\nisijsi\njack'
>>> print(s)
hssis
isijsi
jack
>>> re.search('\s',s)
<_sre.SRE_Match object; span=(5, 6), match='\n'>
>>> re.search('\s+',s)
<_sre.SRE_Match object; span=(5, 6), match='\n'>
>>> re.findall('\s+',s)
['\n', '\n']
"""

# '(?P<name>...)' 分组匹配
"""
>>> s = '230701200104280028'
>>> re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_date>\d{8})(?P<seq>\d{4})',s)
<_sre.SRE_Match object; span=(0, 18), match='230701200104280028'>
>>> re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_date>\d{8})(?P<seq>\d{4})',s).groups()
('230', '701', '20010428', '0028')
>>> res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_date>\d{8})(?P<seq>\d{4})',s)
>>> res.groupdict()
{'province': '230', 'city': '701', 'born_date': '20010428', 'seq': '0028'}
"""