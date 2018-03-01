import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")  # 打开文件
root = tree.getroot()  #
"""
# print(root)
# 输出：<Element 'data' at 0x1019b2a48>
"""
print(root.tag)
# 输出：data

"""
#遍历xml文档
for child in root:
    # print(child.tag, child.attrib)
    print('-------',child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

输出：------- country {'name': 'Liechtenstein'}
     rank 2
     year 2008
     gdppc 141100
     neighbor None
     neighbor None
"""

"""
#只遍历year 节点
for node in root.iter('year'):
    print(node.tag,node.text)

输出：year 2008
     year 2011
     year 2011
"""