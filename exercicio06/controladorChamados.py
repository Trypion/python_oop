from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len([item for item in self.__chamados if item.tipo.codigo == tipo.codigo])

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if (isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(titulo, str) and isinstance(descricao, str) and isinstance(prioridade, int) and isinstance(tipo, TipoChamado)):
            chamado = Chamado(data, cliente, tecnico, titulo,
                            descricao, prioridade, tipo)

            duplicado = False
            for item in self.__chamados:
                if (item.data == data or item.cliente.codigo == cliente.codigo or item.tecnico.codigo == tecnico.codigo or item.tipo.codigo == tipo.codigo):
                    duplicado = True
                    break

            if not duplicado:
                self.__chamados.append(chamado)

            return chamado        

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        if (isinstance(codigo, int) and isinstance(nome, str), isinstance(descricao, str)):
            tipo = TipoChamado(codigo, descricao, nome)
            if not self.__verifica_duplicada(self.__tipos_chamados, codigo):
                self.__tipos_chamados.append(tipo)

            return tipo        

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados

    def __verifica_duplicada(self, lista, codigo):
        encontrado = False
        for item in lista:
            if item.codigo == codigo:
                encontrado = True
                break

        return encontrado
