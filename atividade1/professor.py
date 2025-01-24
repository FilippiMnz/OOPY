class Professor:
    def __init__(self, nome, matriculaSIAPE, CargaHoraria):
        self.__nomeProf = nome
        self.__matriculaSIAPE = matriculaSIAPE
        self.__CargaHoraria = CargaHoraria

    def get_nome(self) -> str:
        return self.__nomeProf
    
    def set_nome(self, novo_nome: str):
        if novo_nome:
            self.__nomeProf = novo_nome
        else:
            print("Erro: Nome deve conter ao menos um elemento.")

    def get_MatriculaSIAPE(self):
        return self.__matriculaSIAPE

    def set_MatriculaSIAPE(self, NovaMatricula:int):
        if NovaMatricula > 0: 
            self.__matriculaSIAPE = NovaMatricula
        else: 
            print("Erro: o numero de matricula deve ser positivo")
    def get_HoraTrabalho(self):
        return self.__CargaHoraria
    def set_CargaHoraria(self, novaCarga: int):
        if novaCarga > 0:
            self.__CargaHoraria = novaCarga
        else:
            print("Erro: a carga horaria deve ser maior que 0")
    
    def mais_horas(self, horas: int):
        if horas > 0:
            self.__CargaHoraria += horas
        else:
            print("Erro: A quantidade de horas a adicionar deve ser maior que 0.")

    def menos_horas(self, horas: int):
        if 0 < horas <= self.__CargaHoraria:
            self.__CargaHoraria -= horas
        else:
            print("Erro: A quantidade de horas a remover deve ser positiva e menor ou igual à carga horária atual.")

    def Escolha(Opc):
        if Opc == 1:
            menos_horas()
        elif Opc == 2:
            mais_horas()
