from autor import Autor
from editora import Editora
from capitulo import Capitulo


class Livro():
    def __init__(self, codigo: int, titulo: str, ano: int,
                 editora: Editora, autor: Autor,
                 numero_capitulo: int, titulo_capitulo: str) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self. __editora = editora
        self.__autor = autor
        self.__capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos = [self.__capitulo]
        self.__autores = [self.__autor]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora

    @property
    def autores(self) -> list:
        return self.__autores

    @property
    def capitulos(self) -> list:
        return self.__capitulos

    def incluir_autor(self, autor: Autor) -> None:
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor) -> None:
        if isinstance(autor, Autor) and autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str) -> None:
        encontrado = self.find_capitulo_by_titulo(titulo)
        if not encontrado:
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str) -> None:
        for index, capitulo in enumerate(self.__capitulos):
            if capitulo.titulo == titulo:
                del self.__capitulos[index]

    def find_capitulo_by_titulo(self, titulo: str) -> Capitulo:
        for index, capitulo in enumerate(self.__capitulos):
            if capitulo.titulo == titulo:
                return self.__capitulos[index]
