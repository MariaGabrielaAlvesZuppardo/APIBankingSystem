from datetime import datetime

class Transacao:
    def __init__(self, tipo: str, valor: float):
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now()
