class Veiculo:
    def __init__(self, modelo: str, fabricante: str, numero_rodas: int, descricao: str):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__numero_rodas = numero_rodas
        self.__descricao = descricao

    
    def get_modelo(self):
        return self.__modelo

    def get_fabricante(self):
        return self.__fabricante

    def get_numero_rodas(self):
        return self.__numero_rodas

    def get_descricao(self):
        return self.__descricao

    
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def set_numero_rodas(self, numero_rodas):
        self.__numero_rodas = numero_rodas

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def imprime(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Fabricante: {self.__fabricante}")
        print(f"Número de Rodas: {self.__numero_rodas}")
        print(f"Descrição: {self.__descricao}")



