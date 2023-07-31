class Veiculo:
    def mover(self):
        print("O veículo está se movendo")

def mover_veiculo(veiculo):
    veiculo.mover()

class Veiculo:
    def mover(self):
        print("O veículo está se movendo")

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo")

class Aviao(Veiculo):
    def mover(self):
        print("O avião está voando")

mover_veiculo(Carro())
mover_veiculo(Aviao())