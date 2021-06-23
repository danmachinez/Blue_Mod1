alunos = dict()

nome = input('Digite o nome do aluno: ').title()
media = float(input('Digite a média do aluno: ').replace(',','.'))
alunos[nome] = media

if media > 5 and media < 6.9:
    print('Aluno em recuperação!')
elif media < 5:
    print('Aluno REPROVADO!')
else:
    print('Aluno APROVADO!')
