from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

BR = Element('br')


def make_node(nodeName, attrs=None, text=None):
    childNode = Element(nodeName)
    if attrs:
        try:
            set_attr(childNode, attrs)
        except:
            pass
            text = attrs
    if text:
        childNode.text = text
    return childNode


def set_attr(node, attrs):
    ls = attrs.split('^')
    for v in ls:
        key, val = v.split('=')
        node.set(key, val.replace('"', ''))


# --- test ---
ttt = Element('div')
print(ttt)
ttt.set('id', 'test00')
ttt.set('name', 'test11')
print(ttt.attrib)
ttt.text = 'HELL'
print(ttt.text)
# --- ---- ---


# /
root = Element('body')    # createElement

# div#myTitle
eDiv = make_node(
    'div', 'id="myTitle"^style="font-size:2em; color:tomato;"', '[[ MEMBER LOGIN ]]')
root.append(eDiv)

# hr
eHr = make_node('hr')
root.append(eHr)

root.append(BR)

# table
eTable = make_node('table', 'border=3px^style=border-color:gray')
root.append(eTable)

# table.tr
eTr = make_node('tr')

# table.tr.td
eTd = make_node('td', 'MemId')
eTr.append(eTd)

# table.tr.td
eTd = make_node('td')
eTr.append(eTd)

# table.tr.td.input
eInput = make_node('input', 'name=mem_id')
eTd.append(eInput)

eTable.append(eTr)

# table.tr
eTr = make_node('tr')

# table.tr.td
eTd = make_node('td', 'MemPwd')
eTr.append(eTd)

# table.tr.td
eTd = Element('td')
eTr.append(eTd)

# table.tr.td.input
eInput = make_node('input', 'name=mem_pwd^type=password')
eTd.append(eInput)

eTable.append(eTr)

# table.tr
eTr = make_node('tr')

# table.tr.td
eTd = make_node('td', 'colspan=2')
eTr.append(eTd)

# table.tr.td.input
eInput = make_node('input', 'type=submit^value=LOGIN')
eTd.append(eInput)
eTable.append(eTr)


# ----------------------------------
#  write file
# ----------------------------------
tree = ElementTree(root)
tree.write('./test.html')
