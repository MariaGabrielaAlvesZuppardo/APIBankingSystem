from datetime import datetime

class Cliente : 
    def __init__(self,nome:str,data_nascimento:datetime, cpf:str,endereco:str) :
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        self.contas = []
        
    
    def adicionando_conta(self,conta):
        self.contas.append(conta)    