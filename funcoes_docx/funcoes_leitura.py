import os
from constantes import MODELO_PCM, MODELO_JUVENTUDE

def buscarRelatorios(usuario):#Pega o nome dos relatórios presentes na pasta do professor

    pasta_professor = os.path.join("Professores", usuario)

    arquivos = os.listdir(pasta_professor)

    templates = []

    for arquivo in arquivos:
        if "Relatorio PCM.docx" in arquivo or "Relatorio Juventude.docx" in arquivo:
            txt = os.path.splitext(arquivo)[0]
            templates.append(txt)



    return templates


def buscarDatas(usuario, modelo):
    pastaJuventude = os.path.join("Professores",usuario, "backupJuventude")
    pastaPCM = os.path.join("Professores",usuario, "backupPCM")

    if modelo == MODELO_PCM:
        arquivos = os.listdir(pastaPCM)
    elif modelo == MODELO_JUVENTUDE:
        arquivos = os.listdir(pastaJuventude)

    datas = []
    datas_formatadas = []

    for arquivo in arquivos:
        nome_arquivo = os.path.splitext(arquivo)[0]
        data_bruta = nome_arquivo[-10:]
        dataFormatada = data_bruta.replace("-","/")
        datas.append(data_bruta)
        datas_formatadas.append(dataFormatada)

    dicionarioDatas = {"datasFormatadas": datas_formatadas,"datas": datas}
    return dicionarioDatas

