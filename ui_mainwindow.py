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


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(620, 466)
        icon = QIcon()
        icon.addFile(u"img/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet(u"")
        login.setIconSize(QSize(32, 32))
        login.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: #fff;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.inpUsuario = QLineEdit(self.frame_5)
        self.inpUsuario.setObjectName(u"inpUsuario")
        font1 = QFont()
        font1.setPointSize(14)
        self.inpUsuario.setFont(font1)
        self.inpUsuario.setStyleSheet(u"QLineEdit{\n"
"	padding-top: 8px;\n"
"	padding-bottom: 8px;\n"
"	border: 0px;\n"
"	border-bottom: 2px solid #000;\n"
"	background-color: transparent;\n"
"	color: #262626;\n"
"	padding-left: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.inpUsuario)


        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.inpPass = QLineEdit(self.frame_4)
        self.inpPass.setObjectName(u"inpPass")
        self.inpPass.setFont(font1)
        self.inpPass.setStyleSheet(u"QLineEdit{\n"
"	padding-top: 8px;\n"
"	padding-bottom: 8px;\n"
"	border: 0px;\n"
"	border-bottom: 2px solid #000;\n"
"	background-color: transparent;\n"
"	color: #262626;\n"
"	padding-left: 5px;\n"
"}")
        self.inpPass.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.inpPass)


        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnIniciarSesion = QPushButton(self.frame_6)
        self.btnIniciarSesion.setObjectName(u"btnIniciarSesion")
        self.btnIniciarSesion.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnIniciarSesion.setFont(font2)
        self.btnIniciarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnIniciarSesion.setStyleSheet(u"QPushButton{\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"	background-color: #0891B2;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #0e7490;\n"
"}")

        self.gridLayout_4.addWidget(self.btnIniciarSesion, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(71, 71))

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(22)
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 620, 21))
        login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(login)
        self.statusbar.setObjectName(u"statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("login", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Contrase\u00f1a", None))
        self.btnIniciarSesion.setText(QCoreApplication.translate("login", u"Iniciar Sesi\u00f3n", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("login", u"Hospital Blabla", None))
    # retranslateUi

