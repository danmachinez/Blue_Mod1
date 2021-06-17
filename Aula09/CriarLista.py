###tentativa

# n1 = n2 = n3 = n4 = n5 = 0
# Lista_numerica = []

# n1 = int(input('Digite um valor a ser adicionado a lista: '))
# Lista_numerica.append(n1)
# n2 = int(input('Digite um valor a ser adicionado a lista: '))
# Lista_numerica.append(n2)
# n3 = int(input('Digite um valor a ser adicionado a lista: '))
# Lista_numerica.append(n3)
# n4 = int(input('Digite um valor a ser adicionado a lista: '))
# Lista_numerica.append(n4)
# n5 = int(input('Digite um valor a ser adicionado a lista: '))
# Lista_numerica.append(n5)
# Lista_numerica.sort()
# print(Lista_numerica)

###corrigido

lista = []
resp = 's'
while resp == 's':
    n1 = int(input('Insira um número: '))
    if n1 not in lista:
        lista.append(n1)
    else:
        print('Esse número ja existe na lista!')
    resp = input('Deseja continuar? [s/n] ').lower()
    while resp not in ['s', 'n']:
        resp = input('Resposta inválida! Deseja continuar? [s/n]').lower()
print(sorted(lista))