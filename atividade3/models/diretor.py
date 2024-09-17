from models.funcionario import Funcionario
from enum import Enum

class Premio(enumerate):
    PREMIO = 0.5

class Diretor:
    def __init__(self, funcionario: Funcionario) -> None:
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (f"\n{self.funcionario}"
                f"\nSalário bonificado: {self.funcionario.salario * (1.45 + Premio.PREMIO)}")