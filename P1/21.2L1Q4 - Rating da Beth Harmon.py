from unittest import result


r2 = int(input()) #rating Beth
r1 = int(input()) #rating adversary
result = input()
P0 = 0

if result == 'vitoria':
    P0 = 1
elif result == 'empate':
    P0 = 0.5
elif result == 'derrota':
    P0 = 0

#calculations
E = 1/(1+10**((r1-r2)/400))
R = r2 + 40 * (P0 - E)

if result == 'vitoria' or result == 'empate' or result == 'derrota':
    print(f'O novo rating da Beth Harmon é {int(R)}')
else:
    print('Resultado da partida invalido') 