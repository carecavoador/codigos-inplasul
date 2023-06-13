from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_janela import Ui_MainWindow
import gerador


class JanelaPrincipal(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.btn_importar.clicked.connect(self.carrega_arquivo)
        self.btn_limpar.clicked.connect(self.limpa_codigos)
        self.btn_exportar.clicked.connect(self.exporta_pdf)

    def carrega_arquivo(self) -> None:
        tipo_arquivo = "Arquivos de texto (*.txt)"
        titulo = "Importar arquivo de texto..."
        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            caption=titulo,
            filter=tipo_arquivo
        )
        texto = Path(arquivo).read_text().strip()
        self.edit_codigos.setPlainText(texto)

    def limpa_codigos(self) -> None:
        self.edit_codigos.clear()

    def exporta_pdf(self) -> None:
        tipo_arquivo = "Arquivo PDF (*.pdf)"
        titulo = "Salvar PDF..."
        arquivo, _ = QFileDialog.getSaveFileName(
            self,
            caption=titulo,
            filter=tipo_arquivo
        )
        codigos = self.edit_codigos.toPlainText()
        colunas = self.spin_numero_colunas.value()
        tamanho_pagina = self.combo_tamanho_pagina.itemText(self.combo_tamanho_pagina.currentIndex())
        espaco_vertical = self.spin_vertical.value()
        espaco_horizontal = self.spin_horizontal.value()
        fonte = self.combo_fonte.itemText(self.combo_fonte.currentIndex())
        tamanho_fonte = self.spin_tamanho_fonte.value()
        gerador.gera_pdf_codigos(
                                codigos,
                                colunas,
                                tamanho_pagina,
                                espaco_vertical,
                                espaco_horizontal,
                                fonte,
                                tamanho_fonte,
                                arquivo_pdf=Path(arquivo)
        )
