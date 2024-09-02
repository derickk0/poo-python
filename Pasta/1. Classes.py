import os

os.system("cls || clear")

class Aluno:
    # nome, idade
    # Construtor
    def __init__(self, nome: str, idade: int) -> None:
        # Atributos
        self.nome = nome
        self.idade = idade

    def exibirDados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}" 

# Instanciar classe.
aluno = Aluno("Zé", 4)

# print(f"Nome: {aluno.nome}")
# print(f"Idade: {aluno.idade}")
print(aluno.exibirDados())