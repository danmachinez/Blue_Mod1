resp = 'S'
listaFinal = list()
listaIdade = list()
listaMulheres = list()
listaIdadesAcimaDaMedia = list()
while resp == 'S':
    dicAtual = {}
    nome = input('Digite seu nome:\n ').title()
    genero = input('Digite seu gênero: [F/M]\n ').upper()
    if genero == 'F':
        listaMulheres.append(nome)
    idade = int(input('Digite sua idade:\n '))
    listaIdade.append(idade)
    dicAtual['Nome'] = nome
    dicAtual['Gênero'] = genero
    dicAtual['Idade'] = idade
    listaFinal.append(dicAtual)
    media = sum(listaIdade) / len(listaIdade)
    if idade > media:
        listaIdadesAcimaDaMedia.append(idade)
    resp = input('Deseja cadastrar mais alguém? [S/N]\n').upper()
    print()
    if resp == 'N':
        break
print('=-' * 30)
print(f'A quantidade de pessoas cadastradas foram {len(listaFinal)}')
print()
print(f'A média de idade dos cadastrados é de {media} anos')
print()
print(listaMulheres)
print()
print(listaIdadesAcimaDaMedia)
print('=-' * 30)
