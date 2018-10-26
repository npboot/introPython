inputlist = eval(input("Geef lijst met minimaal 10 strings: "))
vierletterlijst = []
for word in inputlist:
    if len(word ) == 4:
        vierletterlijst.append(word)
print(vierletterlijst)