import csv

with open('gamescores.csv', 'r') as bestand:
    reader = csv.reader(bestand, delimiter=';')
    hoogste_score = 0
    for row in reader:
        if int(row[2]) > hoogste_score:
            naam = row[0]
            datum = row[1]
            hoogste_score = int(row[2])

print('De hoogste scor is: ' + str(hoogste_score) + ' op '+ datum + ' behaald door ' + naam)
