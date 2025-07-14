class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def chamar_nome(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input("digite o nome: ")
idade = int(input("digite a idade: "))

p = Pessoa(nome, idade) 

print(p.chamar_nome())