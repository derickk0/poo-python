from enum import Enum

class Sexo(enumerate):
    MASCULINO = ("Masculino")
    FEMININO = ("Feminino")

    def __init__(self, texto: str) -> None:
        self.texto = texto
    

