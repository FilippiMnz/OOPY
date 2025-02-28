from item import Item

class CD(Item):
    def __init__(self, titulo, tempo_reproducao, artista, num_trilhas, possuo, comentario):
        super().__init__(titulo, tempo_reproducao, possuo, comentario)
        self.artista = artista
        self.num_trilhas = num_trilhas
    
    def imprime(self):
        print(f"CD - {self.titulo} | Artista: {self.artista} | Trilhas: {self.num_trilhas} | Tempo: {self.tempo_reproducao} min | Possuo: {self.possuo} | Comentário: {self.comentario}")
