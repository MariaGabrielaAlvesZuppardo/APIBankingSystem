from typing import List, Optional
from app.api.models.client import Client
from app.api.models.account import Account

class Bank:
    def __init__(self):
        self.clients: List[Client] = []
        self.accounts: List[Account] = []
        
    def register_client(self, name: str, birth_date: str, cpf: str, address: str) -> Client:
        if self.find_client_by_cpf(cpf):
            raise ValueError(f"A client with CPF {cpf} is already registered.")
        
        client = Client(name, birth_date, cpf, address)
        self.clients.append(client)
        return client
    
    def find_client_by_cpf(self, cpf: str) -> Optional[Client]:
        for client in self.clients:
            if client.cpf == cpf:
                return client
        return None
