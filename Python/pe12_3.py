import xmltodict


with open('pe12_3.xml') as XMLstations:
    stationsdict = xmltodict.parse(XMLstations.read())

stations = stationsdict['Stations']['Station']

def synoniemen():
    print('Dit zijn alle stations met één of meer synoniemen:')
    for station in stations:
        if station['Synoniemen'] is not None:
            print('{:4} - {}'.format(station['Code'], station['Synoniemen']))
    print('')


def types():
    print('Dit zijn de codes en types van de 4 stations:')
    for station in stations:
        print('{:4} - {}'.format(station['Code'],station['Type']))
    print('')

def langenaam():
    print('Dit is de lange naam van elk station:')
    for station in stations:
        print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))
    print('')

types()
synoniemen()
langenaam()