from random import randint
from time import sleep

print('Olá! Pronto pra mais um jogo de adivinha?')
sleep(1)
print('Dessa vez vou te ajudar até você acertar, vamos lá!')

numComputador = randint(1, 10)
total_Palpites = 1
palpite = 0

while palpite != numComputador:
    palpite = int(input('Diga um número entre 0 e 10: '))
    while palpite not in range(1, 10):
        palpite = int(input('Valor incorreto! Diga um número entre 0 e 10: '))
    if palpite > numComputador:
        palpite = int(input('Hmm... passou direto, mais pra baixo: '))
        total_Palpites += 1
    if palpite < numComputador:
        palpite = int(input('Hmm... muito pouco, mais pra cima: '))
        total_Palpites +=1
    if palpite == numComputador:
        print(f'Parabéns! Você acertou depois de tentar {total_Palpites} vezes!')
    