from datetime import date

dados = {}

nome = input("Digite o nome do funcionário:\n").title()
anoNascimento = int(input('Digite o ano de nascimento:\n'))
numCarteira = int(input('Digite o código da carteira de trabalho:\n'))
dados[nome] = [anoNascimento,numCarteira]
if numCarteira != 0:
    anoContratacao = int(input('Digite o ano da contratação:\n'))
    salario = input('Digite o salario:R$ \n')
    dados[nome]=[anoNascimento, numCarteira, anoContratacao, salario]
    idadeAposentadoria = anoContratacao + 35 - anoNascimento
    print(f'Todas as infos do funcionário: {dados}')
    print()
    idade = date.today().year - anoNascimento
    print(f'A idade do funcionário é de {idade} anos e ele irá se aposentar com {idadeAposentadoria} anos')
    print()