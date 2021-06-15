vogais = 0

frase = input('Digite uma frase:\n').upper()

for i in frase:
    if i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U':
        vogais += 1
print()
print(f'Sua frase tem {vogais} vogais!')
