class NumberDisplay:
    def __init__(self, rollOverLimit):
        self.__limit = rollOverLimit
        self.__value = 0
    
    def incremento(self):
        self.__value = (self.__value + 1) % self.__limit
    
    def getDisplayValue(self):
        return f"{self.__value:02d}"
    

    #atividade 1
    def getValue(self):
        return self.__value
    
    
    def setValue(self, replacementValue):
        if 0 <= replacementValue < self.__limit:
            self.__value = replacementValue
        else:
            print("Valor inválido!")

    #