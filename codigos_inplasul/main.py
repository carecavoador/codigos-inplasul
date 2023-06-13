import sys
from PySide6.QtWidgets import QApplication
from janela_principal import JanelaPrincipal


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    janela = JanelaPrincipal()
    janela.show()
    app.exec()


if __name__ == "__main__":
    main()
