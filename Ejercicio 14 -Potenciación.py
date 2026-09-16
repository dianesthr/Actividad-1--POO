# Ejercicio resuelto

class CalculadoraPotencias:

    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return self.numero ** 2

    def calcular_cubo(self):
        return self.numero ** 3


# Programa principal
numero = float(input("Ingrese un número: "))

calculadora = CalculadoraPotencias(numero)

print("El cuadrado de", numero, "es:", calculadora.calcular_cuadrado())
print("El cubo de", numero, "es:", calculadora.calcular_cubo())
