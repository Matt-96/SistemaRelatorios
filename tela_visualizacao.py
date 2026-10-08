from componentes.conteiners_visualizarRelatorio import (
    criarHeader,
    linhaDivisoria,
    criar_filtros,
    tabela,
    criar_btnEnviarDrive
)
from componentes.objetosConteiner import limpar_tela
from tkinter import messagebox
from caminhos import obter_caminho_arquivo
from servico_drive import enviar_relatorio_drive

def visualizarConteudo(quadro_central, quadro_principal, usuario, disciplina_var):
    limpar_tela(quadro_central)

    disciplina = disciplina_var.get()

    # 1. BOTÃO DE ENVIO FIXO NO RODAPÉ (seguindo o padrão da tela de cadastro)
    btn_drive = criar_btnEnviarDrive(quadro_central)

    # 2. CABEÇALHO
    criarHeader(quadro_central)

    # 3. LINHA DIVISÓRIA
    linhaDivisoria(quadro_central)

    # 4. ÁREA DA TABELA ROLÁVEL (CTkScrollableFrame)
    organizaTabela, frameTabela = tabela(quadro_central)

    # 5. ÁREA DOS FILTROS (MODELO E DATA)
    menuModelo, menuData = criar_filtros(quadro_central, usuario, organizaTabela, frameTabela, disciplina)



    def acao_enviar_drive():

        # 1. Pega os valores selecionados nos menus
        modelo = menuModelo.get()
        data = menuData.get()
        # 2. Validação: O professor esqueceu de selecionar algum menu?
        if modelo == "Selecione o modelo" or data == "Selecione a data":
            messagebox.showwarning("Aviso", "Por favor, selecione o modelo e a data do relatório antes de enviar.")
            return
        # 3. Localiza o arquivo físico no computador
        caminho = obter_caminho_arquivo(usuario, disciplina, modelo, data)
        if not caminho:
            messagebox.showerror("Erro", "Arquivo do relatório não foi encontrado no computador.")
            return
        # 4. Envia para o Drive com feedback visual
        try:
            btn_drive.configure(state="disabled", text="Enviando para o Google Drive...")
            quadro_central.update()  # Força a interface a atualizar o texto do botão na hora


            nome_mes, nome_projeto = enviar_relatorio_drive(caminho, usuario, modelo)

            messagebox.showinfo(
                "Sucesso",
                f"Relatório enviado com sucesso para a pasta {nome_mes} de {nome_projeto}!"
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao enviar para o Drive: {e}")
        finally:
            btn_drive.configure(state="normal", text="Enviar para o Drive")


    btn_drive.configure(command=acao_enviar_drive)
