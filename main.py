# ler a parte de downloads do usuário e listar os arquivos presentes no diretório. colocar em uma lista e classificar os arquivos por tipo (imagens, documentos, vídeos, etc.). assim organizar automaticamente os arquivos em pastas separadas de acordo com o tipo de arquivo.
from pathlib import Path
import shutil

Downloads = Path.home() / 'Downloads'
Documents = Path.home() / 'Documents'

for arquivo in Downloads.iterdir():
    #if arquivo.is_file():
    print(arquivo.name)
    print(arquivo.suffix)

