import os
from constantes import MODELO_PCM, MODELO_JUVENTUDE


def buscarDatas(usuario, modelo,disciplina):
    pastaJuventude = os.path.join("Professores",usuario,disciplina, "backupJuventude")
    pastaPCM = os.path.join("Professores",usuario, disciplina,"backupPCM")

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

