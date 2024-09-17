from enum import Enum

class Setor(enumerate):
    ENGENHARIA = ("Engenharia")
    JURIDICO = ("Jurídico")
    RECURSOS_HUMANOS = ("Recursos Humanos")
    MARKETING = ("Marketing")
    OPERACOES = ("Operações")

    def __init__(self, texto: str) -> None:
        self.texto = texto