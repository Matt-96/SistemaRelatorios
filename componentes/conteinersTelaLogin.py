import customtkinter as ctk
from PIL import Image

#SESSÃO LOGIN ----- FRAME + LABEL DO TITULO
def criar_quadroLogin(janela):
    quadroLogin = ctk.CTkFrame(janela, #QUADRO LOGIN
                               width=400,
                               height=630,
                               fg_color="#0F162E",
                               corner_radius=16,
                               border_width=1,
                               border_color="#087CFF"
                               )
    quadroLogin.pack_propagate(False)
    quadroLogin.place(relx=0.5, rely=0.5, anchor="center")

    return quadroLogin


def criar_labelLogin(quadroLogin):
    iconeLogin = ctk.CTkImage(light_image=Image.open("imagens/iconeBoasVindas.png"),
                              dark_image=Image.open("imagens/IconeBoasVindas.png"),
                              size=(100,100))

    label_login = ctk.CTkLabel(quadroLogin, image= iconeLogin, text="") #ICONE LOGIN
    label_login.pack(pady=(40,10))

    return label_login

def criar_labelLoginTitulo(quadroLogin):
    label_tituloLogin = ctk.CTkLabel(quadroLogin,text="Gerador de \nRelatórios", font=("Inter bold",30), text_color="#F1EFF0")
    label_tituloLogin.pack()

    return label_tituloLogin

def criar_linhaCentral(quadroLogin):
    img_linha = ctk.CTkImage(light_image=Image.open("imagens/linhaCentral.png"), dark_image=Image.open(
        "imagens/linhaCentral.png"),size=(150,40))
    labelLinha = ctk.CTkLabel(quadroLogin,text="",image=img_linha)
    labelLinha.pack()
    return labelLinha

def criar_txtCentral(quadroLogin):
    txtCentral = ctk.CTkLabel(quadroLogin,text="Entre com suas credenciais \npara acessar o sistema", text_color="grey",
                              font=("Roboto", 16))
    txtCentral.pack(pady=15)

    return txtCentral
#ENTRYS
def criar_TituloUsuario(quadroLogin):
    tituloLogin = ctk.CTkLabel(
        quadroLogin,
        text="Usuário",
        text_color="white",
        fg_color="#0F162E",
        font=("Roboto", 15)
    )

    tituloLogin.place(
        x=50,
        y=330,
        anchor="nw"

    )

    return tituloLogin

def criar_frameUsuario(quadroLogin):
    frameUsuario = ctk.CTkFrame(quadroLogin, fg_color="transparent", width=300, height=50, border_width=1,
    border_color="#334155",
    corner_radius=8)
    frameUsuario.pack_propagate(False)

    frameUsuario.pack(pady=(40,10))

    return frameUsuario

def criar_labelIconeUsuario(frameUsuario):
    iconeUsuario = ctk.CTkImage(light_image=Image.open("imagens/iconeUsuario.png"), dark_image=Image.open(
        "imagens/iconeUsuario.png"),size=(30,30))

    labelIconeUsuario = ctk.CTkLabel(frameUsuario, image=iconeUsuario,text="", fg_color="transparent")
    labelIconeUsuario.pack(side="left", padx=5)
    return labelIconeUsuario

def criar_campoUsuario(frameUsuario): # ENTRY DO USUÁRIO
    campo_usuario = ctk.CTkEntry(frameUsuario, placeholder_text="Nome de Usuário", width=205, height=30,fg_color="transparent",border_width=0)
    campo_usuario.pack(padx=(0,10),side="left")

    return campo_usuario

def criar_frameSenha(quadroLogin):
    frameSenha = ctk.CTkFrame(quadroLogin, fg_color="transparent", width=300, height=50, border_width=1,
    border_color="#334155",
    corner_radius=8)
    frameSenha.pack_propagate(False)

    frameSenha.pack(pady=(40,5))

    return frameSenha

def criar_TituloSenha(quadroLogin):
    tituloSenha = ctk.CTkLabel(
        quadroLogin,
        text="Senha",
        text_color="white",
        fg_color="#0F162E",
        font=("Roboto", 15)
    )

    tituloSenha.place(
        x=50,
        y=430,
        anchor="nw"

    )

    return tituloSenha


def alternar_senha(campo_senha):

    if campo_senha.cget("show") == "*":
        campo_senha.configure(show="")
    else:
        campo_senha.configure(show="*")


def criar_btnVisibilidadeSenha(frameSenha, campo_senha):
    iconeOlho = ctk.CTkImage(
        light_image=Image.open("imagens/iconeOlho.png"),
        dark_image=Image.open("imagens/iconeOlho.png"),
        size=(35, 35)
    )

    botaoOlho = ctk.CTkButton(
        frameSenha,
        width=35,
        height=35,
        text="",
        border_width=0,
        image=iconeOlho,
        fg_color="transparent",
        command=lambda: alternar_senha(campo_senha)
    )

    botaoOlho.pack(side="right", padx=(0, 5))

    return botaoOlho

def criar_labelIconeSenha(frameSenha):
    iconeUsuario = ctk.CTkImage(light_image=Image.open("imagens/iconeSenha.png"), dark_image=Image.open(
        "imagens/iconeSenha.png"),size=(30,30))

    labelIconeSenha = ctk.CTkLabel(frameSenha, image=iconeUsuario,text="", fg_color="transparent")
    labelIconeSenha.pack(side="left",padx=5)
    return labelIconeSenha
def criar_campoSenha(frameSenha):

    campo_senha = ctk.CTkEntry(
        frameSenha,
        placeholder_text="Senha",
        width=205,
        height=30,
        show="*",
        fg_color="transparent",
        border_width=0
    )

    campo_senha.pack(
        side="left",
        padx=5
    )

    return campo_senha

def mostrarLogin(janela):
    resultado_login = ctk.CTkLabel(janela, text="")
    resultado_login.pack(side="bottom",pady=(0,100))

    return resultado_login



