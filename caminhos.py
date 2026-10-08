from config import BASE_DIR
import pathlib

def obter_caminho_template(usuario,disciplina,modelo):
    nomeArquivo = f"Relatorio {modelo} {disciplina}.docx"
    caminhoTemplate = BASE_DIR / "Professores" / usuario / disciplina / nomeArquivo

    if caminhoTemplate.exists():
        return caminhoTemplate
    else:
        return  None


def obter_caminho_arquivo(usuario,disciplina,modelo,data):
    dataFormatada = data.replace("/", "-")

    nomeArquivo = f"Relatorio{modelo}{disciplina}{dataFormatada}.docx"
    caminhoArquivo = BASE_DIR / "Professores" / usuario / disciplina /f"backup{modelo}"/ nomeArquivo



    if caminhoArquivo.exists():
        return caminhoArquivo
    else:
        return  None
