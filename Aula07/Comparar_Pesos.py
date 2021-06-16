maior = 0
menor = 11110

for p in range(5):
    peso = float(input('Qual o peso? '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print()
print(f'O maior peso foi {maior}kg\nE o menor peso foi {menor}kg.')