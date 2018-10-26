stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(lijst):
    x = False
    while x == False:
        invoer = input('Wat is je beginstation?\n')
        x = invoer in stations
    return invoer

def inlezen_eindstation(stations, beginstation):

    while True:
        invoer = input('Wat is je eindstation?\n')
        verschil = stations.index(invoer) - stations.index(beginstation)
        if invoer in stations and verschil > 0:
            return invoer
        else:
            continue

def omroepen_reis(stations, beginstation, eindstation):
    verschil = stations.index(eindstation) - stations.index(beginstation)
    ritprijs = verschil*5
    nummerbegin = stations.index(beginstation) + 1
    nummereind = stations.index(eindstation) +1
    tussen = stations[nummerbegin:stations.index(eindstation)]
    print('Het beginstation '+ beginstation + ' is het ' + str(nummerbegin) + 'e station in het traject.')
    print('Het eindstation ' + eindstation + ' is het ' + str(nummereind) + 'e station in het traject.')
    print('De afstand bedraagt ' + str(verschil) + ' station(s)')
    print('De prijs van een het kaartje is ' + str(ritprijs) + ' euro')
    print('\nJij stapt in de trein in: ' + beginstation)
    for station in tussen:
        print('- ' + station)
    print("Jij stapt uit in: " + eindstation)


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)