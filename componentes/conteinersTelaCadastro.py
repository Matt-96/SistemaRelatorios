from pydoc import text

import customtkinter as ctk
from PIL import Image

from constantes import MODELO_PCM
from caminhos import obter_caminho_template

from funcoes_docx.funcoes_cadastro import carregarTemplate, extrair_turmasPCM, escolheTurma, mostraTurmasPCM
from datetime import date
import docx
#HEADER - TÍTULO COM IMAGEM E TEXTO

#POSICIONAMENTO DA IMAGEM
def criar_frameTextos(quadroHeader):
    frameTexto = ctk.CTkFrame(quadroHeader,fg_color="transparent")
    frameTexto.pack(side="left")

    criarLabelTitulo(frameTexto)
    criar_TxtHeader(frameTexto)

    return frameTexto

def criar_hearderImg(quadroHeaderl):
    img = ctk.CTkImage(light_image=Image.open("imagens/headerCadastro.png"), dark_image=Image.open(
        "imagens/headerCadastro.png"), size=(100,100))
    labelImg = ctk.CTkLabel(quadroHeaderl, text="", image=img)
    labelImg.pack(side="left",padx=(10,0),pady=(10,0))

def criarLabelTitulo(quadroHeader):
    ctk.CTkLabel(quadroHeader, text="Cadastrar Conteúdo", font=("Roboto", 45)).pack()

def criar_TxtHeader(quaadroHeader):
    ctk.CTkLabel(quaadroHeader, text="Informe os conteúdos trabalhados durante a aula.", font=("Roboto",20)).pack(padx=(45,0))

def linhaDivisoria(quadro_principal):
    linhaImg = ctk.CTkImage(light_image=Image.open("imagens/linhaCentralGrande.png"), dark_image=Image.open(
        "imagens/linhaCentralGrande.png"),
                            size=(1450,80))

    ctk.CTkLabel(quadro_principal, text="", image=linhaImg).pack(fill="x", padx=20)

def criarHeader(quadro_central):
    quadroHeader = ctk.CTkFrame(quadro_central, width=1500,height=150, fg_color="transparent")
    quadroHeader.pack(fill="x", pady=(10,0),padx=2)

    criar_hearderImg(quadroHeader)


    return quadroHeader
#ARÉA MODELO E DATA
def criar_frameInformacoes(quadro_central):
    frameInformacao =  ctk.CTkFrame(quadro_central,fg_color="transparent")
    frameInformacao.pack(fill="x", padx=2)

    frameInformacao.grid_columnconfigure(0,weight=1)
    frameInformacao.grid_columnconfigure(1,weight=1)

    return frameInformacao



#AREA DO MODELO E BOTOES DE RADIO
def criar_frameModelo(frameInformacao):
    frameModelo = ctk.CTkFrame(frameInformacao,fg_color="transparent")
    frameModelo.grid(row=0,column=0, sticky="nw")

    return frameModelo


def labelModeloRelatorio(frameModelo):
    modeloRelatorio = ctk.CTkLabel(frameModelo,text="Modelo do relatório", font=("Roboto", 20))#TITULO
    modeloRelatorio.grid(row=0,column=0, sticky="nw",pady=(0,10),padx=(20,0))

    return modeloRelatorio


def labelConteudo(txtBox):
    ctk.CTkLabel(txtBox, text="Conteúdo", font=("Roboto", 23)).pack(side="top", anchor="nw", padx=20, pady=(15, 15))  # SUB-TITULO

#AREA PARA AS TURMAS PCM
def criar_frameTurmas(frameModelo,usuario,disciplina, MODELO_PCM):
    frameTurmas = ctk.CTkFrame(frameModelo, fg_color="transparent")
    frameTurmas.grid(row=4, padx=(20,0))

    doc = docx.Document(obter_caminho_template(usuario, disciplina, MODELO_PCM))
    turmas = extrair_turmasPCM(doc)
    txtTurma = ctk.CTkLabel(frameTurmas, text="Turma", font=("Roboto",20))
    txtTurma.grid(sticky="w", padx=(30,0), pady=(0,10))
    menuOpcoes = ctk.CTkOptionMenu(frameTurmas, width=350, fg_color="#080D19", values=turmas, height=40,
    font=("Roboto",18), button_color="#080D19", dropdown_fg_color="#080D19", dropdown_font=("Roboto",18))
    menuOpcoes.grid(padx=(30,0))

    return frameTurmas, menuOpcoes





#CAMPO TEXTBOX PARA CADASTRAR OS CONTEUDOS
def criar_frameTxtBox(quadro_central):
   txtBox =  ctk.CTkFrame(quadro_central, fg_color="transparent",height=500)
   txtBox.pack(side="bottom", fill="x")

   return txtBox

def criarCaixaConteudo(txtBox):
     caixa = ctk.CTkTextbox(txtBox,  # CAMPO DE INPUT
                   corner_radius=12, border_width=1,border_color="#5EEAD4")
     caixa.pack(expand=True, fill="both", padx=20)

     return caixa

#SESSÃO DATA E HORA
def verificarSwitch(switch,label_data, dicionario,data_var):
    # LOGICA PARA SABER SE O BOTÃO ESTÁ LIGADO OU NÃO
    if switch.get() == 1: # SE ESTIVER LIGADO ELE PEGA A DATA AUTOMATICAMENTE
        data = date.today().strftime("%d/%m/%Y")
        label_data.configure(text=f"Data atual: {data}")

        dicionario['Frame'].grid_forget()



    else:

        dicionarioMes = {
            'Janeiro': '01',
            'Fevereiro': '02',
            'Março': '03',
            'Abril': '04',
            'Maio': '05',
            'Junho': '06',
            'Julho': '07',
            'Agosto': '08',
            'Setembro': '09',
            'Outubro': '10',
            'Novembro': '11',
            'Dezembro': '12'
        }

        label_data.configure(text="Data Selecionada:")
        dicionario['Frame'].grid(row=3, column=1, sticky="w",pady=(0,10))

        dia = dicionario['Dia'].get()
        mes_selecionado = dicionario['Mes'].get()
        ano = dicionario['Ano'].get()

        mes = dicionarioMes[mes_selecionado]

        data = f"{int(dia):02d}/{mes}/{ano}"
    data_var.set(data)


def criarQuadroData(frameInformacao):
     data_var = ctk.StringVar()
     #FRAME DATA
     frameData = ctk.CTkFrame(frameInformacao, fg_color="transparent")
     frameData.grid(row=0, column=1,sticky="w")
    #TITULO DATA
     ctk.CTkLabel(frameData, text="Data do relatório",font=("Roboto",20)).grid(row=0,column=1,sticky="w",pady=(0,10))
     # FRAME CALENDARIO
     frame_calendario = ctk.CTkFrame(frameData, width=350, height=40, border_width=1, border_color="gray",
                                     corner_radius=6, fg_color="#0B1120")
     frame_calendario.grid(column=1,row=2,sticky="w", pady=(0,10))
     frame_calendario.grid_columnconfigure(0,weight=1)
     frame_calendario.grid_propagate(False)

     # IMAGEM CALENDARIO
     calendario = ctk.CTkImage(light_image=Image.open("imagens/calendario.png"),
                               dark_image=Image.open("imagens/calendario.png"), size=(35, 35))
     # LABEL DATA ATUAL
     label_data = ctk.CTkLabel(frame_calendario, text="Data Atual:", image=calendario, font=("Roboto", 16),
                               compound="left", fg_color="transparent")
     label_data.grid(column=0,row=0,sticky="w",pady=(2,0), padx=(5,0))


     dicionario = criarOptionsMenu(frameData,label_data,data_var)

     #SWITCH DE DATA
     switch = ctk.CTkSwitch(frameData, text="Usar data automática (data atual)", font=("Roboto",18),
                   fg_color="#334155",progress_color="#6535E9",switch_height=25, switch_width=50, command=lambda :verificarSwitch(switch,label_data,dicionario, data_var))
     switch.grid(sticky="w",row=1,column=1,pady=(0,10))


     return switch, dicionario, data_var

def criarOptionsMenu(frameData,label_data,data_var):
    #FRAME PARA COLOCAR ESSA SEÇAO
    frame_data_manual = ctk.CTkFrame(
        frameData,
        width=550,
        height=150,
        fg_color="transparent"
    )

    frame_data_manual.grid(row=3,column=1,sticky="w")

    valores_dias = [str (i) for i in range(1,32)]
    valores_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho","Agosto","Setembro","Outubro",
                     "Novembro", "Dezembro"]
    valores_anos = [str(i) for i in range(2026,2127) ]
    ctk.CTkLabel(frame_data_manual, text="Inserir data manualmente", font=("Roboto", 20)).grid(row=3,columnspan=3,sticky="w")
    #OPÇÃO DO DIA
    ctk.CTkLabel(frame_data_manual, text="Dia", font=("Roboto", 18)).grid(row=4,column=1,sticky="w",padx=(10,0))
    menuDia = ctk.CTkOptionMenu(frame_data_manual, fg_color="#080D19", values=valores_dias,
    command=lambda valor:atualizarDataSelecionada(label_data,menuDia,menuMes,menuAno, data_var), button_color="#080D19", height=30,
    font=("Roboto",16), dropdown_fg_color="#080D19",dropdown_font=("Roboto",14))
    menuDia.grid(row=5,column=1,sticky="w",padx=(20,0))

    #OPÇÃO DO MÊS
    ctk.CTkLabel(frame_data_manual, text="Mês", font=("Roboto", 18)).grid(row=4,column=2,sticky="w",padx=(50,0))
    menuMes = ctk.CTkOptionMenu(frame_data_manual, fg_color="#080D19", values=valores_meses,
    command=lambda valor:atualizarDataSelecionada(label_data,menuDia,menuMes,menuAno,data_var ), button_color="#080D19", height=30,
    font=("Roboto",16), dropdown_fg_color="#080D19",dropdown_font=("Roboto",14))
    menuMes.grid(row=5,column=2,sticky="w",padx=(60,0))

    #OPÇAO DO DIA
    ctk.CTkLabel(frame_data_manual, text="Ano", font=("Roboto", 18)).grid(row=4,column=3,sticky="w", padx=(50,0))
    menuAno = ctk.CTkOptionMenu(frame_data_manual, fg_color="#080D19", values=valores_anos,
    command=lambda valor:atualizarDataSelecionada(label_data,menuDia,menuMes,menuAno,data_var), button_color="#080D19",
    height=30, font=("Roboto",16), dropdown_fg_color="#080D19",dropdown_font=("Roboto",14))
    menuAno.grid(row=5,column=3,sticky="w",padx=(60,0))

    dicionarioDataFrame = {'Dia':menuDia, 'Mes':menuMes, 'Ano':menuAno, 'Frame':frame_data_manual}

    return dicionarioDataFrame

def atualizarDataSelecionada(label_data, menuDia, menuMes, menuAno, data_var):
    dia = menuDia.get()
    mes = menuMes.get()
    ano = menuAno.get()

    dicionarioMes = {
        'Janeiro': '01',
        'Fevereiro': '02',
        'Março': '03',
        'Abril': '04',
        'Maio': '05',
        'Junho': '06',
        'Julho': '07',
        'Agosto': '08',
        'Setembro': '09',
        'Outubro': '10',
        'Novembro': '11',
        'Dezembro': '12'
    }

    label_data.configure(text=f"Data Selecionada: {dia}/{dicionarioMes[mes]}/{ano} ")
    data = f"{dia}/{dicionarioMes[mes]}/{ano}"
    data_var.set(data)
    return data






