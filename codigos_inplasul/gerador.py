"""
Este script gera um arquivo PDF com os códigos passados pelo usuário.
"""
from io import BytesIO
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4, A3
from reportlab.pdfbase import pdfmetrics


TAMANHOS = {
    "A4": A4,
    "A3": A3,
}

def divide_em_colunas(lista: list, colunas: int) -> list[list]:
    """
    Divide uma lista em um determinado numero de colulas e retorna
    uma lista contendo uma lista para cada coluna.
    Descaradamente roubado do Stack Overflow:
    https://stackoverflow.com/questions/2130016/
    """
    k, m = divmod(len(lista), colunas)
    return list((lista[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(colunas)))


def gera_pdf_codigos(
        codigos: str,
        colunas: int,
        tamanho_pagina: str,
        espaco_vertical: int,
        espaco_horizontal: int,
        fonte: str,
        tamanho_fonte: int,
        arquivo_pdf: Path
    ) -> None:
    """Gera e salva o PDF contendo os códigos informados."""

    tamanho_pagina = TAMANHOS[tamanho_pagina]
    separador = ";"
    codigos = codigos.split(separador)
    lista_colunas = divide_em_colunas(codigos, colunas)
    bytes_pdf = BytesIO()
    _, altura = tamanho_pagina
    margem_topo = 10 * mm
    margem_lateral = 10 * mm
    documento = canvas.Canvas(bytes_pdf, pagesize=tamanho_pagina)

    pos_x = margem_lateral
    for coluna in lista_colunas:
        texto = documento.beginText()
        texto.setTextOrigin(pos_x, altura - margem_topo - tamanho_fonte)
        texto.setFont(fonte, tamanho_fonte)
        maior_texto = 0.0
        for codigo in coluna:
            texto.moveCursor(0, espaco_vertical)
            texto.textLine(codigo)
            larg_texto = pdfmetrics.stringWidth(codigo, fonte, tamanho_fonte)
            maior_texto = max(maior_texto, larg_texto)
        documento.drawText(texto)
        pos_x += maior_texto + espaco_horizontal
        texto.setTextOrigin(pos_x, altura - margem_topo - tamanho_fonte)

    documento.save()
    bytes_pdf.seek(0)
    novo_pdf = PdfReader(bytes_pdf)
    pdf_writer = PdfWriter()
    pdf_writer.add_page(novo_pdf.pages[0])

    with open(arquivo_pdf, "wb") as arquivo:
        pdf_writer.write(arquivo)
