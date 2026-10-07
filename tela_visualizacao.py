from componentes.conteiners_visualizarRelatorio import (
    criarHeader,
    linhaDivisoria,
    criar_filtros,
    tabela,
    criar_btnEnviarDrive
)
from componentes.objetosConteiner import limpar_tela
import customtkinter as ctk


def visualizarConteudo(quadro_central, quadro_principal, usuario, disciplina_var):
    limpar_tela(quadro_central)

    disciplina = disciplina_var.get()

    # 1. BOTÃO DE ENVIO FIXO NO RODAPÉ (seguindo o padrão da tela de cadastro)
    criar_btnEnviarDrive(quadro_central)

    # 2. CABEÇALHO
    criarHeader(quadro_central)

    # 3. LINHA DIVISÓRIA
    linhaDivisoria(quadro_principal)

    # 4. ÁREA DA TABELA ROLÁVEL (CTkScrollableFrame)
    organizaTabela, frameTabela = tabela(quadro_central)

    # 5. ÁREA DOS FILTROS (MODELO E DATA)
    criar_filtros(quadro_central, usuario, organizaTabela, frameTabela, disciplina)
