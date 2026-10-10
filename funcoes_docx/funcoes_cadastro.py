from dataclasses import replace
from tkinter import simpledialog, filedialog, messagebox

import docx
import customtkinter as ctk
from datetime import date
import os
from docx.shared import Inches
import shutil

from caminhos import obter_caminho_template
from config import BASE_DIR
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

    if modelo_var.get() == "PCM":
        frameTurmas.grid(row=4,padx=(20, 0))
    else:
        frameTurmas.grid_remove()




def carregarTemplate(usuario, modelo_var,data, disciplina):
    #Define a pasta de destino do professor
    pasta_raiz = os.path.dirname(os.path.dirname(__file__))  # Ajusta a pasta raiz
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)


    #PEGA O NOME DO MODELO
    modelo = modelo_var.get()
    dataFormatada = data.replace("/", "-")
    #PEGA OS TEMPLATES
    caminhoMatriz = obter_caminho_template(usuario, disciplina, modelo)

    pasta_backup = os.path.join(pasta_professor, disciplina, f"backup{modelo}")
    os.makedirs(pasta_backup, exist_ok=True)

    # ACESSA OS ARQUIVOS PREENCHIDOS
    caminhoBackup = os.path.join(pasta_backup,f"Relatorio{modelo}{disciplina}{dataFormatada}.docx")

    if os.path.exists(caminhoBackup):
        doc = docx.Document(caminhoBackup)
        nomeArquivo = f"Relatorio {modelo}{disciplina}{dataFormatada}"
    else:
        doc = docx.Document(caminhoMatriz)
        doc.save(caminhoBackup)
        nomeArquivo = f"Relatorio{modelo} {disciplina}{dataFormatada}"

        print("CAMINHO BACKUP:", caminhoBackup)

    return doc, nomeArquivo, caminhoBackup




def escreverConteudo(usuario, modelo_var, caixaDeTexto,  data_var, turmas, disciplina):
    doc, nomeArquivo, caminhoBackup = carregarTemplate(usuario, modelo_var, data_var, disciplina)

    conteudo = caixaDeTexto.get("1.0", "end")  # CAPTURA O TEXTO

    caminho_assinatura = buscar_caminho_assinatura(usuario)




    if not caminho_assinatura:
        messagebox.showwarning("Assinatura Ausente",
                               "Por favor, insira uma assinatura antes de cadastrar o relatório")
        return




    inserirData(doc,data_var, caminhoBackup)
    inserirAssinatura(doc, caminho_assinatura, usuario)

    try:
        if modelo_var.get() == "Juventude":

            escreverJuventude(doc,conteudo)

            doc.save(caminhoBackup)

        else:

            escreverPCM(doc, conteudo, turmas)
            doc.save(caminhoBackup)


        messagebox.showinfo(title="Sucesso",message="Conteúdo cadastrado com sucesso!")

    except Exception as Erro:
        messagebox.showwarning(title="Erro", message=f"Erro: {Erro}")

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


def criar_pasta_professor(usuario):
    pasta_raiz = os.path.dirname(os.path.dirname(__file__))  # Ajusta a pasta raiz
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)

    os.makedirs(pasta_professor,exist_ok=True)

    return pasta_professor

def criar_pasta_disciplina(usuario,disciplina):
    pasta_raiz = BASE_DIR
    pasta_professor = os.path.join(pasta_raiz, "Professores", usuario)
    pasta_disciplina = os.path.join(pasta_professor,disciplina)

    os.makedirs(pasta_disciplina, exist_ok=True)

