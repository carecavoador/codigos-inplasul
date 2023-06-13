import tomllib
from pathlib import Path
from tomlkit import document, table
import tomli_w


arquivo_config = Path().home().joinpath(".config/codigos-inplasul.toml")

def carrega_config() -> dict:
    if not arquivo_config.exists():
        salva_config()
    config = tomllib.load(arquivo_config.open(mode="rb"))
    return config

def salva_config(
        tamanho_pagina: str = "A4",
        fonte: str = "Helvetica",
        tamanho_fonte: int = 8,
        numero_colunas: int = 18,
        espacamento_vertical: int = 10,
        espacamento_horizontal: int = 5
    ):
    doc = document()
    padroes = table()
    padroes.add("tamanho_pagina", tamanho_pagina)
    padroes.add("fonte", fonte)
    padroes.add("tamanho_fonte", tamanho_fonte)
    padroes.add("numero_colunas", numero_colunas)
    padroes.add("espacamento_vertical", espacamento_vertical)
    padroes.add("espacamento_horizontal", espacamento_horizontal)
    doc.add("padroes", padroes)
    with open(arquivo_config, "wb") as f:
        tomli_w.dump(doc, f)
