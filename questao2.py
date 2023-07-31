class Animal:
    def emitir_som(self):
        print("Som do animal")

def emitir_som(animal):
    animal.emitir_som()

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

emitir_som(Animal())
emitir_som(Cachorro())
emitir_som(Gato())