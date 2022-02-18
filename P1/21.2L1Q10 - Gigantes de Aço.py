#Boxer_1
name1 = input()
life1 = int(input())
attack1 = int(input())
defense1 = int(input())

#Boxer_2
name2 = input()
life2 = int(input())
attack2 = int(input())
defense2 = int(input())

attacker = input()
defender = input()

#Round 1
print('Round 1')
if attacker == 'jab':
    if defender == 'bloqueio':
        damage = attack1 - (attack1 * defense2/100)
    elif defender == 'esquiva':
        attack2 += (attack2/100)*10
        damage = 0
    elif defender == 'X':
        damage = attack1
    life2 -= damage
elif attacker == 'direto':
    if defender == 'bloqueio':
        damage = attack1 * 1.3 - (attack1 * defense2/100)
    elif defender == 'esquiva':
        attack2 += (attack2/100)*20
        damage = 0
    elif defender == 'X':
        damage = attack1 * 1.4
    life2 -= damage
if life2 <= 0:
    print(f'NOSSO CAMPEAO E {name1.upper()} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
else:
#Round 2
    attacker = input()
    defender = input()
    print('Round 2')
    if attacker == 'jab':
        if defender == 'bloqueio':
            damage = attack2 - (attack2 * defense1/100)
        elif defender == 'esquiva':
            attack1 += (attack1*100)*10
            damage = 0
        elif defender == 'X':
            damage = attack2
        life1 -= damage
    elif attacker == 'direto':   
        if defender == 'bloqueio':
            damage = attack2 * 1.3 - (attack2 * defense1/100)
        elif defender == 'esquiva':
            attack1 += (attack1/100)*20
            damage = 0
        elif defender == 'X':
            damage = attack2 * 1.4
        life1 -= damage
    if life1 <= 0:
        print(f'NOSSO CAMPEAO E {name2.upper()}')
    else:
#Round 3
        attacker = input()
        defender = input()
        print('Round 3')
        print(f'{name1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO')
        if attacker == 'jab':
            if defender == 'bloqueio':
                damage = attack1 - (attack1 * defense2/100)
            elif defender == 'esquiva':
                attack2 += (attack2/100)*10
                damage = 0
            elif defender == 'X':
                damage = attack1
            life2 -= damage
        elif attacker == 'direto':
            if defender == 'bloqueio':
                damage = attack1 * 1.3 - (attack1 * defense2/100)
            elif defender == 'esquiva':
                attack2 += (attack2/100)*20
                damage = 0
            elif defender == 'X':
                damage = attack1 * 1.4
            life2 -= damage
        if life2 > 0:
            print(f'NOSSO CAMPEAO E {name2.upper()}')
        else:
            print(f'NOSSO CAMPEAO E {name1.upper()}')