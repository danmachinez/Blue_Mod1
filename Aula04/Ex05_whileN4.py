from random import randint
from time import sleep
n = randint(0, 10)
print('Olá... Sou sua máquina, não se assuste, vamos jogar um jogo.')
sleep(3)
print('Séra que você consegue adivinhar em que número estou pensando?')
sleep(3)
print()

a = 0
certo = False
while not certo: 
    jogador = int(input('Qual número a máquina pensou: '))
    a += 1
    if jogador == n:
        certo = True

print()

print(f'Você acertou depois de tentar {a} vezes, parabéns pela insistência!')
