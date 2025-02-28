from item import Item

class DVD(Item):
    def __init__(self, titulo, tempo_reproducao, diretor, possuo, comentario):
        super().__init__(titulo, tempo_reproducao, possuo, comentario)
        self.__diretor = diretor

   
    def get_diretor(self):
        return self.__diretor
    
    def set_diretor(self, diretor):
        self.__diretor = diretor
    
    def imprime(self):
        print(f"DVD - {super().imprime()} | Diretor: {self.__diretor}")