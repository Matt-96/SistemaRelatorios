import mimetypes
import os.path #PARA MANIPULAR O credential.json
from pathlib import Path

from datetime import datetime
from google.auth.transport.requests import  Request # PARA PEDIR ACESSO SEMPRE QUE UM TOKEN EXPIRAR
from google.oauth2.credentials import Credentials # PARA AUTENTICAR O USUARIO, SERIA UMA CHAVE
from google_auth_oauthlib.flow import InstalledAppFlow # CONVERTE A RESPOSTA DO GOOLE EM UM ARQUIVO DE CREDENCIAIS VALIDO
from googleapiclient.discovery import build # INSTANCIA O OBJETO CLIENTE COM TODOS OS METODOS DO GOOGLE DISPONIVEIS
from googleapiclient.http import MediaFileUpload

from caminhos import obter_caminho_arquivo
from constantes import ID_PASTA_COMPARTILHADA

# Permite ao app criar e gerenciar APENAS os arquivos que ele mesmo enviar
SCOPES = ['https://www.googleapis.com/auth/drive']

def obter_servico_drive():
    creds = None

    #1. Checa se o token.jason já existe(de um login anterior)
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES) #Nesse caso as credenciais são válidas

    #2. Caso não tenha credenciais:
    if not creds or not creds.valid:
        #2A o acesso expirou, mas temos o Refresd Token para renovar?
        if creds and creds.expired and creds.refresh_token: #temos credenciais expiradas e PODEMOS renovar
                print("Renovando tokens de acesso nos bastidores")
                creds.refresh(Request()) # aqui é feita a requisição de renovação do token
        #2B nesse caso, é o primeiro acesso. vai abrir o navegador para se logar
        else:
            print("Abrindo o navegador para acesso inicial..")
            # Instancia o objeto flow com o arquivo secreto do usuario e a URL do google drive
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            #aqui ele cria uma conexão, abrindo o site do google drive para o usuario confirmar os escopos e acessos, depois de clicar em permitir, ele envia de volta para o usuario um arquivo CREDENTIALS válido
            creds = flow.run_local_server(port=0)

            #3. Salva o novo acesso em token.json para os próximos dias
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    #4. Constrói e retorna o cliente do Goolge Drive
    service = build("drive", "v3", credentials=creds)

    return service



def obter_nome_mes(caminho_arquivo):
    MESES = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março",
        "04": "Abril", "05": "Maio", "06": "Junho",
        "07": "Julho", "08": "Agosto", "09": "Setembro",
        "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }

    caminho_arquivo = Path(caminho_arquivo)
    nomeArquivo = caminho_arquivo.name
    data = nomeArquivo.split("-")
    mes = data[1]
    mesNome = MESES[mes]

    return mesNome


def obter_ou_criar_pasta(service,nome_pasta,id_pai):
    query = (f"name = '{nome_pasta}' and '{id_pai}' in parents and mimeType = 'application/vnd.google-apps.folder' and "
             f"trashed = false")
    resposta = service.files().list(
        q=query,
        fields="files(id, name)",
        supportsAllDrives=True,
        includeItemsFromAllDrives=True).execute()

    pastas = resposta.get("files", [])

    if pastas:
        return pastas[0]["id"]
    else:
        metadados = {
            "name":nome_pasta,
            "mimeType":"application/vnd.google-apps.folder",
            "parents": [id_pai]
        }

        nova_pasta = service.files().create(
            body=metadados,
            fields="id",
            supportsAllDrives=True,
        ).execute()

        return nova_pasta.get("id")

MAPEAMENTO_PASTAS_PROJETOS = {
    "PCM": "Crescendo com Música",
    "Juventude": "Juventude",
    "São Vicente": "São Vicente"
}


def enviar_relatorio_drive(caminho_arquivo, usuario, modelo):
    service = obter_servico_drive()

    ano_atual = str(datetime.now().year)
    nome_mes = obter_nome_mes(caminho_arquivo)
    nome_pasta_projeto = MAPEAMENTO_PASTAS_PROJETOS.get(modelo, modelo)

    # PASTA DO ANO
    id_ano = obter_ou_criar_pasta(service, ano_atual, ID_PASTA_COMPARTILHADA)
    # PASTA DO PROJETO (Traduzido para o nome real da pasta no Drive)
    id_modelo = obter_ou_criar_pasta(service, nome_pasta_projeto, id_ano)
    # PASTA DO PROFESSOR
    id_professor = obter_ou_criar_pasta(service, usuario, id_modelo)
    # PASTA DO MÊS
    id_mes = obter_ou_criar_pasta(service, nome_mes, id_professor)

    midia = MediaFileUpload(
        str(caminho_arquivo),
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    metadados_arquivo = {
        "name": Path(caminho_arquivo).name,
        "parents": [id_mes]
    }

    arquivo_enviado = service.files().create(
        body=metadados_arquivo,
        media_body=midia,
        fields="id",
        supportsAllDrives=True
    ).execute()

    return nome_mes, nome_pasta_projeto
