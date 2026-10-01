from tkinter import messagebox
import sqlite3
import hashlib
#CRIA O BANCO. NO SQLITE NÃO PRECISAMOS DE CREATE DATABASE
conexao = sqlite3.connect("sistemaRelatorios.db")
#cria o cursor para rodar os comandos sql
cursor = conexao.cursor()#ESSE CURSOR É PARA SIMULAR O CURSOR DO PROMPT DO SQLITE, TIPO UM TERMINAL?

#AQUI ESTÁ SENDO CRIADA A TABELA COM USUARIO E SENHA
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    caminho_pasta TEXT
);
""")

conexao.commit()




def cadastrarProfessor(usuario, senha, caminho_pasta=None):
    try:
        #CRIPTOGRAFANDO A SENHA
        senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

        #1 ABRE A CONEXÃO COM O BANCO
        conexao = sqlite3.connect("sistemaRelatorios.db")
        #2 CRIA O CURSOR QUE VAI SE COMUNICAR COM O BANCO
        cursor = conexao.cursor()
        #3 INSERE OS DADOS
        cursor.execute("""
            INSERT INTO usuarios (usuario, senha, caminho_pasta) VALUES(?,?, ?);
                    """,(usuario,senha_hash,caminho_pasta))
        #4 SALVA AS ALTERAÇÕES
        conexao.commit()
        messagebox.showinfo("Confirmação de cadastro", "Usuário Cadastrado com sucesso!")
        return True

    except sqlite3.IntegrityError:
        #Se o usuário já existir ele fecha a conexão
        messagebox.showwarning("Erro no cadastro", "Usuário já cadastrado")
        return False
    finally:
        conexao.close()#EVITA QUE A CONEXÃO FIQUE ABERTA



def atualizar_caminho_pasta(usuario, novo_caminho):
    try:
        conexao = sqlite3.connect("sistemaRelatorios.db")
        cursor= conexao.cursor()

        #ATUALIZA A COLUNA caminho_pasta
        cursor.execute("""
            UPDATE usuarios
            SET caminho_pasta = ?
            WHERE usuario = ?
        """,(novo_caminho,usuario))

        conexao.commit()


    except sqlite3.Error as Erro:
        print(f"Não foi possível atualizar o caminho. Erro: {Erro}")

    finally:
        conexao.close()

def verificar_login(usuario, senha):
    try:

        senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

        conexao = sqlite3.connect("sistemaRelatorios.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM usuarios
            WHERE usuario = ? AND senha = ?;
            
        """, (usuario, senha_hash))


        resultado = cursor.fetchone()
        if resultado != None:
            print("Conexão Autenticada com Sucesso")
            return True
        else:
            print("Credenciais incorretas.")
            return False

    except Exception as Erro:
        print(f"Não foi possível concluir a operação. Erro:{Erro}")
        return False

    finally:
        conexao.close()


