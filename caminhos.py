from config import BASE_DIR
import pathlib

def obter_caminho_template(usuario,disciplina,modelo):
    nomeArquivo = f"Relatorio {modelo} {disciplina}.docx"
    caminhoTemplate = BASE_DIR / "Professores" / usuario / disciplina / nomeArquivo

    if caminhoTemplate.exists():
        return caminhoTemplate
    else:
        return  None
