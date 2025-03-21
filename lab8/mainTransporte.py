from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta


def main():
    veiculo = Veiculo("Modelo Genérico", "Fabricante Genérico", 4, "Veículo genérico")
    veiculo.imprime()
    print("-")

    carro = Carro("Gol", "Volkswagen", 4, "Carro popular", 4)
    carro.imprime()
    print("-")

    moto = Moto("Ninja", "Kawasaki", 2, "Moto esportiva", 600)
    moto.imprime()
    print("-")

    bicicleta = Bicicleta("Mountain Bike", "Caloi", 2, "Bicicleta de trilha", 18)
    bicicleta.imprime()
    print("-")


if __name__ == "__main__":
    main()
