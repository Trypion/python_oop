from livro import Livro


class Biblioteca:
    def __init__(self) -> None:
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        try:
            self.__livros.remove(livro)
        except ValueError:
            ...

    @property
    def livros(self) -> list:
        return self.__livros
