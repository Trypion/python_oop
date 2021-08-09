from elevador import Elevador
from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        super().__init__()
        self.__elevador = None

    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        if (not isinstance(andar_atual, int)
            or not isinstance(total_andares_predio, int)
            or not isinstance(capacidade, int)
            or not isinstance(total_pessoas, int)
            or capacidade < 0
            or total_pessoas < 0
            or total_andares_predio < 0
            or andar_atual < 0
            or andar_atual > total_andares_predio
                or total_pessoas > capacidade):
            raise ComandoInvalidoException()

        self.__elevador = Elevador(
            capacidade, total_pessoas, total_andares_predio, andar_atual)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def subir(self) -> str:
        self.__elevador.subir()

    def descer(self) -> str:
        self.__elevador.descer()

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()
