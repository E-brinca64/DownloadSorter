# DownloadSorter

Uma ferramenta simples desenvolvida em Python para organizar automaticamente os arquivos da pasta Downloads em diretórios categorizados de acordo com suas extensões.

## Funcionalidades

- **Classificação automática:** Identifica arquivos com base em suas extensões.
- **Organização por categorias:** Move os arquivos para diretórios predefinidos.
- **Tratamento de arquivos duplicados:** Evita conflitos de nomes adicionando um sufixo numérico aos arquivos duplicados.
- **Modo Dry-run:** Simula a organização sem mover os arquivos de verdade.
- **Categorias personalizáveis:** As categorias e extensões suportadas podem ser modificadas no arquivo `config.py`.

## Estrutura do Projeto

```text
DownloadSorter/
├── config.py
├── classifier.py
├── organizer.py
└── main.py
```

## Requisitos

- Python 3.15 ou superior.
- Nenhuma dependência externa necessária.

O projeto utiliza apenas bibliotecas da própria biblioteca padrão do Python.

## Como utilizar

1. Clone o repositório:

   ```bash
   git clone https://github.com/E-brinca64/DownloadSorter.git
   ```

2. Entre no diretório do projeto:

   ```bash
   cd DownloadSorter
   ```

3. Execute o programa:

   ```bash
   python3 main.py
   ```

## Modo Dry-run

O DownloadSorter possui um modo Dry-run que permite visualizar como os arquivos seriam organizados antes de realizar qualquer alteração.

Quando ativado, o programa exibe os caminhos de destino dos arquivos sem movê-los ou criar os diretórios de destino.

Para realizar a organização de verdade, altere a variável `DRY_RUN` no arquivo `main.py` para `False`.

**Recomendação:** Mantenha o Dry-run ativado durante os testes.

## Configuração

Você pode personalizar as categorias e extensões dos arquivos no arquivo `config.py`.

Por exemplo:

```python
'Pictures/Geral': ['.jpg', '.jpeg', '.png', '.webp'],
'Documents/Pdf': ['.pdf'],
'Music/Geral': ['.mp3', '.wav', '.flac'],
```

Arquivos que não correspondem a nenhuma extensão configurada são direcionados para o diretório `Geral`.

## Compatibilidade

Desenvolvido e testado no Linux. A compatibilidade com Windows e macOS ainda não foi testada.

## Licença

Este projeto está licenciado sob a licença MIT.

---

**Language:** [English](README.md)