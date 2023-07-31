class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo

# Criando classe Funcionario
funcionario1 = Funcionario("vitoria","gerente")

# Imprimindo os atributos da instância
print("Nome:", funcionario1.nome)
print("Cargo:", funcionario1.cargo)