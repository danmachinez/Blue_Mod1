valorProdutos = []
nomeProdutos = []
produtosCaros = 0
resp = 's'

while resp == 's':
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o preço desse produto: R$'))
    if produto not in nomeProdutos and valor not in valorProdutos:
        nomeProdutos.append(produto)
        valorProdutos.append(valor)
        if valor >= 1000:
            produtosCaros += 1
        resp = input('Deseja continuar cadastrando? [s/n]').lower()
    else:
        print('Produto ja cadastrado!')
        resp = input('Deseja continuar cadastrando? [s/n]').lower()
    while resp not in 'sn':
        resp = input('Resposta inválida! Deseja continuar? [s/n] ').lower()  
print()
soma = sum(valorProdutos)
print(f'O valor total de sua compra foi de R${soma}')
print(f'No total, {produtosCaros} custam mais de R$ 1000')
#ficou faltando o ultimo print 'mostrar o nome do produto mais barato        