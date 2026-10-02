import shutil

import customtkinter as ctk
from tkinter import messagebox, filedialog
from database import cadastrarProfessor, atualizar_caminho_pasta

from funcoes_docx import funcoes_cadastro


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

    if sucesso:
        messagebox.showinfo("Confirmação de cadastro", "Usuário Cadastrado com sucesso!")
        caminho_pasta = funcoes_cadastro.criar_pasta_professor(usuario)
        adiciona_template(usuario,caminho_pasta)

    else:
        messagebox.showwarning("Erro no cadastro", "Usuário já cadastrado")

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

