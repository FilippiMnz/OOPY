class Estudante: 
    def adicionarCreditos(self, quantidade):
        if quantidade > 0:
            self.creditos += quantidade
        else: 
            print("Erro:  A quantidade precisa ser maior que 0")
    def DiminuirCreditos(self, quantidade):
        if quantidade > 0:
            self.creditos -= quantidade
        else: 
            print("Erro:  A quantidade precisa ser maior que 0")
    def mudarNome(self, novonome):
        self.nome = novonome
    def mudarCurso(self,novoCurso):
        self.curso = novoCurso
    def MudarNotas(self, novasnotas):
        if novasnotas > -1 : 
            self.notas = novasnotas


def main():
    estudante1 = Estudante()
    estudante1.nome = "Filippi"
    estudante1.matricula = 2023000020
    estudante1.creditos = 40
    estudante1.curso = "Computacao"
    estudante1.notas = 9

    estudante2 = Estudante()
    estudante2.nome = "George o curioso"
    estudante2.matricula = 101010010
    estudante2.creditos = 30
    estudante2.curso = "Arquitetura"
    estudante2.notas = 10

    estudante3 = Estudante()
    estudante3.nome = "Luquinhas"
    estudante3.matricula = 102000450
    estudante3.creditos = 50
    estudante3.curso = "Engenharia de materiais"
    estudante3.notas = 25

    estudante4 = Estudante()
    estudante4.nome = "hominho"
    estudante4.matricula = 2023000020
    estudante4.creditos = 20
    estudante4.curso = "Nutricao"
    estudante4.notas = 11

    estudante5 = Estudante()
    estudante5.nome = "Deborah"
    estudante5.matricula = 9999999999
    estudante5.creditos = 15
    estudante5.curso = "Arquitetura"
    estudante5.notas = 24

    estudante6 = Estudante()
    estudante6.nome = "Dexter"
    estudante6.matricula = 100000000
    estudante6.creditos = 10
    estudante6.curso = "Engenharia de materiais"
    estudante6.notas = 12

    print("Lista Alunos: ")
    print(f"Nomes: Aluno 1: {estudante1.nome}, Aluno 2: {estudante2.nome}, Aluno 3: {estudante3.nome}, Aluno 4: {estudante4.nome}, Aluno 5: {estudante5.nome}, Aluno 6: {estudante6.nome}")
    print(f"Creditos: Aluno 1: {estudante1.creditos}, Aluno 2: {estudante2.creditos}, Aluno 3: {estudante3.creditos}, Aluno 4: {estudante4.creditos}, Aluno 5: {estudante5.creditos}, Aluno 6: {estudante6.creditos}")
    
    
    buscaAluno = input("\n Digite o nome do aluno: ")
    adicionarCreditosEncontrado = int(input("Digite a quantidade de creditos: "))

    Encontrado = False
    if estudante1.nome == buscaAluno:
        estudante1.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    elif estudante2.nome == buscaAluno:
        estudante2.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    elif estudante3.nome == buscaAluno:
        estudante3.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    elif estudante4.nome == buscaAluno:
        estudante4.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    elif estudante5.nome == buscaAluno:
        estudante5.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    elif estudante6.nome == buscaAluno:
        estudante6.adicionarCreditos(adicionarCreditosEncontrado)
        Encontrado = True
    else: 
        print("Aluno não encontrado")

    if Encontrado == True:
        print("Lista Alunos: ")
        print(f"Nomes: Aluno 1: {estudante1.nome}, Aluno 2: {estudante2.nome}, Aluno 3: {estudante3.nome}, Aluno 4: {estudante4.nome}, Aluno 5: {estudante5.nome}, Aluno 6: {estudante6.nome}")
        print(f"Creditos: Aluno 1: {estudante1.creditos}, Aluno 2: {estudante2.creditos}, Aluno 3: {estudante3.creditos}, Aluno 4: {estudante4.creditos}, Aluno 5: {estudante5.creditos}, Aluno 6: {estudante6.creditos}")
    
    

main()