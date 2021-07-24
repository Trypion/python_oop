from abc import ABC, abstractmethod


class UsuarioBU(ABC):
    @abstractmethod
    def __init__(self, cpf: str, dias_de_emprestimo: int):
        self.__cpf = cpf
        self.__dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int):
        self.__dias_de_emprestimo = dias_de_emprestimo

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        ...

    @abstractmethod
    def devolver(self, titulo_livro: str):
        ...
