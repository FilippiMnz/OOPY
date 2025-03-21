from veiculo import *
class Moto(Veiculo):
    def __init__(self, modelo: str, fabricante: str, numero_rodas: int, descricao: str, cilindrada: int):
        super().__init__(modelo, fabricante, numero_rodas, descricao)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def imprime(self):
        super().imprime()
        print(f"Cilindrada: {self.__cilindrada} cc")
