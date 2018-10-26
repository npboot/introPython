invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoerlijst = [int(s) for s in invoer.split('-')]

print('Gesorteerde list van ints: ' + str(invoerlijst))
print('Grootste getal: ' + str(max(invoerlijst)) + ' en Kleinste getal: ' + str(min(invoerlijst)))
print('Aantal getallen: '  + str(len(invoerlijst)) + ' en Som van de getallen: ' + str(sum(invoerlijst)))
print('Gemiddelde: ' + str(sum(invoerlijst)/len(invoerlijst) ))