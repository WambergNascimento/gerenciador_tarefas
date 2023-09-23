import random

numero = random.randint(1,1000)
jogada = 0

while jogada != numero:
    jogada = int(input('Adivinhe o número: '))

    if jogada == numero:
        print('Parabens! Voce acertou!')
    else:
        if jogada < numero:
            print('O número é maior.')
        else:
            print('O número é menor.')