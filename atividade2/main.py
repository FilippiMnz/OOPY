class Estudante:
    def __init__(self, nome, matricula, creditos):
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_creditos(self):
        return self.__creditos

    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_creditos(self, creditos):
        self.__creditos = creditos

    def adicionar_creditos(self, quantidade):
        if quantidade > 0:
            self.__creditos += quantidade
        else:
            print("A quantidade de créditos a adicionar deve ser positiva.")

def main():
    estudante = Estudante("João da Silva", "20250101", 30)

    print("Nome:", estudante.get_nome())
    print("Matrícula:", estudante.get_matricula())
    print("Créditos:", estudante.get_creditos())

    estudante.set_nome("Maria Oliveira")
    estudante.set_matricula("20250202")
    estudante.set_creditos(40)

    print("\nApós modificações:")
    print("Nome:", estudante.get_nome())
    print("Matrícula:", estudante.get_matricula())
    print("Créditos:", estudante.get_creditos())

    estudante.adicionar_creditos(10)
    print("\nApós adicionar 10 créditos:")
    print("Créditos:", estudante.get_creditos())

    estudante.adicionar_creditos(-5)

if __name__ == "__main__":
    main()
