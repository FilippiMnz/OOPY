from veiculo import *
class Carro(Veiculo):
    def __init__(self, modelo: str, fabricante: str, numero_rodas: int, descricao: str, numero_portas: int):
        super().__init__(modelo, fabricante, numero_rodas, descricao)
        self.__numero_portas = numero_portas

    def get_numero_portas(self):
        return self.__numero_portas

    def set_numero_portas(self, numero_portas):
        self.__numero_portas = numero_portas

    def imprime(self):
        super().imprime()
        print(f"Número de Portas: {self.__numero_portas}")
