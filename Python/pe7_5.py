

def gemiddelde():
    userInput = input('Geef een zin: ')

    woordlengte = (len(userInput) - userInput.count(' ') )/ len(userInput.split())
    print(woordlengte)
    return woordlengte

gemiddelde()

