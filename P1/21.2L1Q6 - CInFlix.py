category = input() 
genre = input()

#category == filme
if category == 'Filme':
    if genre == 'Acao':
        selected = 'Kill Bill Vol. I'
    elif genre == 'Terror':
        selected = 'It - A Coisa'
    elif genre == 'Drama':
        selected = 'Sempre ao Seu Lado'
    elif genre == 'Romance':
        selected = 'Me Chame Pelo Seu Nome'
    elif genre == 'Aventura':
        selected = 'Homem - Aranha: Sem Volta para Casa'
    elif genre == 'Animacao':
        selected = 'Encanto'
    elif genre == 'Comedia':
        selected = 'Nao Olhe Para Cima'
    elif genre == 'Fantasia':
        selected = 'Harry Potter e a Pedra Filosofal'
    elif genre == 'Suspense':
        selected = 'Corra!'
    elif genre == 'Policial':
        selected = 'Cidade de Deus'
    elif genre == 'Ficcao':
        selected = 'Interestelar'  
#caregory == serie
if category == 'Serie':
    if genre == 'Acao':
        selected = 'The Boys'
    elif genre == 'Terror':
        selected = 'A Maldicao da Residencia Hill'
    elif genre == 'Drama':
        selected = 'Euphoria'
    elif genre == 'Romance':
        selected = 'Bridgerton'
    elif genre == 'Aventura':
        selected = 'The Witcher'
    elif genre == 'Animacao':
        selected = 'Arcane'
    elif genre == 'Comedia':
        selected = 'FRIENDS'
    elif genre == 'Fantasia':
        selected = 'Game Of Thrones'
    elif genre == 'Suspense':
        selected = 'Prison Break'
    elif genre == 'Policial':
        selected = 'Peaky Blinders'
    elif genre == 'Ficcao':
        selected = 'Dark'

if category == 'Filme':
    print(f'{selected} e o filme mais popular do genero {genre} no momento.')
elif category == 'Serie':
    print(f'{selected} e a serie mais popular do genero {genre} no momento.')