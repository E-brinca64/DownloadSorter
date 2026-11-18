
from pathlib import Path
import shutil


def organizar_arquivo(arquivo, categoria, dry_run=True):
    destino = Path.home() / categoria

    caminho_final = destino / arquivo.name

    if caminho_final.exists():
        nome_arquivo = arquivo.stem
        extensao_arquivo = arquivo.suffix
        contador = 1

        while (destino / f"{nome_arquivo}_{contador}{extensao_arquivo}").exists():
            contador += 1

        novo_nome = f"{nome_arquivo}_{contador}{extensao_arquivo}"
        caminho_final = destino / novo_nome

    if dry_run:
        print(f"[DRY-RUN] {arquivo} -> {caminho_final}")

    else:
        destino.mkdir(parents=True, exist_ok=True)
        shutil.move(str(arquivo), str(caminho_final))
        print(f"[MOVIDO] {arquivo.name} -> {caminho_final}")
