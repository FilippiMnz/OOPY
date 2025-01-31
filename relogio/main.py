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


class ClockDisplay:
    def __init__(self):
        self.__hora = NumberDisplay(24)
        self.__minuto = NumberDisplay(60)
        self.__segundo = NumberDisplay(60)
        self.__updateDisplay()
    
    def __updateDisplay(self):
        self.__displayString = f"{self.__hora.getDisplayValue()}:{self.__minuto.getDisplayValue()}:{self.__segundo.getDisplayValue()}"
    
    def timeTick(self):
        self.__segundo.incremento()
        if self.__segundo.getValue() == 0:
            self.__minuto.incremento()
            if self.__minuto.getValue() == 0:
                self.__hora.incremento()
        self.__updateDisplay()
    
    #atividade 3
    def getTime(self):
        return self.__displayString
    

    def setTime(self, hour, minute, second=0):
        self.__hora.setValue(hour)
        self.__minuto.setValue(minute)
        self.__segundo.setValue(second)
        self.__updateDisplay()



# Teste atividade 2
print("Testando NumberDisplay:")
teste_numero = NumberDisplay(60)
teste_numero.setValue(10)
print(teste_numero.getDisplayValue())  
print(teste_numero.getDisplayValue())  

# Teste atividade 4
print("\nTestando ClockDisplay:")
relogio = ClockDisplay()
print(relogio.getTime())  

relogio.setTime(23, 59, 57)
print(relogio.getTime())  

relogio.timeTick()
print(relogio.getTime()) 

relogio.timeTick()
print(relogio.getTime()) 

relogio.timeTick()
print(relogio.getTime())  
