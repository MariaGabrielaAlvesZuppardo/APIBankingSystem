from typing import List,Optional
from app.api.models.cliente import Cliente
from app.api.models.conta import Conta 

class Banco:
    def __init__(self):
        self.clientes: List[Cliente] = []
        self.contas: List [Conta] = []
        
    def cadastrar_cliente(self,nome:str,data_nascimento:str,cpf:str,endereco:str) -> Cliente:
        if self.buscar_cliente_por_cpf(cpf):
            raise ValueError(f"Já existe um cliente cadastrado com o CPF {cpf}.")
        
        cliente = Cliente(nome,data_nascimento,cpf,endereco)
        self.clientes.append(cliente)
        return cliente
    
    def buscar_cliente_por_cpf(self,cpf:str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None        