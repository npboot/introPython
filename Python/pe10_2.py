def monopolyworp():
    import random
    i = 0
    while i is not 3:
        worp1 = random.randrange(1, 7)
        worp2 = random.randrange(1, 7)
        som = worp1 + worp2
        if worp1 == worp2:
            print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(som) + '(dubbel)')
            i += 1
        else:
            print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(som))
            break

