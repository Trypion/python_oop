from abc import abstractmethod
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU):
    @abstractmethod
    def __init__(self, departamento: str, cpf: str, dias_de_emprestimo: int) -> None:
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str):
        self.__departamento = departamento
  
    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return f"do departamento \"{self.departamento}\" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo"
    
    @abstractmethod
    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)