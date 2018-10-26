infile = open('Bedrijven.txt', 'r')
test = infile.read()
bedrijven = test.split('\n')
print(bedrijven)

bDict = {}
for bedrijf in bedrijven:
    x = bedrijf.split(':')
    bDict[x[0]] = x[1]
    print(x)

print(bDict)