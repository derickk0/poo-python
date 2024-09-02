import os

os.system("cls || clear")

class Livro:
    def __init__(self, titulo: str, autor: str, quantidadePaginas: int, preco: float) -> None:
        self.titulo = preco
        self.autor = autor
        self.quantidadePaginas = quantidadePaginas
        self.preco = preco

    def exibirDados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nQuantidade de páginas: {self.quantidadePaginas} \nPreço: {self.preco}"

livro = Livro("fodase","fodase jr",55,765478468)

print(livro.exibirDados())