resultaten ={'Sam':6.3, 'Geert':8.0, 'Anne': 9.1, 'Ali':8.2, 'Rachel':5.2, 'Joost':6.0, 'Sjonnie':9.2, 'Anita':7.3}
studenten = resultaten.keys()

for student in studenten:
    resulataat = resultaten[student]
    if resulataat >= 9.0:
        print(student + ' : ' + str(resultaten[student]))