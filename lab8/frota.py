from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta
from typing import List


class Frota:
    def __init__(self):
        self.__veiculos: List[Veiculo] = []

    def adicionar_veiculo(self, veiculo: Veiculo):
        self.__veiculos.append(veiculo)

    def remover_veiculo(self, veiculo: Veiculo):
        if veiculo in self.__veiculos:
            self.__veiculos.remove(veiculo)

    def pesquisar_veiculo(self, modelo: str):
        for veiculo in self.__veiculos:
            if veiculo.get_modelo().lower() == modelo.lower():
                return veiculo
        return None


    def imprimir_frota(self):
        if not self.__veiculos:
            print("A frota está vazia.")
        else:
            for tipo in (Carro, Moto, Bicicleta):
                for veiculo in self.__veiculos:
                    if isinstance(veiculo, tipo):
                        veiculo.imprime()
                        print("-")

