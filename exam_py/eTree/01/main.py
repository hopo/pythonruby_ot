from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

root = Element('person')    # createElement
name = Element('name')

root.append(name)   # apeendChild
name.text = 'Harpa' # textContent

root.set('class', 'person') # setAttribute

print(etree.tostring(root))   # type: bytes

tree = ElementTree(root)
# tree.write(open(r'./eTree/test.xml', 'w'))
tree.write('./eTree/test.xml')
