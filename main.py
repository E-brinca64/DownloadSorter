from pathlib import Path

from classifier import classificar_arquivo
from organizer import organizar_arquivo


Downloads = Path.home() / 'Downloads'

dry_run = True  # Mude para False para mover os arquivos

for arquivo in Downloads.iterdir():
    if arquivo.is_file():
        categoria = classificar_arquivo(arquivo)

        organizar_arquivo(arquivo, categoria, dry_run)