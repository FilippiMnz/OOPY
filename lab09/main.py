from conta import Conta
try:
    conta1 = Conta("Filippi")
    print(conta1)
    print("\n")

    print(conta1.deposito(1000))
    print(conta1.deposito(-100))  
    print("\n")

    print(conta1)

    print(conta1.saque(500))
    print(conta1.saque(1000))  
    print(conta1.saque(-100))  
    print("\n")

    print(conta1)

    conta1.setNome("")  
    conta1.setFlag("True")  
    conta1.setNumeroConta(-123)  
    
    print("\n")
    conta1.setFlag(False)
    print(conta1)
    print(conta1.deposito(100))  

except Exception as e:
    print(f"Erro durante execução: {e}")