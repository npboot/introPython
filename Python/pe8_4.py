studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    ant = []
    for student in studentencijfers:
        gem = int(sum(student)) / len(student)
        ant.append(gem)
    return ant

def gemiddelde_van_alle_studenten(studentencijfers):
     ant = sum(gemiddelde_per_student(studentencijfers)) / len(studentencijfers)
     return ant


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))

