import xmltodict


with open('artikelen.xml') as XMLartikel:
    artikelendict = xmltodict.parse(XMLartikel.read())

artikelen = artikelendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])



