

try:
    aantal = eval(input('Hoeveel personen gaan er mee op reis: '))
    bedrag = 4356/int(aantal)
    print('Het bedrag per persoon is: ' + str(bedrag))
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except TypeError:
    print('Negatieve getallen zijn niet toegestaan!')
except NameError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')

