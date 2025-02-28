from item import Item

class DVD(Item):
    def __init__(self, titulo, tempo_reproducao, diretor, possuo, comentario):
        super().__init__(titulo, tempo_reproducao, possuo, comentario)
        self.diretor = diretor
    
    def imprime(self):
        print(f"DVD - {self.titulo} | Diretor: {self.diretor} | Tempo: {self.tempo_reproducao} min | Possuo: {self.possuo} | Comentário: {self.comentario}")