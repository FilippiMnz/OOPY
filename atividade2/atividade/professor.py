class Professor:
    def __init__(self, nome, siape, carga_horaria):
        self.__nome = nome
        self.__siape = siape
        self.__carga_horaria = carga_horaria

    def get_nome(self):
        return self.__nome

    def get_siape(self):
        return self.__siape

    def get_carga_horaria(self):
        return self.__carga_horaria

    def set_nome(self, nome):
        self.__nome = nome

    def set_siape(self, siape):
        self.__siape = siape

    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    def maisHoras(self, horas):
        if horas > 0:
            self.__carga_horaria += horas
        else:
            print("A quantidade de horas a ser adicionada deve ser positiva.")

    def menosHoras(self, horas):
        if horas > 0:
            if self.__carga_horaria - horas >= 0:
                self.__carga_horaria -= horas
            else:
                print("A carga horária não pode ser negativa.")
        else:
            print("A quantidade de horas a ser reduzida deve ser positiva.")
