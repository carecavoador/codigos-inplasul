from sys import argv
from PySide6.QtWidgets import QApplication
from janela_principal import JanelaPrincipal


def main():
    app = QApplication(argv)
    app.setStyle("Fusion")
    janela = JanelaPrincipal()
    janela.show()
    app.exec()


if __name__ == "__main__":
    main()
