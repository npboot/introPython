def standaardprijs(afstandKM):
    if 0< afstandKM < 50 :
        prijs = afstandKM*0.8
        return prijs
    else :
        if afstandKM > 0 :
            prijs = 15 + afstandKM*0.6
            return  prijs
        else:
            prijs = 0
            return prijs

print(standaardprijs(-100))

