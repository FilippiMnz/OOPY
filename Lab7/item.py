class Item:
    def __init__(self, titulo, tempo_reproducao, possuo, comentario):
        self.titulo = titulo
        self.tempo_reproducao = tempo_reproducao
        self.possuo = possuo
        self.comentario = comentario
    
    def imprime(self):
        print(f"Título: {self.titulo}, Tempo de Reprodução: {self.tempo_reproducao} min, Possuo: {self.possuo}, Comentário: {self.comentario}")
