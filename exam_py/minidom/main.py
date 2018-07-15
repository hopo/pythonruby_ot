from xml.dom import minidom
import os

document = minidom.Document()

xml = document.createElement('document')
document.appendChild(xml)

bodyChild = document.createElement('body')
bodyChild.setAttribute('class', 'prod01')

childOfBody = document.createElement('div')
childOfBody.setAttribute('id', 'myDiv')

text = document.createTextNode('hello xml.dom')
childOfBody.appendChild(text)

bodyChild.appendChild(childOfBody)
xml.appendChild(bodyChild)

xml_str = document.toprettyxml(indent='\t')

save_path_file = 'test.xml'

with open(save_path_file, 'w') as f:
    f.write(xml_str)
