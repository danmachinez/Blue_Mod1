soma = 0

quantidade = int(input('Quantos números gostaria de inserir para a soma?\n'))

for i in range(quantidade):
   soma = soma + int(input('Digite o número: '))
   
print('A soma é:', soma)