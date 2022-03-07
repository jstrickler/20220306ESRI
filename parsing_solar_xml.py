import lxml.etree as et

doc = et.parse('DATA/solar.xml')

print(doc)

root = doc.getroot()

print(root, root.tag)

for element in root:
    if "planets" in element.tag:
        # print(element.tag)
        for planet in element.findall('planet'):
            print(planet.get('planetname'))
            for moon in planet.findall('moon'):
                print(f"    {moon.text}")




