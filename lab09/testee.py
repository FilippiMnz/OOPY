class Conta:
    def __init__(self, nome_correntista, numero_conta):
        self.__nome_correntista = nome_correntista
        self.__numero_conta = numero_conta
        self.__saldo = 0.0
        self.__ativa = True
    
    def get_nome_correntista(self):
        return self.__nome_correntista
    
    def get_numero_conta(self):
        return self.__numero_conta
    
    def get_saldo(self):
        return self.__saldo
    
    def get_ativa(self):
        return self.__ativa
    
    def set_nome_correntista(self, novo_nome):
        if not novo_nome or not isinstance(novo_nome, str):
            raise ValueError("Nome do correntista deve ser uma string não vazia")
        self.__nome_correntista = novo_nome
    
    def set_numero_conta(self, novo_numero):
        if not isinstance(novo_numero, str):
            raise ValueError("Número da conta deve ser uma string")
        self.__numero_conta = novo_numero
    
    def set_ativa(self, status):
        if not isinstance(status, bool):
            raise ValueError("Status da conta deve ser True ou False")
        self.__ativa = status
    
    def depositar(self, valor):
        if not self.__ativa:
            raise ValueError("Conta inativa. Não é possível realizar depósitos.")
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        self.__saldo += valor
    
    def sacar(self, valor):
        if not self.__ativa:
            raise ValueError("Conta inativa. Não é possível realizar saques.")
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para o saque")
        self.__saldo -= valor
    
    def __str__(self):
        return f"Conta de {self.__nome_correntista} (Nº {self.__numero_conta}) - Saldo: R${self.__saldo:.2f} - {'Ativa' if self.__ativa else 'Inativa'}"