
def kwadraten_som(grondgetallen):
    totaal = 0
    for getal in grondgetallen:

        if getal >= 0:
            totaal = totaal + getal
    return totaal

print(kwadraten_som([ 4, 5, 3, -81 ]))