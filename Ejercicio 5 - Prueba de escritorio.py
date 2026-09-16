# Prueba de escritorio

class PruebaEscritorio:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def calcular(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y
        return self.suma

    def mostrar_resultado(self):
        print("EL VALOR DE LA SUMA ES:", self.suma)


# Programa principal
prueba = PruebaEscritorio()
prueba.calcular()
prueba.mostrar_resultado()
