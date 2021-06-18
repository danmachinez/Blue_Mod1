from random import randint
lista_final = []

nJogos = int(input('Quantos jogos gostaria de tentar? '))

for i in range(nJogos):
    lista_vez = []
    cont = 0
    while cont < 6:
        sorteio = randint(1, 60)
        if sorteio not in lista_vez:
            lista_vez.append(sorteio)
            cont += 1
    lista_final.append(sorted(lista_vez))
print(lista_final)    