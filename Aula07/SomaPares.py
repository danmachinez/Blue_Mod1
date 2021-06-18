pares = 0
impares = 0
listaPares = []
for i in range(6):
    n = int(input('Digite um número inteiro qualquer: '))
    if n % 2 == 0:
        pares += 1
        listaPares.append(n)
    else:
        impares += 1
print()
print('-' * 32)
print(f'A soma dos números pares é {sum(listaPares)}!')
print('-' * 32)
print(f'Foram digitados {pares} números pares!')
print('-' * 32)