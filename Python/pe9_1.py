i = 0
totaal = 0
getal = 1
while getal != 0 :
    getal = int(input('Geef een getal:' ))
    i += 1
    totaal += getal
print('Er zijn ' + str(i) + ' getallen ingevoerd, de som is: ' + str(totaal))