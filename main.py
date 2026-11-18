from pathlib import Path
import shutil

from classifier import classificar_arquivo


Downloads = Path.home() / 'Downloads'

for arquivo in Downloads.iterdir():
    if arquivo.is_file():
        print(f"Nome: {arquivo.name}, Sufixo: {arquivo.suffix}")
        categoria = classificar_arquivo(arquivo)
        print(f"Categoria: {categoria}")