from models.funcionario import Funcionario

class Motorista:
    def __init__(self, habilitacao: str, funcionario: Funcionario) -> None:
        self.habilitacao = habilitacao
        self.funcionario = funcionario

    def __str__(self) -> str:
        return (f"\n{self.funcionario}"
                f"\nHabilitação: {self.habilitacao}")