from random import randint

class Conta:
    def __init__(self, correntista, numero_conta=None):
        self.__correntista = correntista
        try:
            self.__numero_conta = numero_conta if numero_conta else randint(100000, 999999)
        except Exception as e:
            print(f"Erro ao gerar número da conta: {e}")
            self.__numero_conta = randint(100000, 999999)
        
        self.__saldo = 0.0  
        self.__flag = True
    
    def getCorrentista(self):
        return self.__correntista
    
    def getNumeroConta(self):
        return self.__numero_conta
    
    def getSaldo(self):
        return self.__saldo
    
    def getFlag(self):
        return self.__flag
    
    def setNome(self, novo_nome):
        try:
            if not novo_nome or not isinstance(novo_nome, str):
                raise ValueError("Nome inválido")
            self.__correntista = novo_nome
        except ValueError as ve:
            print(f"Erro ao alterar nome: {ve}")
        except Exception as e:
            print(f"Erro inesperado ao alterar nome: {e}")
    
    def setFlag(self, novo_status):
        try:
            if not isinstance(novo_status, bool):
                raise TypeError("Status deve ser True ou False")
            self.__flag = novo_status
        except TypeError as te:
            print(f"Erro ao alterar status: {te}")
        except Exception as e:
            print(f"Erro inesperado ao alterar status: {e}")
    
    def setNumeroConta(self, novonumero):
        try:
            if not isinstance(novonumero, int) or novonumero <= 0:
                raise ValueError("Número da conta deve ser inteiro positivo")
            self.__numero_conta = novonumero
        except ValueError as ve:
            print(f"Erro ao alterar número da conta: {ve}")
        except Exception as e:
            print(f"Erro inesperado ao alterar número da conta: {e}")
    
    def deposito(self, valor):
        try:
            if not self.__flag:
                raise PermissionError("Conta inativa.")
            if not isinstance(valor, (int, float)) or valor <= 0:
                raise ValueError("Valor de depósito inválido.")
            
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
        except (PermissionError, ValueError) as pe:
            return str(pe)
        except Exception as e:
            return f"Erro inesperado durante depósito: {e}"
    
    def saque(self, valor):
        try:
            if not self.__flag:
                raise PermissionError("Conta inativa. Operação não permitida.")
            if not isinstance(valor, (int, float)) or valor <= 0:
                raise ValueError("Valor de saque inválido.")
            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente.")
            
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
        except (PermissionError, ValueError) as pe:
            return str(pe)
        except Exception as e:
            return f"Erro inesperado durante saque: {e}"
    
    def __str__(self):
        status = "Ativa" if self.__flag else "Inativa"
        return (f"Correntista: {self.__correntista}\n"
                f"Número da conta: {self.__numero_conta}\n"
                f"Saldo disponível: R${self.__saldo:.2f}\n"
                f"Status: {status}")


