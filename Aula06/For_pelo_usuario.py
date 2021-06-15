inicio = fim = passo = 0

inicio = int(input('Digite um numero inteiro pro inicio: '))
fim = int(input('Digite um numero inteiro pro fim: '))
passo = int(input('Digite um numero inteiro para o passo:  '))

for i in range(inicio, fim, passo):
    print(i)
