from cd import CD
from dvd import DVD
from item import Item

class Catalogo:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item):
        if isinstance(item, Item):
            self.itens.append(item)
    
    def remover(self, titulo):
        for item in self.itens:
            if item.get_titulo() == titulo:
                self.itens.remove(item)
                return True
        return False
    
    def listar_todos(self):
        cds = [item for item in self.itens if isinstance(item, CD)]
        dvds = [item for item in self.itens if isinstance(item, DVD)]
        for item in cds + dvds:
            item.imprime()
    
    def listar_cds_possuo(self):
        for item in self.itens:
            if isinstance(item, CD) and item.get_possuo():
                item.imprime()

    def catalogo_vazio(self):
        if len(self.itens) == 0:
            return True
        else:
            return False