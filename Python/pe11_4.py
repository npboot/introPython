import csv

with open('producten.csv', 'a+') as bestand:
    writer = csv.writer(bestand, delimiter=';')
    writer.writerow(('Artikelnummer','Artikelcode','Voorraad', 'Prijs'))

    while True:
        artikelnummer = input('Artikelnummer: ')
        artikelcode = input('Artikelcode: ')
        naam = input('Naam: ')
        if naam == 'einde':
            bestand.close()
            break
        voorraad = eval(input('Voorraad: '))
        prijs = eval(input('Prijs: '))
        writer.writerow((artikelnummer,artikelcode,naam,voorraad,prijs))
