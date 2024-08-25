from datetime import datetime

class Conta:
    numero_conta_sequencial = 1
    
    def __init__(self,cliente,saldo_inicial:float):
        self.agencia = "0001"
        self.numero = Conta.numero_conta_sequencial
        Conta.numero_conta_sequencial += 1 
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.historico = []
        self.transacoes_diarias = {}
        
    
    def depositar (self,valor:float):
        self.saldo += valor 
        self.historico.append ((datetime.now(),"Depósito",valor))
        
    
    def sacar (self,valor: float):
        if valor <= self.saldo:
            self.saldo -= valor 
            self.historico.append((datetime.now(),"Saque",valor))
        
        else:
            raise ValueError("Saldo insuficiente")   
    
    def visualizar_extrato(self):
        return [(data,tipo,valor) for data,tipo,valor in self.historico]            