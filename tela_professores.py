import customtkinter as ctk
from PIL import Image

from componentes.objetosConteiner import limpar_tela
from componentes.conteinersTelaCadastro import linhaDivisoria
from database import (
    listar_professores,
    listar_disciplinas,
    buscar_id_usuario
)
from funcoes_cadastro_visual import janelaDeCadastroDisciplina

CORES_ANEL = ["#8B5CF6", "#38BDF8", "#10B981", "#F43F5E", "#A855F7"]


def criar_header_professores(quadro_central):
    """Cria o cabeçalho padronizado seguindo a exata identidade visual das outras telas (45px título, 20px subtítulo, 100x100 ícone)."""
    quadro_header = ctk.CTkFrame(quadro_central, width=1500, height=150, fg_color="transparent")
    quadro_header.pack(fill="x", pady=(10, 0), padx=2)

    # Imagem 100x100 padronizada do cabeçalho
    try:
        img = ctk.CTkImage(
            light_image=Image.open("imagens/iconeVisualizarProfessores.png"),
            dark_image=Image.open("imagens/iconeVisualizarProfessores.png"),
            size=(100, 100)
        )
        label_img = ctk.CTkLabel(quadro_header, text="", image=img)
        label_img.pack(side="left", padx=(10, 0), pady=(10, 0))
    except Exception:
        pass

    # Frame de Textos
    frame_texto = ctk.CTkFrame(quadro_header, fg_color="transparent")
    frame_texto.pack(side="left", padx=(25, 0))

    ctk.CTkLabel(
        frame_texto,
        text="Professores",
        font=("Roboto", 45),
        text_color="#F8FAFC"
    ).pack(anchor="w")

    ctk.CTkLabel(
        frame_texto,
        text="Gerencie os professores cadastrados no sistema.",
        font=("Roboto", 20),
        text_color="#94A3B8"
    ).pack(anchor="w")

    return quadro_header


def visualizarProfessores(quadro_central, quadro_principal):
    limpar_tela(quadro_central)

    # -------------------------------------------------------------
    # 1. CABEÇALHO PADRONIZADO (Roboto 45 + Roboto 20 + Ícone 100x100)
    # -------------------------------------------------------------
    criar_header_professores(quadro_central)

    # -------------------------------------------------------------
    # 2. LINHA DIVISÓRIA PADRÃO DO SISTEMA (linhaCentralGrande.png)
    # -------------------------------------------------------------
    linhaDivisoria(quadro_central)

    # -------------------------------------------------------------
    # 3. ÁREA DE ROLAGEM COM A LISTA DE CARDS PADRONIZADA
    # -------------------------------------------------------------
    quadro_professores = ctk.CTkScrollableFrame(
        quadro_central,
        fg_color="transparent"
    )
    quadro_professores.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    professores = listar_professores()

    # Ícone do Usuário para o Avatar interno
    img_usuario = ctk.CTkImage(
        light_image=Image.open("imagens/iconeUsuario.png"),
        dark_image=Image.open("imagens/iconeUsuario.png"),
        size=(30, 30)
    )

    if not professores:
        ctk.CTkLabel(
            quadro_professores,
            text="Nenhum professor encontrado.",
            font=("Roboto", 18),
            text_color="#94A3B8"
        ).pack(pady=40)
        return

    # Renderização da Lista de Cards
    for index, professor in enumerate(professores):
        id_usuario = buscar_id_usuario(professor)
        disciplinas = listar_disciplinas(id_usuario) if id_usuario else []
        cor_anel = CORES_ANEL[index % len(CORES_ANEL)]

        # CARD HORIZONTAL (LINHA COMPLETA)
        card = ctk.CTkFrame(
            quadro_professores,
            fg_color="#0D1630",
            corner_radius=16,
            border_width=1.5,
            border_color="#1E2B4D"
        )
        card.pack(fill="x", padx=10, pady=10)

        # 1. BLOCO DA ESQUERDA: Avatar com Anel Neon + Nome
        frame_perfil = ctk.CTkFrame(card, fg_color="transparent")
        frame_perfil.pack(side="left", padx=(20, 30), pady=16)

        # Anel circular colorido
        frame_avatar = ctk.CTkFrame(
            frame_perfil,
            width=54,
            height=54,
            corner_radius=27,
            border_width=2,
            border_color=cor_anel,
            fg_color="#16203B"
        )
        frame_avatar.pack(side="left", padx=(0, 16))
        frame_avatar.pack_propagate(False)

        lbl_avatar = ctk.CTkLabel(frame_avatar, image=img_usuario, text="")
        lbl_avatar.place(relx=0.5, rely=0.5, anchor="center")

        # Textos: "Professor" + Nome
        frame_texto_prof = ctk.CTkFrame(frame_perfil, fg_color="transparent")
        frame_texto_prof.pack(side="left")

        ctk.CTkLabel(
            frame_texto_prof,
            text="Professor",
            font=("Roboto", 13),
            text_color="#94A3B8"
        ).pack(anchor="w")

        ctk.CTkLabel(
            frame_texto_prof,
            text=professor,
            font=("Roboto", 20, "bold"),
            text_color="#FFFFFF"
        ).pack(anchor="w")

        # 2. BLOCO DO MEIO: 📖 Disciplinas com Tags / Badges
        frame_disciplinas = ctk.CTkFrame(card, fg_color="transparent")
        frame_disciplinas.pack(side="left", fill="both", expand=True, padx=(10, 20), pady=16)

        ctk.CTkLabel(
            frame_disciplinas,
            text=" Disciplinas",
            font=("Roboto", 14, "bold"),
            text_color="#818CF8"
        ).pack(anchor="w")

        frame_tags = ctk.CTkFrame(frame_disciplinas, fg_color="transparent")
        frame_tags.pack(anchor="w", pady=(6, 0))

        if disciplinas:
            for disc in disciplinas:
                pill = ctk.CTkLabel(
                    frame_tags,
                    text=disc,
                    font=("Roboto", 13, "bold"),
                    text_color="#93C5FD",
                    fg_color="#172554",
                    corner_radius=12,
                    padx=14,
                    pady=5
                )
                pill.pack(side="left", padx=(0, 10))
        else:
            ctk.CTkLabel(
                frame_tags,
                text="Nenhuma disciplina cadastrada",
                font=("Roboto", 13),
                text_color="#64748B"
            ).pack(side="left")

        # 3. BLOCO DA DIREITA: Botão "+ Cadastrar Disciplina"
        frame_acao = ctk.CTkFrame(card, fg_color="transparent")
        frame_acao.pack(side="right", padx=(0, 24), pady=16)

        def ao_cadastrar_disciplina(id_user, prof):
            if janelaDeCadastroDisciplina(id_user, prof):
                visualizarProfessores(quadro_central, quadro_principal)

        btn_cadastrar = ctk.CTkButton(
            frame_acao,
            text="+ Cadastrar Disciplina",
            font=("Roboto", 13, "bold"),
            height=40,
            corner_radius=8,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            text_color="#FFFFFF",
            command=lambda id_u=id_usuario, prof=professor: ao_cadastrar_disciplina(id_u, prof)
        )
        btn_cadastrar.pack(side="right")


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1100x700")
    app.title("Gerador de Relatórios - Professores")

    quadro = ctk.CTkFrame(app, fg_color="#151B2E")
    quadro.pack(fill="both", expand=True)

    visualizarProfessores(quadro, app)
    app.mainloop()
