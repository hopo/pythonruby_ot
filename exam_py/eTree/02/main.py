import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

# /
root = Element('body')    # createElement

# div#title
eDiv = Element('div')
eDiv.set('id', 'title') # setAttribute
eDiv.set('style', 'font-size:2em')
eDiv.text = '[[ Member Login ]]' # appendTextNode?
root.append(eDiv)

# table
eTable = Element('table')
eTable.set('border', '3px')
eTable.set('style', 'border-color:gray')
root.append(eTable)

# table.tr
eTr = Element('tr')

# table.tr.td
eTd = Element('td')
eTd.text = 'MemId'
eTr.append(eTd)

# table.tr.td
eTd = Element('td')

# table.tr.td.input
eInput = Element('input')
eInput.set('name', 'mem_id')
eTd.append(eInput)
eTr.append(eTd)
eTable.append(eTr)

# table.tr
eTr = Element('tr')

# table.tr.td
eTd = Element('td')
eTd.text = 'MemPwd'
eTr.append(eTd)

# table.tr.td
eTd = Element('td')

# table.tr.td.input
eInput = Element('input')
eInput.set('name', 'mem_pwd')
eInput.set('type', 'password')
eTd.append(eInput)
eTr.append(eTd)
eTable.append(eTr)

# table.tr
eTr = Element('tr')

# table.tr.td
eTd = Element('td')
eTd.set('colspan', '2')

# table.tr.td.input
eInput = Element('input')
eInput.set('type', 'submit')
eInput.set('value', 'LOGIN')
eTd.append(eInput)
eTr.append(eTd)
eTable.append(eTr)



# ----------------------------------
#  write file
# ----------------------------------
tree = ET.ElementTree(root)
tree.write('./test.html')

