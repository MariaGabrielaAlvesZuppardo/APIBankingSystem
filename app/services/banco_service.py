from app.core.banco import Banco
from app.api.models.conta import Conta 

class BancoService:
    def __init__(self):
        self.banco = Banco()
    
    
    def cadastrar_cliente(self,nome:str,data_nascimento:str,cpf:str,endereco:str):
        return self.banco.cadastrar_cliente(nome,data_nascimento,cpf,endereco)
    
    def criar_conta_corrente(self,cpf:str,saldo_inicial:float):
        cliente = self.banco.buscar_cliente_por_cpf(cpf)
        if not cliente:
            raise ValueError(f"Cliente com CPF {cpf} não encontrado")
        
        conta = Conta(cliente,saldo_inicial) 
        cliente.adicionando_conta(conta)
        self.banco.contas.append(conta)
        return conta
    def realizar_transacao(self, cpf: str, tipo: str, valor: float):
        cliente = self.banco.buscar_cliente_por_cpf(cpf)
        if not cliente or not cliente.contas:
            raise ValueError(f"Cliente com CPF {cpf} não encontrado ou não possui contas.")
        
        conta = cliente.contas[0]  # Supondo que o cliente tenha ao menos uma conta
        if tipo.lower() == "depósito":
            conta.depositar(valor)
        elif tipo.lower() == "saque":
            conta.sacar(valor)
        else:
            raise ValueError("Tipo de transação inválido.")
        return "Transação realizada com sucesso."

    def exibir_extrato(self, cpf: str):
        cliente = self.banco.buscar_cliente_por_cpf(cpf)
        if not cliente or not cliente.contas:
            raise ValueError(f"Cliente com CPF {cpf} não encontrado ou não possui contas.")
        
        conta = cliente.contas[0]  # Supondo que o cliente tenha ao menos uma conta
        return conta.visualizar_extrato()   
        