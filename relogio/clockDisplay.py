from numberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self):
        self.__hora = NumberDisplay(24)
        self.__minuto = NumberDisplay(60)
        self.__segundo = NumberDisplay(60) #atividade 6, não precisa modificar display
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

