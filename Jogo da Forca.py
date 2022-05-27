import random

print('*' * 73)
print('Bem-Vindo ao jogo da forca! Adivinhe o nome de algum animal de estimação.')
print('*' * 73)
print('Você terá 6 créditos para jogar, e tentar acertar a palavra.')
print('*' * 73)
boneco = (
    '''
    +====+
    |    |     |
    |          |
    |          |
    |          |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |          |
    |          |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |    |     |
    |          |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |   /|     |
    |          |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |   /|\    |
    |          |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |   /|\    |
    |   /      |
    |
    |
    ============''',
    '''
    +====+
    |    |     |
    |    0     |
    |   /|\    |
    |   / \    |
    |
    |
    ============''',)

print("*" * 24)
print(boneco[0])
print("*" * 24)
animais = 'CAVALO', 'OVELHA', 'CACHORRO', 'PATO', 'GALINHA', 'GATO', 'PORCO', 'HAMSTER', 'RATO', 'PAPAGAIO'
vocabulario = random.choice(animais)
status = '_ ' * len(vocabulario)
print(f'Palavra: {status}')

lista = []
credito = 6
dd = 0

while credito <= 6:
    print("*" * 24)
    letra = str(input('Digite uma letra: ')).upper()
    print("*" * 24)
    if vocabulario == letra:
        print('Você venceu o jogo com chute parabéns!')
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    lista.append(letra)

    variavel = ''
    for letrr in vocabulario:
        if letrr in lista:
            variavel = variavel + letrr

        else:
            variavel = variavel + '_ '

    if letra not in vocabulario:
        credito = credito - 1
        while dd <= 6:

            dd = dd + 1
            if dd == 1:
                print(boneco[1])
            elif dd == 2:
                print(boneco[2])
            elif dd == 3:
                print(boneco[3])
            elif dd == 4:
                print(boneco[4])
            elif dd == 5:
                print(boneco[5])
            else:
                print(boneco[6])
            break
        print(f'ERRADO!')
        print(f'Você ainda tem {credito} créditos.')

    if variavel == vocabulario:
        print(vocabulario)
        print('Venceu o jogo, seu vocabulário está afiado.')
        break
    else:
        print(f'Estado: {variavel}')

    if credito == 0:
        print('Morreu filho (_メ)')
        print(f'A palavra era: {vocabulario}')
        break
