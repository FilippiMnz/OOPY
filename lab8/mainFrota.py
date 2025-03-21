from frota import Frota
from moto import Moto
from carro import Carro
from bicicleta import Bicicleta
def main():
    frota = Frota()

    carro = Carro("Fusca", "Volkswagen", 4, "Carro clássico", 2)
    moto = Moto("CB500", "Honda", 2, "Moto esportiva", 500)
    bicicleta = Bicicleta("Caloi", "Caloi", 2, "Bicicleta de montanha", 21)

    frota.adicionar_veiculo(carro)
    frota.adicionar_veiculo(moto)
    frota.adicionar_veiculo(bicicleta)

    print("=== Frota Completa ===")
    frota.imprimir_frota()

    print("=== Pesquisa por modelo: CB500 ===")
    encontrado = frota.pesquisar_veiculo("CB500")
    if encontrado:
        encontrado.imprime()
    else:
        print("Veículo não encontrado.")

    frota.remover_veiculo(moto)
    print("=== Frota Após Remoção da Moto ===")
    frota.imprimir_frota()


if __name__ == "__main__":
    main()
