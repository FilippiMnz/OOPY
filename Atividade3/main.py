from catologo import *
from cd import *

if __name__ == "__main__":
    catalogo = Catalogo()
    
    cd1 = CD("Live in Texas", 45, "Linkin Park", 10, True, "Ótimo álbum!")
    cd2 = CD("LIBAD", 50, "Avenged Sevenfold", 12, True, "Bom pa Garai")
    cd3 = CD("Meteora", 50, "Linkin Park", 10, False, "Muito Bom")
    cd4 = CD("Elect The Dead Symphony", 56, "Serj Tankian",11, False, "Magnifico")
    catalogo.adicionar_cd(cd1)
    catalogo.adicionar_cd(cd2)
    catalogo.adicionar_cd(cd3)
    catalogo.adicionar_cd(cd4)
    
    print("Lista de CDs:")
    catalogo.listar_catalogo()
    
    print("\nVerificando se possuo Life is But a Dream:")
    catalogo.verificar_possuo("LIBAD")
    
    print("\nVerificando se há Meteora: ")
    catalogo.verificar_cd("Meteora")

    print("\nRemovendo Meteora")
    catalogo.remover_cd(cd3)

    
    print("\nLista de CDs após remoção:")
    catalogo.listar_catalogo()

    print("\nListar Cds Possuidos")
    catalogo.listar_cds_possuidos()