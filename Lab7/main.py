from catalogo import Catalogo
from cd import CD
from dvd import DVD

def main():
    catalogo = Catalogo()
    while True:
        print("\n1. Adicionar CD")
        print("2. Adicionar DVD")
        print("3. Remover item")
        print("4. Listar todos os itens")
        print("5. Listar CDs que possuo")
        print("6. Verificar se o catálogo está vazio")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título: ")
            tempo = int(input("Tempo de reprodução (min): "))
            artista = input("Artista: ")
            num_trilhas = int(input("Número de trilhas: "))
            possuo = input("Possui? (s/n): ").lower() == "s"
            comentario = input("Comentário: ")
            catalogo.adicionar(CD(titulo, tempo, artista, num_trilhas, possuo, comentario))
        elif opcao == "2":
            titulo = input("Título: ")
            tempo = int(input("Tempo de reprodução (min): "))
            diretor = input("Diretor: ")
            possuo = input("Possui? (s/n): ").lower() == "s"
            comentario = input("Comentário: ")
            catalogo.adicionar(DVD(titulo, tempo, diretor, possuo, comentario))
        elif opcao == "3":
            titulo = input("Título do item a remover: ")
            catalogo.remover(titulo)
        elif opcao == "4":
            catalogo.listar_todos()
        elif opcao == "5":
            catalogo.listar_cds_possuo()
        elif opcao == "6":
            print("O catálogo está vazio!" if catalogo.catalogo_vazio() else "O catálogo tem itens!")
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
