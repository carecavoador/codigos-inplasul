from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QFileDialog

import config
import gerador
from ui_janela import Ui_MainWindow


class JanelaPrincipal(QMainWindow, Ui_MainWindow):
    """Janela principal do programa."""

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.config = config.carrega_config()["padroes"]
        self.combo_tamanho_pagina.setCurrentIndex(
            self.combo_tamanho_pagina.findText(self.config["tamanho_pagina"])
        )
        self.combo_fonte.setCurrentIndex(
            self.combo_fonte.findText(self.config["fonte"])
        )
        self.spin_tamanho_fonte.setValue(self.config["tamanho_fonte"])
        self.spin_numero_colunas.setValue(self.config["numero_colunas"])
        self.spin_vertical.setValue(self.config["espacamento_vertical"])
        self.spin_horizontal.setValue(self.config["espacamento_horizontal"])
        self.btn_importar.clicked.connect(self.carrega_arquivo)
        self.btn_limpar.clicked.connect(lambda: self.edit_codigos.clear())
        self.btn_exportar.clicked.connect(self.exporta_pdf)
        self.combo_tamanho_pagina.currentTextChanged.connect(self.atualiza_config)
        self.combo_fonte.currentTextChanged.connect(self.atualiza_config)
        self.spin_numero_colunas.valueChanged.connect(self.atualiza_config)
        self.spin_tamanho_fonte.valueChanged.connect(self.atualiza_config)
        self.spin_vertical.valueChanged.connect(self.atualiza_config)
        self.spin_horizontal.valueChanged.connect(self.atualiza_config)

    def carrega_arquivo(self) -> None:
        """Carrega os códigos a partir de um arquivo .txt"""
        tipo_arquivo = "Arquivos de texto (*.txt)"
        titulo = "Importar arquivo de texto..."
        arquivo, _ = QFileDialog.getOpenFileName(
            self, caption=titulo, filter=tipo_arquivo
        )
        texto = Path(arquivo).read_text().strip()
        self.edit_codigos.setPlainText(texto)


    def exporta_pdf(self) -> None:
        """Exporta os códigos para um arquivo .pdf"""
        tipo_arquivo = "Arquivo PDF (*.pdf)"
        titulo = "Salvar PDF..."
        arquivo, _ = QFileDialog.getSaveFileName(
            self, caption=titulo, filter=tipo_arquivo
        )
        codigos = self.edit_codigos.toPlainText()
        colunas = self.spin_numero_colunas.value()
        tamanho_pagina = self.combo_tamanho_pagina.itemText(
            self.combo_tamanho_pagina.currentIndex()
        )
        espaco_vertical = self.spin_vertical.value()
        espaco_horizontal = self.spin_horizontal.value()
        fonte = self.combo_fonte.itemText(self.combo_fonte.currentIndex())
        tamanho_fonte = self.spin_tamanho_fonte.value()
        codigos = codigos.replace("\n", "")
        gerador.gera_pdf_codigos(
            codigos,
            colunas,
            tamanho_pagina,
            espaco_vertical,
            espaco_horizontal,
            fonte,
            tamanho_fonte,
            arquivo_pdf=Path(arquivo),
        )

    def atualiza_config(self) -> None:
        tamanho_pagina = self.combo_tamanho_pagina.itemText(
            self.combo_tamanho_pagina.currentIndex()
        )
        fonte = self.combo_fonte.itemText(self.combo_fonte.currentIndex())
        tamanho_fonte = self.spin_tamanho_fonte.value()
        numero_colunas = self.spin_numero_colunas.value()
        espacamento_vertical = self.spin_vertical.value()
        espacamento_horizontal = self.spin_horizontal.value()
        config.salva_config(
            tamanho_pagina=tamanho_pagina,
            fonte=fonte,
            tamanho_fonte=tamanho_fonte,
            numero_colunas=numero_colunas,
            espacamento_vertical=espacamento_vertical,
            espacamento_horizontal=espacamento_horizontal,
        )
