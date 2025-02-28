class Item:
    def __init__(self, titulo, tempo_reproducao, possuo, comentario):
        self.__titulo = titulo
        self.__tempo_reproducao = tempo_reproducao
        self.__possuo = possuo
        self.__comentario = comentario
    
    def get_titulo(self):
        return self.__titulo

    def get_tempo_reproducao(self):
        return self.__tempo_reproducao
    
    def get_possuo(self):
        return self.__possuo
    
    def get_comentario(self):
        return self.__comentario
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_tempo_reproducao(self, tempo):
        self.__tempo_reproducao = tempo
    
    def set_possuo(self, possuo):
        self.__possuo = possuo
    
    def set_comentario(self, comentario):
        self.__comentario = comentario
    
    def imprime(self):
        print(f"Título: {self.__titulo}, Tempo de Reprodução: {self.__tempo_reproducao} min, Possuo: {self.__possuo}, Comentário: {self.__comentario}")
