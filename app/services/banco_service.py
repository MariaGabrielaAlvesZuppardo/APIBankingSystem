from app.core.banco import Banco
from app.api.models.conta import Conta

class BankService:
    def __init__(self):
        self.bank = Banco()
    
    def register_client(self, name: str, date_of_birth: str, cpf: str, address: str):
        return self.bank.register_client(name, date_of_birth, cpf, address)
    
    def create_current_account(self, cpf: str, initial_balance: float):
        client = self.bank.find_client_by_cpf(cpf)
        if not client:
            raise ValueError(f"Client with CPF {cpf} not found.")
        
        account = Conta(client, initial_balance)
        client.add_account(account)
        self.bank.accounts.append(account)
        return account
    
    def make_transaction(self, cpf: str, transaction_type: str, amount: float):
        client = self.bank.find_client_by_cpf(cpf)
        if not client or not client.accounts:
            raise ValueError(f"Client with CPF {cpf} not found or has no accounts.")
        
        account = client.accounts[0]  # Assuming the client has at least one account
        if transaction_type.lower() == "deposit":
            account.deposit(amount)
        elif transaction_type.lower() == "withdrawal":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type.")
        return "Transaction completed successfully."

    def show_statement(self, cpf: str):
        client = self.bank.find_client_by_cpf(cpf)
        if not client or not client.accounts:
            raise ValueError(f"Client with CPF {cpf} not found or has no accounts.")
        
        account = client.accounts[0]  # Assuming the client has at least one account
        return account.view_statement()
    def buscar_conta_por_numero(self, numero: int) -> Optional[Conta]:
        for conta in self.banco.contas:
            if conta.numero == numero:
                return conta
        return None
    
    def encerrar_conta(self, numero: int):
        conta = self.buscar_conta_por_numero(numero)
        if not conta:
            raise ValueError(f"Conta com número {numero} não encontrada.")
        
        self.banco.contas.remove(conta)
        conta.cliente.contas.remove(conta)