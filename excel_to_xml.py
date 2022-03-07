import openpyxl as px
import lxml.etree as et

root = et.Element('presidents')

wb = px.load_workbook('DATA/presidents.xlsx')

ws = wb['US Presidents']

headers = next(ws.values)
print(headers)

for row in ws.values:
    president = et.SubElement(root, 'president', term=str(row[0]))
    et.SubElement(president, 'last_name').text = row[1]
    et.SubElement(president, 'first_name').text = row[2]
    et.SubElement(president, 'birth_date').text = str(row[3])
    et.SubElement(president, 'death_date').text = str(row[4])

xml_doc = et.tostring(root, pretty_print=True, xml_declaration=True)

print(xml_doc.decode())

doc = et.ElementTree(root)

doc.write('presidents_example.xml', pretty_print=True, xml_declaration=True)
