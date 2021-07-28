from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        cliente = Cliente(nome, codigo)
        if not self.__verifica_duplicada(self.__clientes, codigo):
            self.__clientes.append(cliente)  
        return cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        tecnico = Tecnico(nome, codigo)
        if not self.__verifica_duplicada(self.__tecnicos, codigo):
            self.__tecnicos.append(tecnico)  
        return tecnico

    def __verifica_duplicada(self, lista, codigo):
        encontrado = False
        for item in lista:
            if item.codigo == codigo:
                encontrado = True
                break   

        return encontrado