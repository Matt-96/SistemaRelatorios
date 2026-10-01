import customtkinter as ctk #importação da biblioteca
from PIL import Image
from componentes.botoes import *
from componentes.objetosConteiner import cabecalho, frame_lateral, criar_quadroPrincipal, criar_quadroCentral, \
    criar_sessaoBoasvindas, criar_quadroUsuario, criar_labelUsuario, criar_labelTitulolUsuario, criar_imagemUsuario, \
    criar_btnLogOut, criar_frameMenu
from tela_cadastro import cadastrarConteudo
from tela_gerarRelatorio import gerarRelatorio
from tela_visualizacao import visualizarConteudo
from tela_inserirAss import  inserirAss


def menu_principal(janela,usuario, login):
    #CRIA A JANELA QUE IRÁ A ABRIGAR OS ELEMENTOS
    janela.geometry("1920x1080")
    janela.title("Gerador de Relatórios")



    #QUADRO LATERAL
    quadro_lateral = frame_lateral(janela)


    #CABEÇALHO
    cabecalho(quadro_lateral)#CRIA O CABEÇALHO

    # ARÉA PRINCIPAL
    quadro_principal = criar_quadroPrincipal(janela)
    quadro_central = criar_quadroCentral(quadro_principal)

    # SESSÃO DO USUÁRIO
    quadro_usuario = criar_quadroUsuario(quadro_lateral)  # CRIA A SESSAO QUADRO USUARIO
    criar_labelTitulolUsuario(quadro_usuario)  # CRIA O TITULO USUARIO
    criar_labelUsuario(quadro_usuario, usuario)  # INSERE O USUARIO QUE ESTÁ LOGADO NA TELA
    criar_imagemUsuario(quadro_usuario)  # MOSTRA A IMAGEM DO USUARIO
    criar_btnLogOut(quadro_usuario, quadro_principal, quadro_lateral, login, janela)

    #AREA DO MENU
    frame_Menu = criar_frameMenu(quadro_lateral)



    # BOTÕES
    criar_btn_cadastro(frame_Menu, quadro_central, quadro_principal, cadastrarConteudo,usuario)

    criar_btn_visualizar(frame_Menu, quadro_central,quadro_principal,visualizarConteudo, usuario)

    criar_btn_gerar(frame_Menu, quadro_central,quadro_principal, gerarRelatorio)

    criar_btn_inserirAss(frame_Menu, quadro_central, quadro_principal,inserirAss,usuario)

    #SESSÃO BOAS VINDAS
    criar_sessaoBoasvindas(quadro_central)









