class CD:
    def __init__(self, titulo: str, tempo: int, artista: str, numero_trilhas: int, possuo: bool, comentario: str):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__artista = artista
        self.__numero_trilhas = numero_trilhas
        self.__possuo = possuo
        self.__comentario = comentario
    
    def get_titulo(self):
        return self.__titulo
    
    def get_tempo(self):
        return self.__tempo
    
    def get_artista(self):
        return self.__artista
    
    def get_numero_trilhas(self):
        return self.__numero_trilhas
    
    def get_possuo(self):
        return self.__possuo
    
    def get_comentario(self):
        return self.__comentario
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_tempo(self, tempo):
        self.__tempo = tempo
    
    def set_artista(self, artista):
        self.__artista = artista
    
    def set_numero_trilhas(self, numero_trilhas):
        self.__numero_trilhas = numero_trilhas
    
    def set_possuo(self, possuo):
        self.__possuo = possuo
    
    def set_comentario(self, comentario):
        self.__comentario = comentario
    
    def imprime(self):
        print(f"Título: {self.__titulo}, Artista: {self.__artista}, Tempo: {self.__tempo} min, Trilhas: {self.__numero_trilhas}, Possuo: {self.__possuo}, Comentário: {self.__comentario}")
