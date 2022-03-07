import lxml.etree as et


root = et.Element('knights')

# print(root, root.tag)

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = et.SubElement(root, 'knight', title=title)
        name_element = et.SubElement(knight, 'name')
        name_element.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment


xml_string = et.tostring(root, pretty_print=True, xml_declaration=True)

print(xml_string.decode())
