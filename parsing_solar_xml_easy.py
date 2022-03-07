import lxml.etree as et

doc = et.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")




