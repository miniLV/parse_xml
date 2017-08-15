
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# 读取xml文档 - demo.xml
tree = ET.ElementTree(file='demo.xml')

# 获取根节点
root = tree.getroot()

for child in root:
    print(child.tag,child.attrib)