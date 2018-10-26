def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    aantalkluizen = len(infile)
    return aantalkluizen



invoer = 0
while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn', '2: Ik wil een nieuwe kluis',
          '3: Ik wil even iets uit mijn kluis halen', '4: Ik geef mijn kluis terug', sep='\n')
    invoer = eval(input('voernummer in: '))

    if invoer == 1:
        aantal = toon_aantal_kluizen_vrij()
        print(aantal)
    if invoer == 5:
        False









