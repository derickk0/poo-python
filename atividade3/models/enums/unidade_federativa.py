from enum import Enum

class UnidadeFederativa(enumerate):
    BAHIA = ("Bahia, BA")
    SAO_PAULO = ("São Paulo, SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro, RJ")
    
    def __init__(self, texto: str) -> None:
        self.texto = texto
    