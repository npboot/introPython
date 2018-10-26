def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    aantal= 12 - len(infile.readlines())
    infile.close()
    print('Aantal vrije kluizen: ' + str(aantal))

def nieuwe_kluis():
    kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    infile = open('kluizen.txt', 'r+')
    kluizen = infile.readlines()
    for kluis in kluizen:
        x = kluis.split(';')
        if x[0] in kluisnummers:
            kluisnummers.remove(x[0])
    if len(kluisnummers) != 0:
        code = input('Geef een code: ')
        infile.write('\n' + kluisnummers[0] + ';' + code)
        print('Kluisnummer is: ' + kluisnummers[0])
    else:
        print('Alle kluizen zijn bezet')
    infile.close()

def kluis_openen():
    infile = open('kluizen.txt', 'r')
    kluizen = infile.readlines()
    kluisnummer = input('Geef je kluisnummer: ')
    code = input('Geef je code: ')
    combinatie = False
    for kluis in kluizen:
        if kluisnummer and code in kluis:
            combinatie = True

    if combinatie == True:
        print('De ingevoerde combinatie is juist')
    else:
        print('De ingevoerde combinatie is incorrect')


invoer = 0
while invoer != 5:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn', '2: Ik wil een nieuwe kluis',
          '3: Ik wil even iets uit mijn kluis halen', '4: Ik geef mijn kluis terug', sep='\n')
    invoer = input('voernummer in: ')
    if invoer == '1':
        toon_aantal_kluizen_vrij()
    if invoer == '2':
        nieuwe_kluis()
    if invoer == '3':
        kluis_openen()