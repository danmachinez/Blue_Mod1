homem = mulher_20 = idade_18 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    if idade >= 18:
        idade_18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar com o cadastro? [S/N] ')) .upper().strip()[0]
    if resposta == 'N':
        break
print()  
    
print(f'No total {idade_18} pessoas tem mais de 18 anos!')
print(f'No total foram cadastrados {homem} homens!')
print(f'No total foram cadastradas {mulher_20} mulheres com menos de 20 anos!')

print()

print('Fim')