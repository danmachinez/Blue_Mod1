maioridade = 18
nMaiores = 0
nMenores = 0

for i in range(7):
    idade = int(input('Digite sua idade: '))
    if idade < maioridade:
        nMenores += 1
    else:
        nMaiores += 1
print(f'No total {nMaiores} atingiram a maioridade e {nMenores} ainda não!')
