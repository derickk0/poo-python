from enum import Enum

class UnidadeFederativa(enumerate):
    BAHIA = ("Bahia", "BA")
    RIO_DE_JANEIRO = ("Rio de Janeiro")
    SAO_PAULO = ("São Paulo")

    def __init__(self, texto: str) -> None:
        self.texto = texto

