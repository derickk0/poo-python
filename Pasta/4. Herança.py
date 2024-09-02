from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    @abstractmethod
    def calcularSalario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcularSalario(self) -> float:
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario,)
        self.cnh = cnh

    def calcularSalario(self) -> float:
        BONIFICACAO = 1.5
        salario_final = self.salario * BONIFICACAO
        return salario_final


# Instanciamento de classes
gerente1 = Gerente("gerente", 45643, 5.0)
print(f"Nome: {gerente1.nome}")
print(f"Salário: R${gerente1.calcularSalario()} \n")

motoboy1 = Motoboy("zéca do grau", 3, 5000.0, 5534)
print(f"Nome: {motoboy1.nome}")
print(f"CNH: {motoboy1.cnh}")
print(f"Salário: R${motoboy1.calcularSalario()}")