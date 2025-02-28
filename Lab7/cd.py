from item import Item

class CD(Item):
    def __init__(self, titulo, tempo_reproducao, artista, num_trilhas, possuo, comentario):
        super().__init__(titulo, tempo_reproducao, possuo, comentario)
        self.__artista = artista
        self.__num_trilhas = num_trilhas

    def get_artista(self):
        return self.__artista
    
    def get_num_trilhas(self):
        return self.__num_trilhas
    
    def set_artista(self, artista):
        self.__artista = artista
    
    def set_num_trilhas(self, num_trilhas):
        self.__num_trilhas = num_trilhas
    
    def imprime(self):
        print(f"CD - {super().imprime()} | Artista: {self.__artista} | Trilhas: {self.__num_trilhas}")
