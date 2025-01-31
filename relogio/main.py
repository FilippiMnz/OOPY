import time
from clockDisplay import ClockDisplay
from numberDisplay import NumberDisplay

#loop
relogio = ClockDisplay()
print(relogio.getTime())  

print("Testando loop:")
relogio.setTime(10,20, 50)
i = 0
while i < 10 :
    relogio.timeTick()
    print(relogio.getTime())  
    i += 1
    time.sleep(1)


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

#atividade 5
relogio.setTime(23, 59, 57)
print(relogio.getTime())  

relogio.timeTick()
print(relogio.getTime()) 

relogio.timeTick()
print(relogio.getTime()) 

relogio.timeTick()
print(relogio.getTime())  

#teste 1 hora, 3 incrementos atividade 5
print("teste 1:00")
relogio.setTime(00, 59, 57)

relogio.timeTick()
print(relogio.getTime())  

relogio.timeTick()
print(relogio.getTime())  

relogio.timeTick()
print(relogio.getTime())   #1 hora