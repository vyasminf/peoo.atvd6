class Forma:
    def __init__(self, tipo, descrição):
        self.tipo = tipo
        self.descrição = descrição

    def dadosDaForma(self):
        return f"Tipo: {self.tipo}\nDescrição: {self.descrição}"

    def calcular_area(self):
        return "Não há dados suficientes para realizar o cálculo."

    def calcular_perimetro(self):
        return "Não há dados suficientes para realizar o cálculo."

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Círculo", "Forma redonda")
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio


class Retangulo(Forma):
    def __init__(self, lado1, lado2):
        super().__init__("Retângulo", "Forma com lados perpendiculares")
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)

circulo = Circulo(5)
retangulo = Retangulo(4, 6)

area_circulo = circulo.calcular_area()
perimetro_circulo = circulo.calcular_perimetro()

area_retangulo = retangulo.calcular_area()
perimetro_retangulo = retangulo.calcular_perimetro()

print("Círculo:")
print(circulo.dadosDaForma())
print("Área:", area_circulo)
print("Perímetro:", perimetro_circulo)

print("\nRetângulo:")
print(retangulo.dadosDaForma())
print("Área:", area_retangulo)
print("Perímetro:", perimetro_retangulo)