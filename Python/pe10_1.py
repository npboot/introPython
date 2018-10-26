bruin = {'Boxtel', 'Best', 'Beukenlaan','Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan','Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

gelijk = bruin & groen
print(gelijk)

verschil = bruin - groen
print(verschil)

allemaal = bruin | groen
print(allemaal)