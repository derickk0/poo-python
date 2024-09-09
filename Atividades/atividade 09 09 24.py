import os
from enum import Enum
os.system("cls || clear")

class Sexo(enumerate):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(enumerate):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "RH"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self,
                id: int,
                nome: str,
                idade: int,
                salario: float,
                setor: Setor,
                sexo: Sexo
                ) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}"
                )
    
funcionario1 = Funcionario(6666554, "jão kleb", 56, 5000, Setor.VENDAS, Sexo.MASCULINO)

print(funcionario1)