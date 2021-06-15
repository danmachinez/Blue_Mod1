# n1 = valor de 1
# n2 = valor de 5
# n3 = valor de 10
# n4 = valor de 50
# n5 = valor de 100

quantidade_n1 = 0
quantidade_n2 = 0
quantidade_n3 = 0
quantidade_n4 = 0
quantidade_n5 = 0

valor_n1 = 1
valor_n2 = 5
valor_n3 = 10
valor_n4 = 50
valor_n5 = 100

Valor_minimo = 10
Valor_maximo = 600


quantidade_Sacar  = float(input(f'Qual a quantidade que vc gostaria de sacar? (Valores entre R$ {Valor_minimo} - R$ {Valor_maximo}) '))

while quantidade_Sacar < Valor_minimo or quantidade_Sacar > Valor_maximo:
    quantidade_Sacar = float(input(f'A quantidade informada não é permitida. Favor informar um valor entre R$ {Valor_minimo} e R$ {Valor_maximo}: '))

quantidade_Auxiliar = quantidade_Sacar

quantidade_n5 = int(quantidade_Auxiliar//100)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n5 * 100)

quantidade_n4 = int(quantidade_Auxiliar//50)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n4 * 50)

quantidade_n3 = int(quantidade_Auxiliar//10)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n3 * 10)

quantidade_n2 = int(quantidade_Auxiliar//5)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n2 * 5)

quantidade_n1 = int(quantidade_Auxiliar//1)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n1 * 1)

print(f'Para sacar a quantia de {quantidade_Sacar} reais, você precisa de: ')

if quantidade_n5 > 0:
    print(f'{quantidade_n5} nota(s) de {valor_n5}')
if quantidade_n4 > 0:
    print(f'{quantidade_n4} nota(s) de {valor_n4}')
if quantidade_n3 > 0:
    print(f'{quantidade_n3} nota(s) de {valor_n3}')
if quantidade_n2 > 0:
    print(f'{quantidade_n2} nota(s) de {valor_n2}')
if quantidade_n1 > 0:
    print(f'{quantidade_n1} nota(s) de {valor_n1}')