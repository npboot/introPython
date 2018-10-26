import datetime
vandaag = datetime.datetime.today()

import csv

with open('inloggers.csv', 'a') as bestand:
    writer = csv.writer(bestand, delimiter=';')

    while True:
        tijd = vandaag.strftime("%a %d %b %Y at %H:%I")
        naam = input("Wat is je achternaam? ")
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        if naam == 'einde':
            break

        writer.writerow((tijd, naam, voorl, gbdatum, email))


#gebruik hier een herhalingslus:

#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file