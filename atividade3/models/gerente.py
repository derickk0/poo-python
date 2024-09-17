from models.funcionario import Funcionario

class Gerente:
    def __init__(self, funcionario: Funcionario) -> None:
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (f"\n{self.funcionario}"
                f"\nSalário bonificado: {self.funcionario.salario * 1.35}")