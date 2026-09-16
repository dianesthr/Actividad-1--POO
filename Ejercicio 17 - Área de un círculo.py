# Ejercicio 17 - Área y longitud de un círculo

import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_longitud(self):
        return 2 * math.pi * self.radio


# Programa principal
radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)

print("El área del círculo es:", circulo.calcular_area())
print("La longitud de la circunferencia es:", circulo.calcular_longitud())
