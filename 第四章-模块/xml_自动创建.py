
import xml.etree.ElementTree as ET


root = ET.Element("namelist")  # root
name = ET.SubElement(root,"name",attrib={"enrolled":"yes"})  # 在root下创建name节点，内容为"enrolled":"yes"
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = 'male'  # 性别

name2 = ET.SubElement(root,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(root) #生成文档对象

et.write("test.xml", encoding="utf-8",xml_declaration=True)  # 写入文档

ET.dump(root) #打印生成的格式
