# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(495, 392)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnAgregarInicio = QPushButton(self.groupBox)
        self.btnAgregarInicio.setObjectName(u"btnAgregarInicio")

        self.gridLayout_2.addWidget(self.btnAgregarInicio, 5, 0, 1, 2)

        self.inpAutor = QLineEdit(self.groupBox)
        self.inpAutor.setObjectName(u"inpAutor")

        self.gridLayout_2.addWidget(self.inpAutor, 1, 1, 1, 1)

        self.btnMostrar = QPushButton(self.groupBox)
        self.btnMostrar.setObjectName(u"btnMostrar")

        self.gridLayout_2.addWidget(self.btnMostrar, 6, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.btnAgregarFinal = QPushButton(self.groupBox)
        self.btnAgregarFinal.setObjectName(u"btnAgregarFinal")

        self.gridLayout_2.addWidget(self.btnAgregarFinal, 4, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.inpEditorial = QLineEdit(self.groupBox)
        self.inpEditorial.setObjectName(u"inpEditorial")

        self.gridLayout_2.addWidget(self.inpEditorial, 3, 1, 1, 1)

        self.inpTitulo = QLineEdit(self.groupBox)
        self.inpTitulo.setObjectName(u"inpTitulo")

        self.gridLayout_2.addWidget(self.inpTitulo, 0, 1, 1, 1)

        self.inpPublicado = QSpinBox(self.groupBox)
        self.inpPublicado.setObjectName(u"inpPublicado")

        self.gridLayout_2.addWidget(self.inpPublicado, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.txtMostrar = QTextEdit(self.centralwidget)
        self.txtMostrar.setObjectName(u"txtMostrar")

        self.gridLayout.addWidget(self.txtMostrar, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 495, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Libro", None))
        self.btnAgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Publicado:", None))
        self.btnAgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Titulo:", None))
        self.inpEditorial.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editorial:", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

