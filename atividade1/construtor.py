class Estudante:
    def aluno(aluno, nome, matricula, creditos, curso, notas):
        aluno.nome = nome
        aluno.matricula = matricula
        aluno.creditos = creditos
        aluno.curso = curso
        aluno.notas = notas
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
    estudante1 = Estudante("Filippi", 2023000020, 40, "Computacao", 9)
    estudante2 = Estudante("George o curioso", 101010010, 30 ,"Arquitetura", 10)
    estudante3 = Estudante("Luquinhas", 102000450, 50, "Engenharia de materiais", 25)
    estudante4 = Estudante("hominho", 2023000020, 20, "Nutricao", 11)
    estudante5 = Estudante("Deborah", 9999999999, 15 ,"Arquitetura", 24)
    estudante6 = Estudante("Dexter", 100000000, 10, "Engenharia de materiais", 12)

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