senha = 'Blue123'
leitura = ''
erros = 0

while (leitura != senha):
    leitura = input('Digite a senha: ')
    if leitura == senha:
        print('Acesso liberado')
    else:
        erros += 1
        print('Senha incorreta, digite novamente!')

print(f'Você errou a senha {erros} vezes!')