from pydoc import doc
from xml.dom.minidom import Document
from constantes import MODELO_JUVENTUDE, MODELO_PCM
import customtkinter as ctk
import docx
from PIL import Image

from funcoes_docx.funcoes_leitura import buscarRelatorios, buscarDatas



#CABECALHO
def criarHeader(quadro_central):
    quadroHeader = ctk.CTkFrame(quadro_central, width=1500,height=150, fg_color="transparent", border_width=1, border_color="red")
    quadroHeader.pack(fill="x", pady=(10,0),padx=2)


    criar_hearderImg(quadroHeader)
    criar_frameTextos(quadroHeader)


    return quadroHeader


def criar_hearderImg(quadroHeaderl):
    img = ctk.CTkImage(light_image=Image.open("imagens/iconeVerRelatorio.png"), dark_image=Image.open(
        "imagens/iconeVerRelatorio.png"), size=(100, 100))
    labelImg = ctk.CTkLabel(quadroHeaderl, text="", image=img)
    labelImg.pack(side="left",padx=(10,0),pady=(10,0))

def criarLabelTitulo(quadroHeader):
    ctk.CTkLabel(quadroHeader, text="Visualizar Relatórios", font=("Roboto", 45)).pack()

def criar_TxtHeader(quaadroHeader):
    ctk.CTkLabel(quaadroHeader, text="Visualize os conteúdos cadastrados no relatório", font=("Roboto",20)).pack(padx=(45,0))

def linhaDivisoria(quadro_principal):
    linhaImg = ctk.CTkImage(light_image=Image.open("imagens/linhaCentralGrande.png"), dark_image=Image.open(
        "imagens/linhaCentralGrande.png"),
                            size=(1450,80))

    ctk.CTkLabel(quadro_principal, text="", image=linhaImg).pack(fill="x", padx=20)

def criar_frameTextos(quadroHeader):
    frameTexto = ctk.CTkFrame(quadroHeader,fg_color="transparent")
    frameTexto.pack(side="left")

    criarLabelTitulo(frameTexto)
    criar_TxtHeader(frameTexto)

    return frameTexto

#AREA DOS FILTROS

def criar_filtros(quadro_central,usuario, organizaTabela,frameTabela):
    frameFiltro = ctk.CTkFrame(quadro_central,
    border_width=1,
    border_color="green"
)

    frameFiltro.pack(fill="x", pady=(50,0))

    frameFiltro.grid_columnconfigure(0,weight=1)
    frameFiltro.grid_columnconfigure(1,weight=1)

    labelModeloRelatorio(frameFiltro)
    labelData(frameFiltro)


    menuModelo = criar_optionModelo(frameFiltro, usuario)
    menuData = criar_optionData(frameFiltro, usuario, menuModelo, organizaTabela,frameTabela)

    menuModelo.configure(
        command=lambda escolha: atualizaOptionData(
            menuData,
            usuario,
            escolha
        )
    )


def labelModeloRelatorio(frameModelo):
    modeloRelatorio = ctk.CTkLabel(frameModelo,text="Modelo do relatório", font=("Roboto", 20))#TITULO
    modeloRelatorio.grid(row=0,column=0, sticky="nw",pady=(0,10),padx=(20,0))

    return modeloRelatorio

def labelData(frame):
    labelData = ctk.CTkLabel(frame, text="Data", font=("Roboto", 20))
    labelData.grid(row=0,column=1,pady=(0,10), padx=(20,0), sticky="nw")

def criar_optionModelo(frame,usuario):
    modelos = buscarRelatorios(usuario)
    menuModelo = ctk.CTkOptionMenu(frame, fg_color="#080D19", values=modelos, button_color="#080D19",
                                height=40,
                                font=("Roboto", 16), dropdown_fg_color="#080D19", dropdown_font=("Roboto", 14))
    menuModelo.grid(row=1, column=0, sticky="w", pady=(0,10), padx=(20,0))

    menuModelo.set("Selecione o modelo")
    return menuModelo



def criar_optionData(frame,usuario,menuModelo, organizaTabela,frameTabela):
    menuData = ctk.CTkOptionMenu(frame, fg_color="#080D19", values=[], button_color="#080D19",
                                height=40,command=lambda escolha:pegaDataSelecionada(escolha,usuario,menuModelo,organizaTabela,frameTabela),
                                font=("Roboto", 16), dropdown_fg_color="#080D19", dropdown_font=("Roboto", 14))
    menuData.grid(row=1, column=1, sticky="w", pady=(0,10), padx=(20,0))
    menuData.set("Selecione a data")
    return menuData

def atualizaOptionData(menuData,usuario, modelo):
    novas_datas = buscarDatas(usuario, modelo)


    menuData.configure(values=novas_datas["datasFormatadas"])



    if novas_datas:
        menuData.set("Selecione a data")




def pegaDataSelecionada(dataSelecionada,usuario, menuModelo,organizaTabela,frameTabela):
        modelo = menuModelo.get()

        organizaTabela.pack(
            anchor="nw",
            fill="x",
            pady=(20, 0)
        )

        frameTabela.grid(padx=(30, 0))

        limpaTabela(frameTabela)

        cabecalhoTabela(frameTabela,modelo)

        corpoTabela(frameTabela,usuario,modelo,dataSelecionada)

#Parte da tabela
def tabela(frame):
    organizaTabela = ctk.CTkFrame(frame)
    #organizaTabela.pack(anchor="nw", fill="x", pady=(20,0))

    frameTabela = ctk.CTkFrame(organizaTabela, border_width=0,border_color="purple")
    #frameTabela.grid(padx=(30,0))

    frameTabela.grid_columnconfigure(0, weight=1,minsize=550)
    frameTabela.grid_columnconfigure(1, weight=1, minsize=780)

    #CABEÇALHO DA TABELA
    #cabecalhoTabela(frameTabela, modelo)
    #corpoTabela(frameTabela,usuario,modelo, data)

    return organizaTabela,frameTabela
def cabecalhoTabela(frame, modelo):
    if modelo == MODELO_PCM:


        turmaDisciplina = ctk.CTkLabel(frame,text="DISCIPLINA / TURMA", border_width=1, border_color="yellow",
                                       font=("Roboto", 20),height=50)
        turmaDisciplina.grid(row=0, column=0, sticky="ew")

        conteudo = ctk.CTkLabel(frame, text="CONTEÚDO MINISTRADO", border_width=1, border_color="yellow",
                                       font=("Roboto", 20), height=50)
        conteudo.grid(row=0, column=1, sticky="ew")

    elif modelo == MODELO_JUVENTUDE:
        Disciplina = ctk.CTkLabel(frame, text="PRÁTICA DE CONJUNTO", border_width=1, border_color="yellow",
                                       font=("Roboto", 20), height=50)
        Disciplina.grid(row=0, column=0, sticky="ew")

        conteudo = ctk.CTkLabel(frame, text="CONTEÚDO MINISTRADO", border_width=1, border_color="yellow",
                                font=("Roboto", 20), height=50)
        conteudo.grid(row=0, column=1, sticky="ew")


def corpoTabela(frame,usuario, modelo, data):
    cont = 1
    #PRECISO CRIAR UMA FUNÇÃO QUE CARREGUE O ARQUIVO SELECIONADO PELOS WIDGETS DE MODELO E DATA DA TELA DE VISUALIZAÇÃO


    dataFormatada = data.replace("/", "-")

    if modelo == MODELO_PCM:
        doc = docx.Document(
            fr"E:\Projetos\SistemaRelatorios\Professores\{usuario}\backupPCM\RelatorioPCMVioloncelo{dataFormatada}.docx")

        for tabela in doc.tables:  # DOCUMENTO
            for linha in tabela.rows:  # TABELA:
                if "TURMA" in linha.cells[0].text:
                    turma = ctk.CTkLabel(frame, text=linha.cells[0].text, border_width=1,
                                         border_color="yellow",
                                         font=("Roboto", 20), height=70)
                    turma.grid(row=cont, column=0, sticky="ew")

                    conteudo = ctk.CTkLabel(frame, text=linha.cells[1].text, border_width=1,
                                            border_color="yellow",
                                            font=("Roboto", 12), height=70)
                    conteudo.grid(row=cont, column=1, sticky="ew")

                    cont = cont + 1




    elif modelo == MODELO_JUVENTUDE:
        doc = docx.Document(
            fr"E:\Projetos\SistemaRelatorios\Professores\{usuario}\backupJuventude\RelatorioJuventudeVioloncelo{dataFormatada}.docx")



def limpaTabela(frameTabela):
    for widget in frameTabela.winfo_children():
        widget.destroy()



