try: 
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
# 要提交的数据字典
demo_dict = {
    'name':'laobin',
    'age':'18',
    'gender':'male',
    'like':'women',
}

# dict 转 xml
def dict_to_xml(tag,datas):
    elem = Element(tag)

    for key,value in datas.items():
        # 转成xml
        child = Element(key)
        child.text = str(value)

        elem.append(child)
    return elem

demo = dict_to_xml('stock',demo_dict)

# print(demo.text)

demo.set('my_id','333333')

# print(demo.text)

# 测试 - xml 中的值
find_Node = demo.find('like')
print(find_Node.text)

find_Node = demo.find('name')
print(find_Node.text)

