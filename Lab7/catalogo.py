from item import Item
from cd import CD
from dvd import DVD

class Catalogo:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item):
        if isinstance(item, Item):
            self.itens.append(item)
    
    def remover(self, titulo):
        self.itens = [item for item in self.itens if item.titulo != titulo]
    
    def listar_todos(self):
        cds = [item for item in self.itens if isinstance(item, CD)]
        dvds = [item for item in self.itens if isinstance(item, DVD)]
        for item in cds + dvds:
            item.imprime()
    
    def listar_cds_possuo(self):
        for item in self.itens:
            if isinstance(item, CD) and item.possuo:
                item.imprime()

    def catalogo_vazio(self):
        return len(self.itens) == 0
