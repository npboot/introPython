
while  True:
    woord = input('Geef een string van vier letters: ')
    lengte = len(woord)
    if lengte != 4:
        print(woord + ' heeft ' + str(lengte) + ' letters')
    else:
        print('Inlezen van correcte string: ' + woord + ' is geslaagd')
        break