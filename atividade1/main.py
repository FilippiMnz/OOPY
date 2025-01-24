from professor import Professor
#Aluno
class Estudante:
    def __init__(self, nome: str, matricula: int, creditos: int):
        self.__nome: str = nome
        self.__matricula: int = matricula
        self.__creditos: int = creditos

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, novo_nome: str):
        if novo_nome:
            self.__nome = novo_nome
        else:
            print("Erro: Nome deve conter ao menos um elemento.")

    def get_matricula(self) -> int:
        return self._matricula

    def set_matricula(self, nova_matricula: int):
        if nova_matricula > 0:
            self._matricula = nova_matricula
        else:
            print("Erro: Matrícula deve ser um número inteiro positivo.")

    def get_creditos(self) -> int:
        return self.__creditos

    def set_creditos(self, novos_creditos: int):
        if novos_creditos >= 0:
            self.__creditos += novos_creditos
        else:
            print("Erro: A quantidade de créditos deve ser maior que 0")

    def adicionar_creditos(self, quantidade: int):
        if quantidade > 0:
            self.__creditos += quantidade
        else:
            print("Erro: A quantidade de créditos deve ser maior que 0.")

    def alterar_nome(self, novo_nome: str):
        self.set_nome(novo_nome)
    
def main():
    estudante1 = Estudante("Lipi", 20230000234, 40)
    estudante2 = Estudante("Guts", 20004240020, 20)
    estudante3 = Estudante("Casca", 2003299298, 10)
    estudante4 = Estudante("Grifith", 2000042424, 240)
    estudante5 = Estudante("Pluck", 202420003, 50)

    professor1 = Professor("Kalil", 303020230, 40)
    professor2 = Professor("Admilson", 20202042, 36)
    professor3 = Professor("Hendrik", 110120230, 20)
    professor4 = Professor("Rodolfo", 101010102, 40)
    professor5 = Professor("Calebe", 303030303, 36)


    while True:
        print("\nBem-vindo à UFC -- Universidade Federal da Cachaça")
        print("Selecione uma opção:")
        print("1- Ver Alunos")
        print("2- Modificar Créditos")
        print("3- Ver Professores")
        print("4- Modificar Carga Horaria")
        print("5- Sair")

        opcao = int(input("Digite a Opção desejada: "))

        if opcao == 1:
            print("\nLista de Alunos:")
            print(f"Aluno 1: {estudante1.get_nome()}, Créditos: {estudante1.get_creditos()}")
            print(f"Aluno 2: {estudante2.get_nome()}, Créditos: {estudante2.get_creditos()}")
            print(f"Aluno 3: {estudante3.get_nome()}, Créditos: {estudante3.get_creditos()}")
            print(f"Aluno 4: {estudante4.get_nome()}, Créditos: {estudante4.get_creditos()}")
            print(f"Aluno 5: {estudante5.get_nome()}, Créditos: {estudante5.get_creditos()}")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == 2:
            print("\nDeseja mudar os créditos de qual aluno?")
            print("1- Lipi")
            print("2- Guts")
            print("3- Casca")
            print("4- Grifith")
            print("5- Pluck")

            aluno = int(input("Insira o número do Aluno: "))
            if aluno == 1:
                novo_credito = int(input(f"Insira o novo número de créditos para {estudante1.get_nome()}: "))
                estudante1.set_creditos(novo_credito)
                print(f"Créditos de {estudante1.get_nome()} atualizados para {estudante1.get_creditos()}.")
            elif aluno == 2:
                novo_credito = int(input(f"Insira o novo número de créditos para {estudante2.get_nome()}: "))
                estudante2.set_creditos(novo_credito)
                print(f"Créditos de {estudante2.get_nome()} atualizados para {estudante2.get_creditos()}.")
            elif aluno == 3:
                novo_credito = int(input(f"Insira o novo número de créditos para {estudante3.get_nome()}: "))
                estudante3.set_creditos(novo_credito)
                print(f"Créditos de {estudante3.get_nome()} atualizados para {estudante3.get_creditos()}.")
            elif aluno == 4:
                novo_credito = int(input(f"Insira o novo número de créditos para {estudante4.get_nome()}: "))
                estudante4.set_creditos(novo_credito)
                print(f"Créditos de {estudante4.get_nome()} atualizados para {estudante4.get_creditos()}.")
            elif aluno == 5:
                novo_credito = int(input(f"Insira o novo número de créditos para {estudante5.get_nome()}: "))
                estudante5.set_creditos(novo_credito)
                print(f"Créditos de {estudante5.get_nome()} atualizados para {estudante5.get_creditos()}.")
            else:
                print("Número de aluno inválido.")
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 3:
            print("Lista Professores")
            print(f"1-{professor1.get_nome()} ")
            print(f"2-{professor2.get_nome()} ")
            print(f"3-{professor3.get_nome()} ")
            print(f"4-{professor4.get_nome()} ")
            print(f"5-{professor5.get_nome()} ")
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == 4:
            print("Mudança de Carga horaria")
            print(f"1-{professor1.get_nome()} Carga Horaria: {professor1.get_HoraTrabalho()} ")
            print(f"2-{professor2.get_nome()} Carga Horaria: {professor2.get_HoraTrabalho()}")
            print(f"3-{professor3.get_nome()} Carga Horaria: {professor3.get_HoraTrabalho()}")
            print(f"4-{professor4.get_nome()} Carga Horaria: {professor4.get_HoraTrabalho()}")
            print(f"5-{professor5.get_nome()} Carga Horaria: {professor5.get_HoraTrabalho()}")
            professorOpc = int(input("Digite o Numero do professor: "))
            if professorOpc == 1:
                print("Deseja diminuir ou aumentar a carga? ")
                print("1- Diminuir")
                print("2- Aumentar")
                opc = int(input("Insira a opcao"))
                if opc == 1 :
                    horas = int(input("Quantas horas deseja diminuir? "))
                    professor1.menos_horas(horas)
                    print(f"Horas de {professor1.get_nome()} atualizados para {professor1.get_HoraTrabalho()}.")
                elif opc == 2:
                    horas = int(input("Quantas horas deseja aumentar? "))
                    professor1.mais_horas(horas)
                    print(f"Horas de {professor1.get_nome()} atualizadas para {professor1.get_HoraTrabalho()}.")
            elif professorOpc == 2:
                print("Deseja diminuir ou aumentar a carga?")
                print("1- Diminuir")
                print("2- Aumentar")
                opc = int(input("Insira a opção: "))
                if opc == 1:
                    horas = int(input("Quantas horas deseja diminuir? "))
                    professor2.menos_horas(horas)
                    print(f"Horas de {professor2.get_nome()} atualizadas para {professor2.get_HoraTrabalho()}.")
                elif opc == 2:
                    horas = int(input("Quantas horas deseja aumentar? "))
                    professor2.mais_horas(horas)
                    print(f"Horas de {professor2.get_nome()} atualizadas para {professor2.get_HoraTrabalho()}.")

            elif professorOpc == 3:
                print("Deseja diminuir ou aumentar a carga?")
                print("1- Diminuir")
                print("2- Aumentar")
                opc = int(input("Insira a opção: "))
                if opc == 1:
                    horas = int(input("Quantas horas deseja diminuir? "))
                    professor3.menos_horas(horas)
                    print(f"Horas de {professor3.get_nome()} atualizadas para {professor3.get_HoraTrabalho()}.")
                elif opc == 2:
                    horas = int(input("Quantas horas deseja aumentar? "))
                    professor3.mais_horas(horas)
                    print(f"Horas de {professor3.get_nome()} atualizadas para {professor3.get_HoraTrabalho()}.")

            elif professorOpc == 4:
                print("Deseja diminuir ou aumentar a carga?")
                print("1- Diminuir")
                print("2- Aumentar")
                opc = int(input("Insira a opção: "))
                if opc == 1:
                    horas = int(input("Quantas horas deseja diminuir? "))
                    professor4.menos_horas(horas)
                    print(f"Horas de {professor4.get_nome()} atualizadas para {professor4.get_HoraTrabalho()}.")
                elif opc == 2:
                    horas = int(input("Quantas horas deseja aumentar? "))
                    professor4.mais_horas(horas)
                    print(f"Horas de {professor4.get_nome()} atualizadas para {professor4.get_HoraTrabalho()}.")

            elif professorOpc == 5:
                print("Deseja diminuir ou aumentar a carga?")
                print("1- Diminuir")
                print("2- Aumentar")
                opc = int(input("Insira a opção: "))
                if opc == 1:
                    horas = int(input("Quantas horas deseja diminuir? "))
                    professor5.menos_horas(horas)
                    print(f"Horas de {professor5.get_nome()} atualizadas para {professor5.get_HoraTrabalho()}.")
                elif opc == 2:
                    horas = int(input("Quantas horas deseja aumentar? "))
                    professor5.mais_horas(horas)
                    print(f"Horas de {professor5.get_nome()} atualizadas para {professor5.get_HoraTrabalho()}.")

            else:
                print("Número de professor inválido.")

            input("\nPressione Enter para voltar ao menu...")             
        elif opcao == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
