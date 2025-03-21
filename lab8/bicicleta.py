from veiculo import *
class Bicicleta(Veiculo):
    def __init__(self, modelo: str, fabricante: str, numero_rodas: int, descricao: str, numero_marchas: int):
        super().__init__(modelo, fabricante, numero_rodas, descricao)
        self.__numero_marchas = numero_marchas

    def get_numero_marchas(self):
        return self.__numero_marchas

    def set_numero_marchas(self, numero_marchas):
        self.__numero_marchas = numero_marchas

    def imprime(self):
        super().imprime()
        print(f"Número de Marchas: {self.__numero_marchas}")

