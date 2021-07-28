from controladorPessoas import ControladorPessoas
from controladorChamados import ControladorChamados


controlador = ControladorPessoas()

retorno = controlador.inclui_cliente(1, 'Israel')

print(retorno)

controlador_chamados = ControladorChamados()

retorno = controlador_chamados.inclui_chamado(1, 2, 3, 4, 5, 6, 7)

print(retorno)