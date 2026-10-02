import customtkinter as ctk
from PIL import Image

from funcoes_docx.funcoes_cadastro import carregarTemplate, escolher_e_salvar_assinatura
from funcoes_cadastro_visual import acionar_cadastro


#BOTOES E ICONES
def criar_btn_cadastro(quadro_lateral, quadro_central,quadro_principal,cadastrarConteudo,usuario):

    icone_btn_cadastrar = ctk.CTkImage(light_image=Image.open("imagens/iconeCadastrar.png"),
                                       dark_image=Image.open("imagens/iconeCadastrar.png"),
                                       size=(60, 60))

    botao =  ctk.CTkButton(quadro_lateral,text="CADASTRAR CONTEÚDO",
                                   font=("roboto",14),
                                   width=300,
                                   height=55,
                                   corner_radius=8,
                                   fg_color="#1E293B",
                                   hover_color="#334155",
                                   image=icone_btn_cadastrar,
                                   compound="left",anchor="w", border_spacing=15,
                  command=lambda:(cadastrarConteudo(quadro_central, quadro_principal, usuario), selecionar_btn(botao)))
    botao.pack(pady=5,padx=15)

def criar_btn_visualizar(quadro_lateral, quadro_central, quadro_principal,visualizarConteudo,usuario):

    icone_btn_visualizar = ctk.CTkImage(light_image=Image.open("imagens/iconeVerRelatorio.png"),
                                        dark_image=Image.open("imagens/iconeVerRelatorio.png"),
                                        size=(60, 60))

    botao = ctk.CTkButton(quadro_lateral,
                  text="VISUALIZAR RELATÓRIO",
                  font=("roboto", 14), width=300,
                  height=55, corner_radius=8,
                  fg_color="#1E293B",
                  hover_color="#334155",
                  image=icone_btn_visualizar,
                  compound="left", anchor="w", border_spacing=15,
                          command=lambda:(visualizarConteudo(quadro_central, quadro_principal, usuario), selecionar_btn(botao)))

    botao.pack(pady=5,padx=15)

def criar_btn_cadastrarProfessor(quadro_lateral, quadro_central,quadro_principal, gerarRelatorio):
    icone_btn_gerar = ctk.CTkImage(light_image=Image.open("imagens/iconeProfessor.png"),
                                   dark_image=Image.open("imagens/iconeProfessor.png"),
                                   size=(70, 70))

    botao = ctk.CTkButton(quadro_lateral, text="CADASTRAR PROFESSOR",
                  font=("roboto", 14),
                  width=300, height=55,
                  corner_radius=8,
                  fg_color="#1E293B",
                  hover_color="#334155",
                  image=icone_btn_gerar,
                  compound="left", anchor="w", border_spacing=15,
                          command=lambda:(acionar_cadastro(), selecionar_btn(botao)))
    botao.pack(pady=5,padx=15)

def criar_btn_inserirAss(quadro_lateral, quadro_central,quadro_principal, inserirAss,usuario):
    icone_btn_inserirAss = ctk.CTkImage(light_image=Image.open("imagens/iconeInserirAss.png"),
                                        dark_image=Image.open("imagens/iconeInserirAss.png"),
                                        size=(60, 60))

    botao = ctk.CTkButton(quadro_lateral,text="INSERIR ASSINATURA",
                                font=("roboto",14),
                                width=300, height=55,
                                corner_radius=8,
                                fg_color="#1E293B",
                                hover_color="#334155",
                                image=icone_btn_inserirAss,
                                compound="left", anchor="w", border_spacing=15,
                                     command=lambda:(selecionar_btn(botao),escolher_e_salvar_assinatura(usuario)))
    botao.pack(pady=(3,15),padx=15)

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
