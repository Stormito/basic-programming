weapon = int(input())
if weapon == 1:
    name = 'Cassetete'
elif weapon == 2:
    name = 'Garrafa de Whisky'
elif weapon == 3:
    name = 'Soco Ingles'
elif weapon == 4:
    name = 'Lamina Escondida'
elif weapon == 5:
    name = 'Pe de Cabra'
elif weapon == 6:
    name = 'Canivete'

if weapon < 1 or weapon > 6:
    print('Numero invalido')
else:
    if weapon%2==0:
        category = 'cortante'
    else:
        category = 'atordoante'

    print(f'A arma corpo a corpo escolhida foi: {name}')
    print(f'A arma corpo a corpo escolhida e {category}')