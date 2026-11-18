from config import arq_categories

def classificar_arquivo(arquivo):
         
        for categoria, extensoes in arq_categories.items():
                if arquivo.suffix.lower() in extensoes:
                        return categoria
        return 'Geral'

