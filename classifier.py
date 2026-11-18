from pathlib import Path

from config import arq_categories

def classificar_arquivo(arquivo):
         
        for categoria, extensoes in arq_categories.items():
                if arquivo.suffix.lower() in extensoes:
                        return categoria
        return 'Geral'

Downloads = Path.home() / 'Downloads'

for arquivo in Downloads.iterdir():
    if arquivo.is_file():
        print(arquivo.name)
        print(arquivo.suffix)
        categoria = classificar_arquivo(arquivo)
        print(f"Categoria: {categoria}")

arquivo = Path("fds.zip")
print(classificar_arquivo(arquivo))