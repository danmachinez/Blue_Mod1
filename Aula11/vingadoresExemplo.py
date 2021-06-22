elencoVingadores = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlett Johansson':'Viúva Negra'}

elencoVingadores ['Miltin MilGrau'] = 'SemBraço'

print('Chris Evans' in elencoVingadores.keys())
print()
print('Chris Evans' in elencoVingadores.values())

print(elencoVingadores)
print()
print(sorted(elencoVingadores.keys()))
print()
print(sorted(elencoVingadores.values()))
print()

nome = (input('Digite o nome do ator: '))
personagem = (input('Digite o nome do personagem: '))

elencoVingadores [nome] = personagem
print()
print(elencoVingadores)
print()

del elencoVingadores['Mark Ruffalo']
print(elencoVingadores)