from funcionario import Funcionario


class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: str) -> None:
        super().__init__(departamento, cpf, dias_de_emprestimo=10)

    def emprestar(self, titulo_livro: str):
        return f"Funcionario administrativo " + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return f"Funcionario administrativo " + super().devolver(titulo_livro)
