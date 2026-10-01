import customtkinter as ctk
from PIL import Image
from componentes.botoes import criar_btnPersonalizado
from componentes.conteinersTelaCadastro import criar_hearderImg, linhaDivisoria, criarCaixaConteudo, \
    labelModeloRelatorio, criar_btnRadio1, criar_btnRadio2, labelConteudo, criarQuadroData, criar_frameTextos, \
    criar_frameInformacoes, criar_frameModelo, criar_frameTxtBox, criar_frameTurmas
from componentes.objetosConteiner import criar_quadroCentral, criar_quadroPrincipal, limpar_tela
from componentes.conteinersTelaCadastro import criarHeader
from funcoes_docx.funcoes_cadastro import escreverConteudo, escolheTurma, carregarTemplate


def cadastrarConteudo(quadro_central, quadro_principal, usuario):

    limpar_tela(quadro_central)

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

    frameTurmas, menuOpcoes = criar_frameTurmas(frameModelo)

    #BOTOES DE RADIO
    criar_btnRadio2(frameModelo, modelo_var, usuario, frameTurmas)
    criar_btnRadio1(frameModelo, modelo_var, usuario,frameTurmas)



    txtBox = criar_frameTxtBox(quadro_central)
    labelConteudo(txtBox)
    caixaDeTexto = criarCaixaConteudo(txtBox) # CRIAR O CAMPO DE INPUT PARA O USUÁRIO
    #BOTAO CADASTRAR
    img = ctk.CTkImage(light_image=Image.open("imagens/cadastroBranco.png"),dark_image=Image.open("imagens/cadastroBranco.png"), size=(40,30))
    botaoCadastrar =  criar_btnPersonalizado(txtBox, text="Cadastrar", font=("Roboto",25), fg_color="#4124CC",
                                             height=55, corner_radius=12, border_color="white",
                                             border_width=1, image=img, command=lambda :(carregarTemplate(usuario,modelo_var,data_var.get()),escreverConteudo(usuario,
                                                                                                          modelo_var,
                                                                                                          caixaDeTexto,
                                                                                                          data_var.get(),
                                                                                                          menuOpcoes)))
    botaoCadastrar.pack(side="bottom",fill="both",padx=20)

