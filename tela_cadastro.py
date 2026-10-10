import customtkinter as ctk
from PIL import Image
from componentes.botoes import criar_btnPersonalizado
from componentes.conteinersTelaCadastro import  linhaDivisoria, criarCaixaConteudo, \
    labelModeloRelatorio, labelConteudo, criarQuadroData, criar_frameTextos, \
    criar_frameInformacoes, criar_frameModelo, criar_frameTxtBox, criar_frameTurmas
from componentes.objetosConteiner import  limpar_tela
from componentes.conteinersTelaCadastro import criarHeader
from database import buscar_id_usuario, buscar_id_disciplina, listar_modelos
from funcoes_docx.funcoes_cadastro import escreverConteudo, carregarTemplate, mostraTurmasPCM
from constantes import MODELO_PCM

def cadastrarConteudo(quadro_central, disciplina, usuario):

    limpar_tela(quadro_central)

    nome_disciplina = disciplina.get()

    #PEGA DADOS DO BANCO DE DADOS
    id_usuario = buscar_id_usuario(usuario)
    id_disciplina = buscar_id_disciplina(id_usuario,nome_disciplina)
    modelos = listar_modelos(id_disciplina)

    #HEADER
    quadroHeader = criarHeader(quadro_central)
    linhaDivisoria(quadro_central)

    #FRAME TEXTO
    frameTexto = criar_frameTextos(quadroHeader)

    # FRAME INFORMACOES
    frameInformacoes = criar_frameInformacoes(quadro_central)


    #AREA DE SELEÇÃO DO MODELO DE TEMPLATE
    frameModelo = criar_frameModelo(frameInformacoes)
    #AREA DE SELEÇAO DE DATA
    switch, dicionario, data_var = criarQuadroData(frameInformacoes)



    #CAIXA CONTEÚDO
    labelModeloRelatorio(frameModelo)#TITULO ESCOLHA DE MODELO DO RELATÓRIO
    #VARIAVEL QUE IRÁ CONTROLAR OS BOTÕES DE RADIO
    modelo_var = ctk.StringVar(value="")

    # AREA DE SELEÇÃO TURMAS PCM

    frameTurmas, menuOpcoes = criar_frameTurmas(frameModelo, usuario,nome_disciplina, MODELO_PCM)





    txtBox = criar_frameTxtBox(quadro_central)
    labelConteudo(txtBox)
    caixaDeTexto = criarCaixaConteudo(txtBox) # CRIAR O CAMPO DE INPUT PARA O USUÁRIO
    #BOTAO CADASTRAR
    img = ctk.CTkImage(light_image=Image.open("imagens/cadastroBranco.png"),dark_image=Image.open("imagens/cadastroBranco.png"), size=(40,30))
    botaoCadastrar =  criar_btnPersonalizado(txtBox, text="Cadastrar", font=("Roboto",25), fg_color="#4124CC",
                                             height=55, corner_radius=12, border_color="white",
                                             border_width=1, image=img,state="disabled", command=lambda :(carregarTemplate(usuario,modelo_var,data_var.get(),nome_disciplina),escreverConteudo(usuario,
                                                                                                          modelo_var,
                                                                                                          caixaDeTexto,
                                                                                                          data_var.get(),
                                                                                                          menuOpcoes,

                                                                                                          nome_disciplina)))
    botaoCadastrar.pack(side="bottom",fill="both",padx=20)


    def ativaBtn_cadastro():
        botaoCadastrar.configure(state="normal")


    # BOTOES DE RADIO
    if not modelos:
        ctk.CTkLabel(frameModelo, text="Nenhum projeto cadastrado", font=("Roboto", 16),
                     text_color="#94A3B8").grid(row=1, column=0, sticky="nw", padx=(20, 0))
        frameTurmas.configure(frameTurmas.grid_forget())
        botaoCadastrar.configure(state="disabled")

    else:
        cont = 0
        for modelo in modelos:
            ctk.CTkRadioButton(frameModelo, text=modelo, font=("Roboto", 18), value=modelo,
                                            variable=modelo_var,
                                            command=lambda: (mostraTurmasPCM(usuario, modelo_var, frameTurmas),ativaBtn_cadastro())).grid(
                row=cont + 1, column=0, sticky="nw", pady=(0, 10), padx=(20, 0))

            cont += 1



