from componentes.conteiners_visualizarRelatorio import criarHeader, linhaDivisoria, criar_filtros, tabela
from componentes.objetosConteiner import criar_quadroCentral, criar_quadroPrincipal, limpar_tela
import customtkinter as ctk


def visualizarConteudo(quadro_central, quadro_principal,usuario):
    limpar_tela(quadro_central)

    #CABEÇALHO
    criarHeader(quadro_central)
    #DIVISAO
    linhaDivisoria(quadro_principal)
    #AREA DOS FILTROS
    organizaTabela,frameTabela = tabela(quadro_central)
    #OS FILTROS CONTROLAM A CRIAÇÃO DA ÁREA DE TABELA
    criar_filtros(quadro_central,usuario, organizaTabela,frameTabela)

