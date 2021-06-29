class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def dados(self):
        print(f'Nome completo: {self.nome} {self.sobrenome}\nIdade: {self.idade}anos')
    
gustavo = Pessoa('Gustavo', 'Batata', '27')  
gustavo.dados()   