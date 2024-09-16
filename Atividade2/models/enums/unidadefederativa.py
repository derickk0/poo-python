from enum import Enum

class UnidadeFederativa(enumerate):
    BAHIA = ("Bahia", "BA")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")
    SAO_PAULO = ("São Paulo", "SP")

    def __init__(self, texto: str, sigla: str) -> None:
        self.texto = texto
        self.sigla = sigla

