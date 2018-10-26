import csv

with open('producten.csv', 'a+') as bestand:
    reader = csv.reader(bestand, delimiter=';')