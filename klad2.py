kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

kluizen = ['11;6754\n', '1;geheim\n', '5;kluisvanpietje\n', '12;z@terd@g']

print(kluizen)
for kluis in kluizen:
    x = kluis.split(';')
    if x[0] in kluisnummers:
        kluisnummers.remove(x[0])

print(kluisnummers)