from abc import abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: str, dias_de_emprestimo: int, matricula: int) -> None:
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def devolver(self, titulo_livro: str):
        return f"Aluno de matricula \"{self.__matricula}\" devolveu o livro: {titulo_livro}"
    
    def emprestar(self, titulo_livro: str):        
        return f"Aluno de matricula \"{self.matricula}\" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo"