import customtkinter as ctk
from PIL import Image



#NESSE ARQUIVO ESTÃO OS ELEMENTOS DO MENU PRINCIPAL

#ARÉA PRINCIPAL
def criar_quadroPrincipal(janela):
    quadro_principal = ctk.CTkFrame(janela, fg_color="#151B2E", corner_radius=12)
    quadro_principal.pack(side="right", fill="both",expand=True, padx=20,pady=20)

    return quadro_principal

def criar_quadroCentral(quadro_principal):
   quadro_central =  ctk.CTkFrame(quadro_principal, fg_color="transparent")
   quadro_central.pack(fill="both", expand=True,pady=3,padx=3)

   return quadro_central # preciso de lembrar de retornar os frames

#AREA LATERAL
def frame_lateral(janela):
    quadro_lateral = ctk.CTkFrame(janela, width=330, fg_color="#0F172A", corner_radius=12)
    quadro_lateral.pack(side="left", padx=20, pady=20, fill="y")  # side para deixar na lateral esquerda
    # os pads para separar da margem da janela e fill para que ele preencha todo o espaço da vertical
    return quadro_lateral

#SESSÃO DE BOAS VINDAS
def criar_sessaoBoasvindas(quadro_central):
    frame_boasVindas = ctk.CTkFrame(quadro_central, fg_color="transparent")

    frame_boasVindas.place(relx=0.5, rely=0.5, anchor="center")


    iconeBoasVindas = ctk.CTkImage(light_image=Image.open("imagens/iconeBoasVindas.png"), dark_image=Image.open(
        "imagens/iconeBoasVindas.png"), size=(120, 120))# label que ira receber o icone boas vindas

    ctk.CTkLabel(frame_boasVindas, image=iconeBoasVindas, text="", fg_color="transparent").pack()

    ctk.CTkLabel(frame_boasVindas, text="Bem Vindo!", font=("roboto bold", 34), text_color="#F8FAFC").pack(pady=15)#MENSAGEM1

    ctk.CTkLabel(frame_boasVindas, text="Selecione uma das opções do menu ao lado para começar.", font=("roboto", 18),
                 text_color="#CBD5E1").pack() # MENSAGEM2

def criar_frameMenu(quadro_lateral):
    frame_menu = ctk.CTkFrame(
        quadro_lateral,
        fg_color="transparent"
    )

    frame_menu.pack(
        fill="both",
        expand=True,
        pady=(10,0)
    )

    return frame_menu



#CABEÇALHO
def cabecalho(quadro_lateral):
    img_Label = ctk.CTkImage(light_image=Image.open("imagens/iconeMenu.png"),#ICONE DO CABEÇALHO
                                 dark_image=Image.open("imagens/iconeMenu.png"),
                                 size=(100,80))
    cabecalho = ctk.CTkFrame(
        quadro_lateral,
        fg_color="transparent",
        height=105
    )

    cabecalho.pack(
        padx=15,
        pady=(10, 5),
        fill="x"
    )

    cabecalho.pack_propagate(False)

    labelIconeMenu = ctk.CTkLabel(
        cabecalho,
        image=img_Label,
        text="",

    )

    labelIconeMenu.pack(
        side="left",
        padx=(0, 12)
    )
    titulo_menuLateral = ctk.CTkLabel(#TITULO DO CABEÇALHO
        cabecalho,
        text="Gerador de\nRelatórios",
        text_color="#F8FAFC",
        font=("Roboto", 20, "bold"),
        justify="left",
        anchor="w"
    )

    titulo_menuLateral.pack(side="left")
    labelMenu = ctk.CTkLabel(quadro_lateral, text="MENU", font=("Roboto", 12), text_color="#94A3B8", anchor="w")
    labelMenu.pack(fill="x", padx=10, pady=(5, 8))

#SESSÃO DO USUÁRIO
def criar_quadroUsuario(quadro_lateral):
    quadro_usuario = ctk.CTkFrame(
        quadro_lateral,
        height=148,
        fg_color="#162032",
        corner_radius=12,
        border_width=1,
        border_color="#334155"
    )
    quadro_usuario.pack(fill="x", padx=15, pady=(0, 15), side="bottom")
    quadro_usuario.pack_propagate(False)

    return quadro_usuario


def criar_menuDisciplinas(quadroUsuario, disciplinas, disciplina_var):
    # Rótulo de contexto para dar acabamento profissional
    label_contexto = ctk.CTkLabel(
        quadroUsuario,
        text="DISCIPLINA ATIVA",
        font=("Roboto", 10, "bold"),
        text_color="#64748B",
        anchor="w"
    )
    label_contexto.place(x=16, y=68)

    menu = ctk.CTkComboBox(
        quadroUsuario,
        fg_color="#0B1322",
        button_color="#1E293B",
        button_hover_color="#2D3E5F",
        dropdown_fg_color="#0F172A",
        dropdown_hover_color="#1E293B",
        dropdown_text_color="#F8FAFC",
        font=("Roboto", 12, "bold"),
        dropdown_font=("Roboto", 12),
        corner_radius=8,
        width=200,
        height=36,
        variable=disciplina_var,
        values=disciplinas if disciplinas else ["Nenhuma disciplina"],
        state="readonly",
        border_width=1,
        border_color="white"
    )
    menu.place(x=16, y=94)
    return menu


def criar_labelTitulolUsuario(quadro_usuario):
    labelTituloUsuario = ctk.CTkLabel(
        quadro_usuario,
        text="PROFESSOR",
        font=("Roboto", 10, "bold"),
        text_color="#64748B",
        anchor="w"
    )
    labelTituloUsuario.place(x=70, y=14)


def criar_labelUsuario(quadro_usuario, usuario):
    labelUsuario = ctk.CTkLabel(
        quadro_usuario,
        text=usuario,
        font=("Roboto", 16, "bold"),
        text_color="#F8FAFC",
        anchor="w"
    )
    labelUsuario.place(x=70, y=30)


def criar_imagemUsuario(quadro_usuario):
    img_usuario = ctk.CTkImage(
        light_image=Image.open("imagens/imagemUsuariopng.png"),
        dark_image=Image.open("imagens/imagemUsuariopng.png"),
        size=(44, 44)
    )
    img_usuarioLabel = ctk.CTkLabel(quadro_usuario, image=img_usuario, text="")
    img_usuarioLabel.place(x=15, y=13)


def logOut(quadro_principal, quadro_lateral, login, janela):
    quadro_principal.destroy()
    quadro_lateral.destroy()
    login(janela)


def criar_btnLogOut(quadro_usuario, quadro_principal, quadro_lateral, login, janela):
    logOutimg = ctk.CTkImage(
        light_image=Image.open("imagens/botaoLogOut.png"),
        dark_image=Image.open("imagens/botaoLogOut.png"),
        size=(34, 34)
    )
    btnLogOut = ctk.CTkButton(
        quadro_usuario,
        width=36,
        height=36,
        fg_color="#1E293B",
        hover_color="#334155",
        border_width=1,
        border_color="#334155",
        corner_radius=8,
        image=logOutimg,
        text="",
        command=lambda: logOut(quadro_principal, quadro_lateral, login, janela)
    )
    btnLogOut.place(x=246, y=14)


def limpar_tela(frame):
  # Remove todos os elementos filhos de dentro do frame
  for widget in frame.winfo_children():
    widget.destroy()

