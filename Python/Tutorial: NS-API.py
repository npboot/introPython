import requests
import xmltodict

station = input('Welk station: ')
auth_details = ('niels.boot@student.hu.nl', 'gIbh4pov7EJogdCx2XZwlvUczv0bvqnPUpvAuVvv0eXoipu6B0hH9g')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station

response = requests.get(api_url, auth=auth_details)
print(response.text)

with open('vertrektijden.xml', 'w') as myXMLFile:
    myXMLFile.write(response.text)

vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36

    print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)