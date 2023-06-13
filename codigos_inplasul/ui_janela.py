# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_janela.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(391, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_exportar = QPushButton(self.centralwidget)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setGeometry(QRect(290, 10, 91, 24))
        self.btn_limpar = QPushButton(self.centralwidget)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setGeometry(QRect(190, 10, 91, 24))
        self.btn_importar = QPushButton(self.centralwidget)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setGeometry(QRect(10, 10, 171, 24))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 300, 371, 121))
        self.combo_tamanho_pagina = QComboBox(self.groupBox)
        self.combo_tamanho_pagina.addItem("")
        self.combo_tamanho_pagina.addItem("")
        self.combo_tamanho_pagina.setObjectName(u"combo_tamanho_pagina")
        self.combo_tamanho_pagina.setGeometry(QRect(10, 40, 111, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 111, 16))
        self.spin_numero_colunas = QSpinBox(self.groupBox)
        self.spin_numero_colunas.setObjectName(u"spin_numero_colunas")
        self.spin_numero_colunas.setGeometry(QRect(130, 40, 111, 22))
        self.spin_numero_colunas.setValue(20)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 111, 16))
        self.combo_fonte = QComboBox(self.groupBox)
        self.combo_fonte.addItem("")
        self.combo_fonte.addItem("")
        self.combo_fonte.addItem("")
        self.combo_fonte.setObjectName(u"combo_fonte")
        self.combo_fonte.setGeometry(QRect(10, 90, 111, 22))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 41, 16))
        self.spin_tamanho_fonte = QSpinBox(self.groupBox)
        self.spin_tamanho_fonte.setObjectName(u"spin_tamanho_fonte")
        self.spin_tamanho_fonte.setGeometry(QRect(130, 90, 111, 22))
        self.spin_tamanho_fonte.setValue(5)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 70, 101, 16))
        self.spin_vertical = QSpinBox(self.groupBox)
        self.spin_vertical.setObjectName(u"spin_vertical")
        self.spin_vertical.setGeometry(QRect(250, 40, 111, 22))
        self.spin_vertical.setValue(5)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 20, 111, 16))
        self.spin_horizontal = QSpinBox(self.groupBox)
        self.spin_horizontal.setObjectName(u"spin_horizontal")
        self.spin_horizontal.setGeometry(QRect(250, 90, 111, 22))
        self.spin_horizontal.setValue(5)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 70, 111, 16))
        self.edit_codigos = QPlainTextEdit(self.centralwidget)
        self.edit_codigos.setObjectName(u"edit_codigos")
        self.edit_codigos.setGeometry(QRect(10, 41, 371, 251))
        font = QFont()
        font.setFamilies([u"Monoid"])
        font.setPointSize(8)
        self.edit_codigos.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerador de c\u00f3digos", None))
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF...", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar texto de arquivo...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es:", None))
        self.combo_tamanho_pagina.setItemText(0, QCoreApplication.translate("MainWindow", u"A4", None))
        self.combo_tamanho_pagina.setItemText(1, QCoreApplication.translate("MainWindow", u"A3", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tamanho da p\u00e1gina", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Colunas", None))
        self.combo_fonte.setItemText(0, QCoreApplication.translate("MainWindow", u"Helvetica", None))
        self.combo_fonte.setItemText(1, QCoreApplication.translate("MainWindow", u"Courier", None))
        self.combo_fonte.setItemText(2, QCoreApplication.translate("MainWindow", u"Times-Roman", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fonte", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tamanho da fonte", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Espa\u00e7amento Vertical", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Espa\u00e7amento Horiz.", None))
        self.edit_codigos.setPlainText("")
    # retranslateUi

