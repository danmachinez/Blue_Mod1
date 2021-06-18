lista = []
lista_par = []
lista_impar = []

for i in range(10):
    n = int(input('Insira um número na lista: '))
    lista.append(n)
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print('Lista completa: ', sorted(lista))
print('Lista de ímpares: ', sorted(lista_impar))
print('Lista de pares: ', sorted(lista_par))