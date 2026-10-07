import sqlite3
import hashlib
from unittest import result

from config import BASE_DIR


BANCO_PATH = BASE_DIR / "sistemaRelatorios.db"

def conectar_banco():
    conexao = sqlite3.connect(BANCO_PATH)
    # Ativa a checagem de chaves estrangeiras para toda conexão aberta
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao




#CRIA O BANCO. NO SQLITE NÃO PRECISAMOS DE CREATE DATABASE

def inicializar_banco():
    conexao = conectar_banco()
    #cria o cursor para rodar os comandos sql
    cursor = conexao.cursor()#ESSE CURSOR É PARA SIMULAR O CURSOR DO PROMPT DO SQLITE, TIPO UM TERMINAL?


    #AQUI ESTÁ SENDO CRIADA A TABELA COM USUARIO E SENHA
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        caminho_pasta TEXT
    );
    
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        UNIQUE(usuario_id, nome),
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        );
        
        CREATE TABLE IF NOT EXISTS configuracoes_modelo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disciplina_id INTEGER NOT NULL,
            tipo_modelo TEXT NOT NULL,
            UNIQUE(disciplina_id, tipo_modelo),
            FOREIGN KEY(disciplina_id) REFERENCES disciplinas(id)
        );
    
    """)

    conexao.commit()
    conexao.close()

def cadastrarProfessor(usuario, senha, caminho_pasta=None):
    try:
        #CRIPTOGRAFANDO A SENHA
        senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

        #1 ABRE A CONEXÃO COM O BANCO
        conexao = conectar_banco()
        #2 CRIA O CURSOR QUE VAI SE COMUNICAR COM O BANCO
        cursor = conexao.cursor()
        #3 INSERE OS DADOS
        cursor.execute("""
            INSERT INTO usuarios (usuario, senha, caminho_pasta) VALUES(?,?, ?);
                    """,(usuario,senha_hash,caminho_pasta))
        #4 SALVA AS ALTERAÇÕES
        conexao.commit()
        return True

    except sqlite3.IntegrityError:
        #Se o usuário já existir ele fecha a conexão
        return False
    finally:
        conexao.close()#EVITA QUE A CONEXÃO FIQUE ABERTA


def listar_professores():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT usuario FROM usuarios
        
        """)


        resultado = cursor.fetchall()
        professores = [professores[0] for professores in resultado]

        return professores

    except Exception as Erro:
        print(f"Erro: {Erro}")
        return []
    finally:
        conexao.close()
        

def cadastrar_disciplina(usuario_id, nome):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO disciplinas (usuario_id, nome)
            VALUES (?,?);
        
        """,(usuario_id,nome))

        conexao.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conexao.close()


def buscar_id_usuario(usuario):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id FROM usuarios WHERE usuario = ?
        """, [usuario])

        resultado = cursor.fetchone()

        if resultado != None:
            return resultado[0]
        else:
            return None
    except Exception as Erro:
        print(f"Erro: {Erro}")
        return None

    finally:
        conexao.close()

def buscar_id_disciplina(usuario_id, nome):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
        
            SELECT id FROM disciplinas
            WHERE usuario_id = ? AND nome = ?
        """,(usuario_id,nome))

        resultado = cursor.fetchone()
        if resultado != None:
            return resultado[0]
        else:
            return None
    except Exception as Erro:
        print(f"Erro: {Erro}" )
        return None
    finally:
        conexao.close()

def listar_disciplinas(usuario_id):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT nome FROM disciplinas
            WHERE usuario_id = ?
            
        
        """,[usuario_id])

        resultado = cursor.fetchall()

        disciplinas = [disciplina[0] for disciplina in resultado]

        return disciplinas
    except Exception as Erro:
        print(f"Erro:{Erro}")
        return []
    finally:
        conexao.close()


def cadastrar_configuracao_modelo(disciplina_id,tipo_modelo):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
        
            INSERT INTO configuracoes_modelo(disciplina_id,tipo_modelo)
            values(?,?);
        """,(disciplina_id,tipo_modelo))

        conexao.commit()

        return True
    except Exception as Erro:
        print(f"ERRO!{Erro}")
        return False

    finally:
        conexao.close()


def buscar_configuracao_modelo(disciplina_id, tipo_modelo):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, disciplina_id, tipo_modelo
            FROM configuracoes_modelo 
            WHERE disciplina_id = ? AND tipo_modelo = ?
        
        """,(disciplina_id,tipo_modelo))

        resultado = cursor.fetchone()
        if resultado != None:
            return resultado

        else:
            return None

    except Exception as Erro:
        print(f"Erro: {Erro}")
        return None
    finally:
        conexao.close()


def listar_modelos(disciplina_id):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT tipo_modelo FROM configuracoes_modelo
            WHERE disciplina_id = ?
        
        """, [disciplina_id])

        resultado = cursor.fetchall()
        modelos = [modelos[0] for modelos in resultado]
        return modelos

    except Exception as Erro:
        print(f"Erro: {Erro}")
        return []
    finally:
        conexao.close()

def listar_projetos_professor(id_usuario):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT DISTINCT CM.tipo_modelo
            FROM configuracoes_modelo CM
            JOIN disciplinas D on CM.disciplina_id = D.id
            WHERE D.usuario_id = ?
                
        """,[id_usuario])

        resultado = cursor.fetchall()
        projetos = [projetos[0] for projetos in resultado]

        return projetos

    except Exception as Erro:
        print(f"Erro: {Erro}")
        return []
    finally:
        conexao.close()

def atualizar_caminho_pasta(usuario, novo_caminho):
    try:
        conexao = conectar_banco()
        cursor= conexao.cursor()

        #ATUALIZA A COLUNA caminho_pasta
        cursor.execute("""
            UPDATE usuarios
            SET caminho_pasta = ?
            WHERE usuario = ?
        """,(novo_caminho,usuario))

        conexao.commit()
        return True

    except sqlite3.Error as Erro:
        print(f"Não foi possível atualizar o caminho. Erro: {Erro}")
        return None
    finally:
        conexao.close()

def verificar_login(usuario, senha):
    try:

        senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

        conexao = conectar_banco()
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


