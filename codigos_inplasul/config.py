import tomllib
from pathlib import Path

import tomli_w
from tomlkit import document, table


arquivo_config = Path().home().joinpath(".config/codigos-inplasul.toml")


def carrega_config() -> dict:
    if not arquivo_config.exists():
        salva_config(
            tamanho_pagina="A4",
            fonte="Helvetica",
            tamanho_fonte=8,
            numero_colunas=18,
            espacamento_vertical=10,
            espacamento_horizontal=5,
        )
    config = tomllib.load(arquivo_config.open(mode="rb"))
    return config


def salva_config(
    tamanho_pagina: str,
    fonte: str,
    tamanho_fonte: int,
    numero_colunas: int,
    espacamento_vertical: int,
    espacamento_horizontal: int,
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

    if not arquivo_config.parent.exists():
        arquivo_config.parent.mkdir(parents=True, exist_ok=True)

    with open(arquivo_config, "wb") as f:
        tomli_w.dump(doc, f)
