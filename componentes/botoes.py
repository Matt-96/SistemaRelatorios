import customtkinter as ctk
from PIL import Image

from funcoes_docx.funcoes_cadastro import carregarTemplate, escolher_e_salvar_assinatura
from funcoes_cadastro_visual import acionar_cadastro
from tela_professores import visualizarProfessores

# CONSTANTES DE PADRONIZAÇÃO VISUAL DA BARRA LATERAL
ALTURA_BOTAO_MENU = 58
TAMANHO_ICONE_MENU = (40, 40)
COR_BOTAO_PADRAO = "#1E293B"
COR_BOTAO_HOVER = "#334155"
COR_BOTAO_SELECIONADO = "#263B63"
COR_TEXTO_PADRAO = "#F8FAFC"

def _criar_item_menu_padrao(quadro_lateral, texto, icone_path, comando=None, font_size=13):
    """Fábrica interna para garantir padronização rigorosa de todos os botões do menu."""
    icone = ctk.CTkImage(
        light_image=Image.open(icone_path),
        dark_image=Image.open(icone_path),
        size=TAMANHO_ICONE_MENU
    )

    botao = ctk.CTkButton(
        quadro_lateral,
        text=texto,
        font=("Roboto", font_size, "bold"),
        height=ALTURA_BOTAO_MENU,
        corner_radius=8,
        fg_color=COR_BOTAO_PADRAO,
        hover_color=COR_BOTAO_HOVER,
        text_color=COR_TEXTO_PADRAO,
        image=icone,
        compound="left",
        anchor="w",
        border_spacing=14
    )

    if comando:
        botao.configure(command=lambda: (comando(), selecionar_btn(botao)))
    else:
        botao.configure(command=lambda: selecionar_btn(botao))

    botao.pack(fill="x", padx=15, pady=4)
    return botao

# BOTOES E ICONES
def criar_btn_cadastro(quadro_lateral, quadro_central, disciplina, cadastrarConteudo, usuario):
    return _criar_item_menu_padrao(
        quadro_lateral=quadro_lateral,
        texto="CADASTRAR CONTEÚDO",
        icone_path="imagens/iconeCadastrar.png",
        comando=lambda: cadastrarConteudo(quadro_central, disciplina, usuario)
    )

def criar_btn_visualizar(quadro_lateral, quadro_central, quadro_principal, visualizarConteudo, usuario,disciplina):
    return _criar_item_menu_padrao(
        quadro_lateral=quadro_lateral,
        texto="VISUALIZAR RELATÓRIO",
        icone_path="imagens/iconeVerRelatorio.png",
        comando=lambda: visualizarConteudo(quadro_central, quadro_principal, usuario,disciplina)
    )

def criar_btn_cadastrarProfessor(quadro_lateral, quadro_central, quadro_principal, gerarRelatorio):
    return _criar_item_menu_padrao(
        quadro_lateral=quadro_lateral,
        texto="CADASTRAR PROFESSOR",
        icone_path="imagens/iconeCadastraProfessor.png",
        comando=lambda: acionar_cadastro()
    )

def criar_btn_visualizarProfessores(quadro_lateral, quadro_central, quadro_principal, usuario=None):
    return _criar_item_menu_padrao(
        quadro_lateral=quadro_lateral,
        texto="VISUALIZAR PROFESSORES\nCADASTRADOS",
        icone_path="imagens/iconeVisualizarProfessores.png",
        font_size=11,
        comando=lambda : visualizarProfessores(quadro_central,quadro_principal)
    )

def criar_btn_inserirAss(quadro_lateral, quadro_central, quadro_principal, inserirAss, usuario):
    return _criar_item_menu_padrao(
        quadro_lateral=quadro_lateral,
        texto="INSERIR ASSINATURA",
        icone_path="imagens/iconeInserirAss.png",
        comando=lambda: escolher_e_salvar_assinatura(usuario)
    )

def criar_btnPersonalizado(
    master,
    text="CTkButton",width=120,height=40,corner_radius=8,border_width=0,border_spacing=2,
    fg_color=None,hover_color=None,border_color=None,bg_color="transparent",
    text_color=None,text_color_disabled=None,font=None,textvariable=None,image=None,compound="left",
    anchor="center",state="normal",hover=True,command=None,**kwargs):
    botao =  ctk.CTkButton(
        master=master,
        text=text,
        width=width,
        height=height,
        corner_radius=corner_radius,
        border_width=border_width,
        border_spacing=border_spacing,
        fg_color=fg_color,
        hover_color=hover_color,
        border_color=border_color,
        bg_color=bg_color,
        text_color=text_color,
        text_color_disabled=text_color_disabled,
        font=font,
        textvariable=textvariable,
        image=image,
        compound=compound,
        anchor=anchor,
        state=state,
        hover=hover,
        command=command,
        **kwargs)

    botao.pack(pady=20)

    return botao

botao_selecionado = None #VARIAVEL INICIALIZADORA, NO MOMENTO QUE UM BOTÃO É CLICADO ELA RECEBE O BOTÃO QUE FOI CLICADO

def selecionar_btn(botao):
    global botao_selecionado
    if  botao_selecionado:
         botao_selecionado.configure(fg_color="#1E293B", state="normal") # SE ESTIVER SELECIONADO VOLTA PRA COR INICIAL

    botao.configure(fg_color="#263B63",state="disabled") #O BOTÃO RECEBE A COR DE SELECIONADO, TANTO QUE ESTÁ FORA DO IF
    botao_selecionado = botao # BOTÃO É O ATUAL E BOTAO_SELECIONADO É O ANTIGO. AQUI O BOTÃO ANTIGO PASSA A SER O BOTÃO SELECIONADO, PORTANTO O ATUAL
    #O OBJETIVO DA FUNÇÃO É MUDAR A COR DO BOTÃO PARA O USUÁRIO SABER QUE ESTÁ SELECIONADO, MAS PARA TANTO PRIMEIRO É
    #FEITA A VERIFICAÇÃO SE ELE JÁ ESTÁ SELECIONADO, CASO JÁ ESTEJA ELE RECEBE A COR INICIAL NO IF, SE A CONDIÇÃO FOR FALSA
    #ELE IGNORA O IF E SELECIONA O BOTÃO
