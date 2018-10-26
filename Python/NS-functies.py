
def standaardprijs(afstandKM) :
    if afstandKM > 50:
        prijs = 15 + 0.6*afstandKM
    prijs = afstandKM*0.8
    return prijs



def ritprijs(leeftijd, weekendrit, afstandKM):
    std = standaardprijs(afstandKM)
    if 12<leeftijd<65:
        if weekendrit == True:
            prijs = std*(0.6)
        else:
            prijs = std
    else:
        if weekendrit == True:
            prijs = std*(0.65)
        else:
            prijs = std*(0.7)
    return prijs






print(ritprijs(41,True,45))
print(ritprijs(41,False,45))
print(standaardprijs(45))