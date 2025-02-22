from cd import *
class Catalogo:
    def __init__(self):
        self.__cds = []
    
    def adicionar_cd(self, cd: CD):
        self.__cds.append(cd)
    
    def remover_cd(self, cd: CD):
        if cd in self.__cds:
            self.__cds.remove(cd)
         

    def listar_catalogo(self):
        if not self.__cds:
            return False
        else:
            for cd in self.__cds:
                cd.imprime()
    
    def verificar_cd(self, titulo: str):   #verifica pelo nome
        for cd in self.__cds:
            if cd.get_titulo() == titulo:
                cd.imprime()
                return
        return False
    
    def verificar_possuo(self, titulo: str):  #verifica o titulo e o bool
        for cd in self.__cds:
            if cd.get_titulo() == titulo and cd.get_possuo():
                cd.imprime()
                return
        return False
    
    
    def listar_cds_possuidos(self): #verifica o bool
        cds_possuidos = [cd for cd in self.__cds if cd.get_possuo()]
        if not cds_possuidos:
            return False
        else:
            for cd in cds_possuidos:
                cd.imprime()
