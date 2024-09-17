from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor

class Funcionario:
    def __init__(self,
                nome: str,
                cpf: str,
                rg: str,
                endereco: Endereco,
                setor: Setor,
                sexo: Sexo,
                salario: float,
                dataNascimento: str
                ) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.setor = setor
        self.sexo = sexo
        self.salario = salario
        self.dataNascimento = dataNascimento

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nEndereço: {self.endereco}"
                f"\nSetor: {self.setor}"
                f"\nSexo: {self.sexo}"
                f"\nSalário: {self.salario}"
                f"\nData de nascimento: {self.dataNascimento}")