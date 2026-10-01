from dataclasses import replace
from tkinter import simpledialog, filedialog, messagebox

import docx
import customtkinter as ctk
from datetime import date
import os
from docx.shared import Inches
import shutil

from database import cadastrarProfessor, atualizar_caminho_pasta


def selecionarData(switch,dicionario):
    if switch.get() == 1: # SE ESTIVER LIGADO ELE PEGA A DATA AUTOMATICAMENTE
        data = date.today().strftime("%d/%m/%Y")


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

        dia = dicionario['Dia'].get()
        mes_selecionado = dicionario['Mes'].get()
        ano = dicionario['Ano'].get()

        mes = dicionarioMes[mes_selecionado]

        data = f"{int(dia):02d}/{mes}/{ano}"

    return data


# Carregando o arquivo de template de acordo com o nome do usuario e template selecionado na tela de cadastro
def mostraTurmasPCM(usuario, modelo_var, frameTurmas):
    if usuario == "Matheus":

        if modelo_var.get() == "Juventude":
            frameTurmas.grid_remove()
        elif modelo_var.get() == "PCM":
            frameTurmas.grid(row=4,padx=(20, 0))





def carregarTemplate(usuario, modelo_var,data):
    #Define a pasta de destino do professor
    pasta_raiz = os.path.dirname(os.path.dirname(__file__))  # Ajusta a pasta raiz
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)

    if usuario == "Matheus":

        if modelo_var.get() == "Juventude":
            dataFormatada = data.replace("/", "-")
            caminhoBackup = os.path.join(pasta_professor,"backupJuventude",f"RelatorioJuventudeVioloncelo{dataFormatada}.docx")
            caminhoMatriz = os.path.join(pasta_professor,"Relatorio Juventude.docx")
            if os.path.exists(caminhoBackup):
                doc = docx.Document(caminhoBackup)
                nomeArquivo = f"RelatorioJuventudeVioloncelo{dataFormatada}"
            else:
                doc = docx.Document(caminhoMatriz)
                doc.save(caminhoBackup)
                nomeArquivo = f"RelatorioJuventudeVioloncelo{dataFormatada}"

        elif modelo_var.get() == "PCM":
            dataFormatada = data.replace("/", "-")
            caminhoBackup = os.path.join(pasta_professor,"backupPCM",f"RelatorioPCMVioloncelo{dataFormatada}.docx")
            caminhoMatriz = os.path.join(pasta_professor, "Relatorio PCM.docx")
            print("CAMINHO BACKUP:", caminhoBackup)
            if os.path.exists(caminhoBackup):
                doc = docx.Document(caminhoBackup)
                nomeArquivo = rf"RelatorioPCMVioloncelo{dataFormatada}"
            else:
                doc = docx.Document(caminhoMatriz)
                doc.save(caminhoBackup)
                nomeArquivo = f"RelatorioPCMVioloncelo{dataFormatada}"
    return doc, nomeArquivo, caminhoBackup




def escreverConteudo(usuario, modelo_var, caixaDeTexto,  data_var, turmas):
    doc, nomeArquivo, caminhoBackup = carregarTemplate(usuario, modelo_var, data_var)

    conteudo = caixaDeTexto.get("1.0", "end")  # CAPTURA O TEXTO

    caminho_assinatura = buscar_caminho_assinatura(usuario)

    if not caminho_assinatura:
        messagebox.showwarning("Assinatura Ausente",
                               "Por favor, insira uma assinatura antes de cadastrar o relatório")
        return
    inserirData(doc,data_var, caminhoBackup)
    inserirAssinatura(doc, caminho_assinatura, usuario)
    data = data_var
    data_formatada = data.replace('/', '-')
    if nomeArquivo == f"RelatorioJuventudeVioloncelo{data_formatada}":
        escreverJuventude(doc,conteudo)

        doc.save(caminhoBackup)

    else:

        print("VOU SALVAR EM:")
        print(caminhoBackup)

        escreverPCM(doc, conteudo, turmas)
        doc.save(caminhoBackup)

def escreverJuventude(doc,conteudo):
    # LAÇO PARA LER AS LINHAS DO TEMPLATE
    for tabela in doc.tables:  # DOCUMENTO
        for linha in tabela.rows:  # TABELA
            for paragrafo in linha.cells[0].paragraphs:  # LINHA
                if "PRÁTICA DE CONJUNTO" in paragrafo.text:
                    for p in linha.cells[1].paragraphs:  # TEXTO
                        p.text = conteudo
                        break



def extrair_turmasPCM(doc):
    turmas = []
    # LAÇO PARA LER AS LINHAS DO TEMPLATE
    for tabela in doc.tables:  # DOCUMENTO
        for linha in tabela.rows:  # TABELA
            for celula in linha.cells:
                for paragrafo in celula.paragraphs:
                    if "TURMA" in paragrafo.text:
                        turmas.append(paragrafo.text)
    return turmas

def escolheTurma(menuOpcoes):
    escolha = menuOpcoes.get()

    return escolha

def escreverPCM(doc,conteudo, turma):
    escolha = escolheTurma(turma)
    # LAÇO PARA LER AS LINHAS DO TEMPLATE
    for tabela in doc.tables:  # DOCUMENTO
        for linha in tabela.rows:  # TABELA
            for paragrafo in linha.cells[0].paragraphs:
                if paragrafo.text in escolha:
                    for p in linha.cells[1].paragraphs:  # TEXTO
                            p.text = conteudo
                            break

def inserirData(doc,data_var, caminhoBackup):
    #LAÇO PARA LER AS LINHAS DO TEMPLATE
    for tabela in doc.tables:
        for linha in tabela.rows:
            for celula in linha.cells:
                for paragrafo in celula.paragraphs:
                    if "DATA:" in paragrafo.text:
                        paragrafo.text =  paragrafo.text.replace("DATA:   /    /", f"DATA:{data_var}")
    doc.save(caminhoBackup)


def inserirAssinatura(doc, nome_arquivo_imagem, usuario):
    # 1. Pega a pasta onde está o funcoes_cadastro.py (.../funcoes_docx)
    pasta_funcoes = os.path.dirname(__file__)

    # 2. Sobe para a pasta raiz do projeto (.../SistemaRelatorios)
    pasta_raiz = os.path.dirname(pasta_funcoes)

    # 3. Monta o caminho completo até a pasta Professores/NomeDoUsuario
    caminho_completo = os.path.join(pasta_raiz, "Professores", f"{usuario}", nome_arquivo_imagem)

    for paragrafo in doc.paragraphs:
        if "[ASSINATURA_AQUI]" in paragrafo.text:
            paragrafo.text = ""
            run = paragrafo.add_run()
            #ESPAÇO PARA ALINHAR PROFESSOR E ASSINATURA
            run.text = "                                                    "
            run.add_picture(caminho_completo, width=Inches(2.0))
            return

def escolher_e_salvar_assinatura(usuario):
    caminho_imagem = filedialog.askopenfilename(title="Selecione a sua assinatura",
                                                filetypes=[("Imagens","*.png;*.jpg;*.jpeg;*.bmp;")])

    if caminho_imagem:
        print(f"Ficheiro selecionado: {caminho_imagem}")
    else:
        print("Nenhum ficheiro foi selecionado.")

    # Se o utilizador escolheu um ficheiro (não cancelou)
    if caminho_imagem:
        # 2. Define a pasta de destino do professor
        pasta_raiz = os.path.dirname(os.path.dirname(__file__))  # Ajusta a pasta raiz
        pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)

        # Cria a pasta caso ela ainda não exista
        os.makedirs(pasta_professor, exist_ok=True) #VOU UTILIZAR ESSE CÓDIGO PARA CADASTRO DE PROFESSORES

        # Define o caminho final com o nome fixo "assinatura.png"
        caminho_destino = os.path.join(pasta_professor, "assinatura.png")

        # 3. Copia a imagem selecionada para a pasta do professor
        shutil.copy(caminho_imagem, caminho_destino)

        # 4. Exibe mensagem de sucesso
        messagebox.showinfo("Sucesso", "Assinatura atualizada com sucesso!")


def buscar_caminho_assinatura(usuario):
    #Aqui estamos montando o diretorio
    pasta_funcoes = os.path.dirname(__file__)
    pasta_raiz = os.path.dirname(pasta_funcoes)
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)

    extensoes_validas = ('.png', 'jpg', 'jpeg', 'bmp')

    #VERIFICA SE A PASTA DO PROFESSOR EXISTE
    if os.path.exists(pasta_professor):
        for arquivo in os.listdir(pasta_professor):#PERCORRE A PASTA DO PROFESSOR
            if arquivo.lower().endswith(extensoes_validas):#SE TERMINAR COM UMA EXTENSÃO VÁLIDA
                return os.path.join(pasta_professor, arquivo)

    return  None

def acionar_cadastro():
    #1 PEDE O NOME DO USUARIO
    dialogo_usuario  = ctk.CTkInputDialog(title="Cadastro", text="Digite o nome do Professor:")
    usuario = dialogo_usuario.get_input()

    if not usuario: #Se o usuário não preencher nada ou clicar em cancelar
        return
    dialogo_senha = ctk.CTkInputDialog(title="Cadastro", text="Digite a senha do Professor:")
    senha = dialogo_senha.get_input()
    if not senha:
        return
    #Manda para a função de Cadastro
    sucesso = cadastrarProfessor(usuario, senha)

   #verificar se sucesso é verdadeiro ou falso
    print(bool(sucesso))
    if sucesso:
        caminho_pasta = criar_pasta_professor(usuario)
        adiciona_template(usuario,caminho_pasta)



def adiciona_template(usuario, caminho_pasta):
    #PEDE OS ARQUIVOS DE TEMPLATE
    arquivos_selecionados = filedialog.askopenfilenames(title=f"Selecione os templates para o Professor{usuario}",
                                                       filetypes=[("Arquivos Word","*.docx")])
    #SE O USUARIO NÃO SELECIONAR NEHUM ARQUIVO
    if not arquivos_selecionados:
        messagebox.showwarning("Cadastro","Nenhum Arquivo foi selecionado.")
        return False
    #ELE COPIA OS ARQUIVOS PARA PASTA DO PROFESSOR
    try:
        for arquivo in arquivos_selecionados:
            shutil.copy(arquivo,caminho_pasta)

        atualizar_caminho_pasta(usuario,caminho_pasta)
        messagebox.showinfo("Cadastro","Templates Cadastrados com Sucesso!")
        return True
    except Exception as Erro:
        messagebox.showerror("Erro", f"Falha ao copiar os arquivos: {Erro}")
        return False


def criar_pasta_professor(usuario):
    pasta_raiz = os.path.dirname(os.path.dirname(__file__))  # Ajusta a pasta raiz
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)

    os.makedirs(pasta_professor,exist_ok=True)

    return pasta_professor