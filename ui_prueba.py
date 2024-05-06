# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondwindow.ui'
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
        MainWindow.resize(1088, 702)
        icon = QIcon()
        icon.addFile(u"img/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: #3F3F46;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_9)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(40, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnInicio = QFrame(self.frame_3)
        self.btnInicio.setObjectName(u"btnInicio")
        self.btnInicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInicio.setFrameShape(QFrame.StyledPanel)
        self.btnInicio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.btnInicio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_10 = QPushButton(self.btnInicio)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(80, 80))

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.lblLogo = QLabel(self.btnInicio)
        self.lblLogo.setObjectName(u"lblLogo")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblLogo.setFont(font)
        self.lblLogo.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")
        self.lblLogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblLogo)


        self.verticalLayout_5.addWidget(self.btnInicio, 0, Qt.AlignTop)

        self.btnMenu = QPushButton(self.frame_3)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMenu.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/bars.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon1)
        self.btnMenu.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btnMenu, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnUsuarios = QFrame(self.frame_5)
        self.btnUsuarios.setObjectName(u"btnUsuarios")
        self.btnUsuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnUsuarios.setStyleSheet(u"QFrame:hover{\n"
"	background-color: #475569;\n"
"}")
        self.btnUsuarios.setFrameShape(QFrame.StyledPanel)
        self.btnUsuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.btnUsuarios)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_6 = QPushButton(self.btnUsuarios)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"img/usuarios.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.lblUsuarios = QLabel(self.btnUsuarios)
        self.lblUsuarios.setObjectName(u"lblUsuarios")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lblUsuarios.setFont(font1)
        self.lblUsuarios.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.gridLayout_5.addWidget(self.lblUsuarios, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.btnUsuarios)

        self.btnPacientes = QFrame(self.frame_5)
        self.btnPacientes.setObjectName(u"btnPacientes")
        self.btnPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPacientes.setStyleSheet(u"QFrame:hover{\n"
"	background-color: #475569;\n"
"}")
        self.btnPacientes.setFrameShape(QFrame.StyledPanel)
        self.btnPacientes.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.btnPacientes)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_7 = QPushButton(self.btnPacientes)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"img/pacientes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.lblPacientes = QLabel(self.btnPacientes)
        self.lblPacientes.setObjectName(u"lblPacientes")
        self.lblPacientes.setFont(font1)
        self.lblPacientes.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.gridLayout_6.addWidget(self.lblPacientes, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.btnPacientes)

        self.btnCitas = QFrame(self.frame_5)
        self.btnCitas.setObjectName(u"btnCitas")
        self.btnCitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCitas.setStyleSheet(u"QFrame:hover{\n"
"	background-color: #475569;\n"
"}")
        self.btnCitas.setFrameShape(QFrame.StyledPanel)
        self.btnCitas.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.btnCitas)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_8 = QPushButton(self.btnCitas)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"img/citas.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.gridLayout_7.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.lblCitas = QLabel(self.btnCitas)
        self.lblCitas.setObjectName(u"lblCitas")
        self.lblCitas.setFont(font1)
        self.lblCitas.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.gridLayout_7.addWidget(self.lblCitas, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.btnCitas)

        self.btnAnalasis = QFrame(self.frame_5)
        self.btnAnalasis.setObjectName(u"btnAnalasis")
        self.btnAnalasis.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalasis.setStyleSheet(u"QFrame:hover{\n"
"	background-color: #475569;\n"
"}")
        self.btnAnalasis.setFrameShape(QFrame.StyledPanel)
        self.btnAnalasis.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.btnAnalasis)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_9 = QPushButton(self.btnAnalasis)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"img/enfermedades.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.gridLayout_8.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.lblAnalisis = QLabel(self.btnAnalasis)
        self.lblAnalisis.setObjectName(u"lblAnalisis")
        self.lblAnalisis.setFont(font1)
        self.lblAnalisis.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.gridLayout_8.addWidget(self.lblAnalisis, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.btnAnalasis)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnSalir = QFrame(self.frame_10)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSalir.setFrameShape(QFrame.StyledPanel)
        self.btnSalir.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.btnSalir)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_11 = QPushButton(self.btnSalir)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"img/salir.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.lblSalir = QLabel(self.btnSalir)
        self.lblSalir.setObjectName(u"lblSalir")
        self.lblSalir.setFont(font1)
        self.lblSalir.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.gridLayout_9.addWidget(self.lblSalir, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.btnSalir)


        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: #fff;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(6)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #fff;\n"
"	color: #000;\n"
"}")
        self.stackedWidget.setLineWidth(0)
        self.pagInicio = QWidget()
        self.pagInicio.setObjectName(u"pagInicio")
        self.verticalLayout_7 = QVBoxLayout(self.pagInicio)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.pagInicio)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 120))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.lblBienvenenida = QLabel(self.frame_11)
        self.lblBienvenenida.setObjectName(u"lblBienvenenida")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblBienvenenida.sizePolicy().hasHeightForWidth())
        self.lblBienvenenida.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(24)
        self.lblBienvenenida.setFont(font2)

        self.horizontalLayout_4.addWidget(self.lblBienvenenida)


        self.verticalLayout_7.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_12 = QFrame(self.pagInicio)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.frame_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cardPacientes = QFrame(self.frame_4)
        self.cardPacientes.setObjectName(u"cardPacientes")
        sizePolicy1.setHeightForWidth(self.cardPacientes.sizePolicy().hasHeightForWidth())
        self.cardPacientes.setSizePolicy(sizePolicy1)
        self.cardPacientes.setMinimumSize(QSize(40, 20))
        self.cardPacientes.setMaximumSize(QSize(211, 91))
        self.cardPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.cardPacientes.setStyleSheet(u"QFrame{\n"
"	background-color: #0284C7;\n"
"	border-radius: 8px;\n"
"}")
        self.cardPacientes.setFrameShape(QFrame.StyledPanel)
        self.cardPacientes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.cardPacientes)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_13 = QPushButton(self.cardPacientes)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.pushButton_13)

        self.lblUsuarios_3 = QLabel(self.cardPacientes)
        self.lblUsuarios_3.setObjectName(u"lblUsuarios_3")
        self.lblUsuarios_3.setFont(font1)
        self.lblUsuarios_3.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_6.addWidget(self.lblUsuarios_3)

        self.lblContadorPacientes = QLabel(self.cardPacientes)
        self.lblContadorPacientes.setObjectName(u"lblContadorPacientes")
        self.lblContadorPacientes.setFont(font1)
        self.lblContadorPacientes.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_6.addWidget(self.lblContadorPacientes)


        self.gridLayout_2.addWidget(self.cardPacientes, 0, 0, 1, 1)

        self.cardUsuarios = QFrame(self.frame_4)
        self.cardUsuarios.setObjectName(u"cardUsuarios")
        sizePolicy1.setHeightForWidth(self.cardUsuarios.sizePolicy().hasHeightForWidth())
        self.cardUsuarios.setSizePolicy(sizePolicy1)
        self.cardUsuarios.setMinimumSize(QSize(40, 20))
        self.cardUsuarios.setMaximumSize(QSize(211, 91))
        self.cardUsuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.cardUsuarios.setStyleSheet(u"QFrame{\n"
"	background-color: #0284C7;\n"
"	border-radius: 8px;\n"
"}")
        self.cardUsuarios.setFrameShape(QFrame.StyledPanel)
        self.cardUsuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.cardUsuarios)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_12 = QPushButton(self.cardUsuarios)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.pushButton_12)

        self.lblUsuarios_2 = QLabel(self.cardUsuarios)
        self.lblUsuarios_2.setObjectName(u"lblUsuarios_2")
        self.lblUsuarios_2.setFont(font1)
        self.lblUsuarios_2.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lblUsuarios_2)

        self.lblContadorUsuarios = QLabel(self.cardUsuarios)
        self.lblContadorUsuarios.setObjectName(u"lblContadorUsuarios")
        self.lblContadorUsuarios.setFont(font1)
        self.lblContadorUsuarios.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lblContadorUsuarios)


        self.gridLayout_2.addWidget(self.cardUsuarios, 1, 0, 1, 1)

        self.cardCitas = QFrame(self.frame_4)
        self.cardCitas.setObjectName(u"cardCitas")
        sizePolicy1.setHeightForWidth(self.cardCitas.sizePolicy().hasHeightForWidth())
        self.cardCitas.setSizePolicy(sizePolicy1)
        self.cardCitas.setMinimumSize(QSize(40, 20))
        self.cardCitas.setMaximumSize(QSize(211, 91))
        self.cardCitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.cardCitas.setStyleSheet(u"QFrame{\n"
"	background-color: #0284C7;\n"
"	border-radius: 8px;\n"
"}")
        self.cardCitas.setFrameShape(QFrame.StyledPanel)
        self.cardCitas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.cardCitas)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_14 = QPushButton(self.cardCitas)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.pushButton_14.setIcon(icon4)
        self.pushButton_14.setIconSize(QSize(50, 50))

        self.horizontalLayout_7.addWidget(self.pushButton_14)

        self.lblUsuarios_4 = QLabel(self.cardCitas)
        self.lblUsuarios_4.setObjectName(u"lblUsuarios_4")
        self.lblUsuarios_4.setFont(font1)
        self.lblUsuarios_4.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_7.addWidget(self.lblUsuarios_4)

        self.lblContadorCitas = QLabel(self.cardCitas)
        self.lblContadorCitas.setObjectName(u"lblContadorCitas")
        self.lblContadorCitas.setFont(font1)
        self.lblContadorCitas.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_7.addWidget(self.lblContadorCitas)


        self.gridLayout_2.addWidget(self.cardCitas, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.pagInicio)
        self.pagUsuarios = QWidget()
        self.pagUsuarios.setObjectName(u"pagUsuarios")
        self.verticalLayout_8 = QVBoxLayout(self.pagUsuarios)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.pagUsuarios)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(0, 120))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.pushButton_15 = QPushButton(self.frame_15)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"img/usuariosPag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(80, 80))

        self.horizontalLayout_8.addWidget(self.pushButton_15)

        self.lblBienvenenida_2 = QLabel(self.frame_15)
        self.lblBienvenenida_2.setObjectName(u"lblBienvenenida_2")
        sizePolicy.setHeightForWidth(self.lblBienvenenida_2.sizePolicy().hasHeightForWidth())
        self.lblBienvenenida_2.setSizePolicy(sizePolicy)
        self.lblBienvenenida_2.setFont(font2)

        self.horizontalLayout_8.addWidget(self.lblBienvenenida_2)

        self.btnAgregarUsuario = QPushButton(self.frame_15)
        self.btnAgregarUsuario.setObjectName(u"btnAgregarUsuario")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnAgregarUsuario.sizePolicy().hasHeightForWidth())
        self.btnAgregarUsuario.setSizePolicy(sizePolicy4)
        self.btnAgregarUsuario.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnAgregarUsuario.setFont(font3)
        self.btnAgregarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarUsuario.setLayoutDirection(Qt.LeftToRight)
        self.btnAgregarUsuario.setStyleSheet(u"QPushButton{\n"
"	background-color: #0EA5E9;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #0284c7;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"img/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAgregarUsuario.setIcon(icon8)
        self.btnAgregarUsuario.setIconSize(QSize(20, 50))

        self.horizontalLayout_8.addWidget(self.btnAgregarUsuario)


        self.verticalLayout_8.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.pagUsuarios)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 55))
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(100, -1, 100, -1)
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        self.label.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label)

        self.inpUsuariosBusqueda = QLineEdit(self.frame_17)
        self.inpUsuariosBusqueda.setObjectName(u"inpUsuariosBusqueda")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.inpUsuariosBusqueda.sizePolicy().hasHeightForWidth())
        self.inpUsuariosBusqueda.setSizePolicy(sizePolicy5)
        self.inpUsuariosBusqueda.setFont(font4)
        self.inpUsuariosBusqueda.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #8B8B8B;\n"
"	padding: 10px;\n"
"	color: #525252;\n"
"}")
        self.inpUsuariosBusqueda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.inpUsuariosBusqueda)


        self.verticalLayout_9.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tblUsuarios = QTableWidget(self.frame_18)
        if (self.tblUsuarios.columnCount() < 5):
            self.tblUsuarios.setColumnCount(5)
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tblUsuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tblUsuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tblUsuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tblUsuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tblUsuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblUsuarios.setObjectName(u"tblUsuarios")
        self.tblUsuarios.setFont(font4)
        self.tblUsuarios.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: #ECECEC;\n"
"	border: 1px solid #8d8d8d;\n"
"}")
        self.tblUsuarios.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout_10.addWidget(self.tblUsuarios)


        self.verticalLayout_9.addWidget(self.frame_18)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.pagUsuarios)
        self.pagPacientes = QWidget()
        self.pagPacientes.setObjectName(u"pagPacientes")
        self.verticalLayout_12 = QVBoxLayout(self.pagPacientes)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.pagPacientes)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QSize(0, 120))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.pushButton_16 = QPushButton(self.frame_20)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"img/pacientesPag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon9)
        self.pushButton_16.setIconSize(QSize(80, 80))

        self.horizontalLayout_11.addWidget(self.pushButton_16)

        self.lblBienvenenida_3 = QLabel(self.frame_20)
        self.lblBienvenenida_3.setObjectName(u"lblBienvenenida_3")
        sizePolicy.setHeightForWidth(self.lblBienvenenida_3.sizePolicy().hasHeightForWidth())
        self.lblBienvenenida_3.setSizePolicy(sizePolicy)
        self.lblBienvenenida_3.setFont(font2)

        self.horizontalLayout_11.addWidget(self.lblBienvenenida_3)

        self.btnAgregarPaciente = QPushButton(self.frame_20)
        self.btnAgregarPaciente.setObjectName(u"btnAgregarPaciente")
        sizePolicy4.setHeightForWidth(self.btnAgregarPaciente.sizePolicy().hasHeightForWidth())
        self.btnAgregarPaciente.setSizePolicy(sizePolicy4)
        self.btnAgregarPaciente.setMaximumSize(QSize(16777215, 16777215))
        self.btnAgregarPaciente.setFont(font3)
        self.btnAgregarPaciente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarPaciente.setLayoutDirection(Qt.LeftToRight)
        self.btnAgregarPaciente.setStyleSheet(u"QPushButton{\n"
"	background-color: #0EA5E9;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #0284c7;\n"
"}")
        self.btnAgregarPaciente.setIcon(icon8)
        self.btnAgregarPaciente.setIconSize(QSize(20, 50))

        self.horizontalLayout_11.addWidget(self.btnAgregarPaciente)


        self.verticalLayout_12.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.pagPacientes)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 55))
        self.frame_19.setMaximumSize(QSize(16777215, 80))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(100, -1, 100, -1)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.inpBusquedaPacientes = QLineEdit(self.frame_19)
        self.inpBusquedaPacientes.setObjectName(u"inpBusquedaPacientes")
        sizePolicy5.setHeightForWidth(self.inpBusquedaPacientes.sizePolicy().hasHeightForWidth())
        self.inpBusquedaPacientes.setSizePolicy(sizePolicy5)
        self.inpBusquedaPacientes.setFont(font4)
        self.inpBusquedaPacientes.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #8B8B8B;\n"
"	padding: 10px;\n"
"	color: #525252;\n"
"}")
        self.inpBusquedaPacientes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.inpBusquedaPacientes)


        self.verticalLayout_12.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.pagPacientes)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tblPacientes = QTableWidget(self.frame_21)
        if (self.tblPacientes.columnCount() < 6):
            self.tblPacientes.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tblPacientes.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.tblPacientes.setObjectName(u"tblPacientes")
        self.tblPacientes.setFont(font4)
        self.tblPacientes.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: #ECECEC;\n"
"	border: 1px solid #8d8d8d;\n"
"}")
        self.tblPacientes.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout_11.addWidget(self.tblPacientes)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.pagPacientes)
        self.pagCitas = QWidget()
        self.pagCitas.setObjectName(u"pagCitas")
        self.verticalLayout_38 = QVBoxLayout(self.pagCitas)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.pagCitas)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy)
        self.frame_54.setMinimumSize(QSize(0, 120))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(20, 20, 20, 20)
        self.pushButton_17 = QPushButton(self.frame_54)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"img/citasPag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon10)
        self.pushButton_17.setIconSize(QSize(80, 80))

        self.horizontalLayout_28.addWidget(self.pushButton_17)

        self.lblBienvenenida_4 = QLabel(self.frame_54)
        self.lblBienvenenida_4.setObjectName(u"lblBienvenenida_4")
        sizePolicy.setHeightForWidth(self.lblBienvenenida_4.sizePolicy().hasHeightForWidth())
        self.lblBienvenenida_4.setSizePolicy(sizePolicy)
        self.lblBienvenenida_4.setFont(font2)

        self.horizontalLayout_28.addWidget(self.lblBienvenenida_4)

        self.btnAgregarCita = QPushButton(self.frame_54)
        self.btnAgregarCita.setObjectName(u"btnAgregarCita")
        sizePolicy4.setHeightForWidth(self.btnAgregarCita.sizePolicy().hasHeightForWidth())
        self.btnAgregarCita.setSizePolicy(sizePolicy4)
        self.btnAgregarCita.setMaximumSize(QSize(16777215, 16777215))
        self.btnAgregarCita.setFont(font3)
        self.btnAgregarCita.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarCita.setLayoutDirection(Qt.LeftToRight)
        self.btnAgregarCita.setStyleSheet(u"QPushButton{\n"
"	background-color: #0EA5E9;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #0284c7;\n"
"}")
        self.btnAgregarCita.setIcon(icon8)
        self.btnAgregarCita.setIconSize(QSize(20, 50))

        self.horizontalLayout_28.addWidget(self.btnAgregarCita)


        self.verticalLayout_38.addWidget(self.frame_54, 0, Qt.AlignTop)

        self.frame_53 = QFrame(self.pagCitas)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 55))
        self.frame_53.setMaximumSize(QSize(16777215, 80))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(100, -1, 100, -1)
        self.label_26 = QLabel(self.frame_53)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setFont(font4)

        self.horizontalLayout_27.addWidget(self.label_26)

        self.inpBusquedaCitas = QLineEdit(self.frame_53)
        self.inpBusquedaCitas.setObjectName(u"inpBusquedaCitas")
        sizePolicy5.setHeightForWidth(self.inpBusquedaCitas.sizePolicy().hasHeightForWidth())
        self.inpBusquedaCitas.setSizePolicy(sizePolicy5)
        self.inpBusquedaCitas.setFont(font4)
        self.inpBusquedaCitas.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #8B8B8B;\n"
"	padding: 10px;\n"
"	color: #525252;\n"
"}")
        self.inpBusquedaCitas.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.inpBusquedaCitas)


        self.verticalLayout_38.addWidget(self.frame_53, 0, Qt.AlignTop)

        self.frame_52 = QFrame(self.pagCitas)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_52)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.tblCitas = QTableWidget(self.frame_52)
        if (self.tblCitas.columnCount() < 6):
            self.tblCitas.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tblCitas.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        self.tblCitas.setObjectName(u"tblCitas")
        self.tblCitas.setFont(font4)
        self.tblCitas.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: #ECECEC;\n"
"	border: 1px solid #8d8d8d;\n"
"}")
        self.tblCitas.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout_37.addWidget(self.tblCitas)


        self.verticalLayout_38.addWidget(self.frame_52)

        self.stackedWidget.addWidget(self.pagCitas)
        self.pagAnalisis = QWidget()
        self.pagAnalisis.setObjectName(u"pagAnalisis")
        self.verticalLayout_18 = QVBoxLayout(self.pagAnalisis)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.pagAnalisis)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 120))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.pushButton_18 = QPushButton(self.frame_6)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"img/enfermedadesPag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon11)
        self.pushButton_18.setIconSize(QSize(80, 80))

        self.horizontalLayout_2.addWidget(self.pushButton_18)

        self.lblBienvenenida_5 = QLabel(self.frame_6)
        self.lblBienvenenida_5.setObjectName(u"lblBienvenenida_5")
        sizePolicy.setHeightForWidth(self.lblBienvenenida_5.sizePolicy().hasHeightForWidth())
        self.lblBienvenenida_5.setSizePolicy(sizePolicy)
        self.lblBienvenenida_5.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lblBienvenenida_5)

        self.btnAgregarCita_2 = QPushButton(self.frame_6)
        self.btnAgregarCita_2.setObjectName(u"btnAgregarCita_2")
        sizePolicy4.setHeightForWidth(self.btnAgregarCita_2.sizePolicy().hasHeightForWidth())
        self.btnAgregarCita_2.setSizePolicy(sizePolicy4)
        self.btnAgregarCita_2.setMaximumSize(QSize(16777215, 16777215))
        self.btnAgregarCita_2.setFont(font3)
        self.btnAgregarCita_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarCita_2.setLayoutDirection(Qt.LeftToRight)
        self.btnAgregarCita_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #0EA5E9;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #0284c7;\n"
"}")
        self.btnAgregarCita_2.setIcon(icon8)
        self.btnAgregarCita_2.setIconSize(QSize(20, 50))

        self.horizontalLayout_2.addWidget(self.btnAgregarCita_2)


        self.verticalLayout_18.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.pagAnalisis)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 55))
        self.frame_8.setMaximumSize(QSize(16777215, 80))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(100, -1, 100, -1)
        self.label_33 = QLabel(self.frame_8)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)
        self.label_33.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_33)

        self.inpBusquedaCitas_2 = QLineEdit(self.frame_8)
        self.inpBusquedaCitas_2.setObjectName(u"inpBusquedaCitas_2")
        sizePolicy5.setHeightForWidth(self.inpBusquedaCitas_2.sizePolicy().hasHeightForWidth())
        self.inpBusquedaCitas_2.setSizePolicy(sizePolicy5)
        self.inpBusquedaCitas_2.setFont(font4)
        self.inpBusquedaCitas_2.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #8B8B8B;\n"
"	padding: 10px;\n"
"	color: #525252;\n"
"}")
        self.inpBusquedaCitas_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.inpBusquedaCitas_2)


        self.verticalLayout_18.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.pagAnalisis)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tblCitas_2 = QTableWidget(self.frame_7)
        if (self.tblCitas_2.columnCount() < 6):
            self.tblCitas_2.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.tblCitas_2.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.tblCitas_2.setObjectName(u"tblCitas_2")
        self.tblCitas_2.setFont(font4)
        self.tblCitas_2.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: #ECECEC;\n"
"	border: 1px solid #8d8d8d;\n"
"}")
        self.tblCitas_2.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout_19.addWidget(self.tblCitas_2)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.pagAnalisis)
        self.pagAgregarUsuario = QWidget()
        self.pagAgregarUsuario.setObjectName(u"pagAgregarUsuario")
        self.verticalLayout_14 = QVBoxLayout(self.pagAgregarUsuario)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.pagAgregarUsuario)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QSize(0, 120))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_13.setSpacing(12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarAUsuarios = QPushButton(self.frame_23)
        self.btnRegresarAUsuarios.setObjectName(u"btnRegresarAUsuarios")
        self.btnRegresarAUsuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarAUsuarios.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"img/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRegresarAUsuarios.setIcon(icon12)
        self.btnRegresarAUsuarios.setIconSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.btnRegresarAUsuarios, 0, Qt.AlignLeft)

        self.lblRegresarAgUsuarios = QLabel(self.frame_23)
        self.lblRegresarAgUsuarios.setObjectName(u"lblRegresarAgUsuarios")
        sizePolicy.setHeightForWidth(self.lblRegresarAgUsuarios.sizePolicy().hasHeightForWidth())
        self.lblRegresarAgUsuarios.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(16)
        self.lblRegresarAgUsuarios.setFont(font6)
        self.lblRegresarAgUsuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarAgUsuarios.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_13.addWidget(self.lblRegresarAgUsuarios)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)


        self.verticalLayout_14.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_22 = QFrame(self.pagAgregarUsuario)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 70))
        self.frame_22.setMaximumSize(QSize(16777215, 264))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(40, -1, 40, -1)
        self.lblRegistroUsuario = QFrame(self.frame_22)
        self.lblRegistroUsuario.setObjectName(u"lblRegistroUsuario")
        self.lblRegistroUsuario.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblRegistroUsuario.setFrameShape(QFrame.StyledPanel)
        self.lblRegistroUsuario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.lblRegistroUsuario)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.lblIconoRegistroUsuario = QPushButton(self.lblRegistroUsuario)
        self.lblIconoRegistroUsuario.setObjectName(u"lblIconoRegistroUsuario")
        self.lblIconoRegistroUsuario.setMinimumSize(QSize(30, 30))
        self.lblIconoRegistroUsuario.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"img/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lblIconoRegistroUsuario.setIcon(icon13)
        self.lblIconoRegistroUsuario.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.lblIconoRegistroUsuario)

        self.lblMsjRegistroUsuario = QLabel(self.lblRegistroUsuario)
        self.lblMsjRegistroUsuario.setObjectName(u"lblMsjRegistroUsuario")
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.lblMsjRegistroUsuario.setFont(font7)
        self.lblMsjRegistroUsuario.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_14.addWidget(self.lblMsjRegistroUsuario)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_12.addWidget(self.lblRegistroUsuario)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.pagAgregarUsuario)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_24)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setMinimumSize(QSize(0, 0))
        self.frame_25.setSizeIncrement(QSize(0, 0))
        self.frame_25.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_25)
        self.verticalLayout_16.setSpacing(14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_13 = QFrame(self.frame_25)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_13.addWidget(self.label_9, 0, Qt.AlignTop)

        self.inpRegistroNick = QLineEdit(self.frame_13)
        self.inpRegistroNick.setObjectName(u"inpRegistroNick")
        self.inpRegistroNick.setMinimumSize(QSize(0, 30))
        self.inpRegistroNick.setFont(font4)
        self.inpRegistroNick.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_13.addWidget(self.inpRegistroNick)


        self.verticalLayout_16.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.frame_25)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_15.addWidget(self.label_10, 0, Qt.AlignTop)

        self.inpRegistroPass = QLineEdit(self.frame_14)
        self.inpRegistroPass.setObjectName(u"inpRegistroPass")
        self.inpRegistroPass.setMinimumSize(QSize(0, 30))
        self.inpRegistroPass.setFont(font4)
        self.inpRegistroPass.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_15.addWidget(self.inpRegistroPass)


        self.verticalLayout_16.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_26)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.frame_26)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_17.addWidget(self.label_11, 0, Qt.AlignTop)

        self.inpRegistroRol = QComboBox(self.frame_26)
        self.inpRegistroRol.setObjectName(u"inpRegistroRol")
        self.inpRegistroRol.setMinimumSize(QSize(0, 30))
        self.inpRegistroRol.setFont(font4)
        self.inpRegistroRol.setLayoutDirection(Qt.LeftToRight)
        self.inpRegistroRol.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.inpRegistroRol)


        self.verticalLayout_16.addWidget(self.frame_26)

        self.btnRegistroSubmit = QPushButton(self.frame_25)
        self.btnRegistroSubmit.setObjectName(u"btnRegistroSubmit")
        self.btnRegistroSubmit.setFont(font1)
        self.btnRegistroSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistroSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_16.addWidget(self.btnRegistroSubmit)


        self.gridLayout_11.addWidget(self.frame_25, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 1, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.pagAgregarUsuario)
        self.pagEditarUsuario = QWidget()
        self.pagEditarUsuario.setObjectName(u"pagEditarUsuario")
        self.verticalLayout_26 = QVBoxLayout(self.pagEditarUsuario)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.pagEditarUsuario)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setMinimumSize(QSize(0, 120))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarAUsuarios2 = QPushButton(self.frame_37)
        self.btnRegresarAUsuarios2.setObjectName(u"btnRegresarAUsuarios2")
        self.btnRegresarAUsuarios2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarAUsuarios2.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.btnRegresarAUsuarios2.setIcon(icon12)
        self.btnRegresarAUsuarios2.setIconSize(QSize(30, 30))

        self.horizontalLayout_20.addWidget(self.btnRegresarAUsuarios2, 0, Qt.AlignLeft)

        self.lblRegresarAgUsuarios2 = QLabel(self.frame_37)
        self.lblRegresarAgUsuarios2.setObjectName(u"lblRegresarAgUsuarios2")
        sizePolicy.setHeightForWidth(self.lblRegresarAgUsuarios2.sizePolicy().hasHeightForWidth())
        self.lblRegresarAgUsuarios2.setSizePolicy(sizePolicy)
        self.lblRegresarAgUsuarios2.setFont(font6)
        self.lblRegresarAgUsuarios2.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarAgUsuarios2.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_20.addWidget(self.lblRegresarAgUsuarios2)

        self.label_18 = QLabel(self.frame_37)
        self.label_18.setObjectName(u"label_18")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(20)
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"QLabel{\n"
"	margin-left: 20px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_18)

        self.lblEditarUsuarioActual = QLabel(self.frame_37)
        self.lblEditarUsuarioActual.setObjectName(u"lblEditarUsuarioActual")
        self.lblEditarUsuarioActual.setFont(font8)

        self.horizontalLayout_20.addWidget(self.lblEditarUsuarioActual)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)


        self.verticalLayout_26.addWidget(self.frame_37, 0, Qt.AlignTop)

        self.frame_36 = QFrame(self.pagEditarUsuario)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 70))
        self.frame_36.setMaximumSize(QSize(16777215, 264))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(40, -1, 40, -1)
        self.lblEditarUsuario = QFrame(self.frame_36)
        self.lblEditarUsuario.setObjectName(u"lblEditarUsuario")
        self.lblEditarUsuario.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblEditarUsuario.setFrameShape(QFrame.StyledPanel)
        self.lblEditarUsuario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.lblEditarUsuario)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_13)

        self.lblIconoEditarUsuario = QPushButton(self.lblEditarUsuario)
        self.lblIconoEditarUsuario.setObjectName(u"lblIconoEditarUsuario")
        self.lblIconoEditarUsuario.setMinimumSize(QSize(30, 30))
        self.lblIconoEditarUsuario.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.lblIconoEditarUsuario.setIcon(icon13)
        self.lblIconoEditarUsuario.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.lblIconoEditarUsuario)

        self.lblMsjEditarUsuario = QLabel(self.lblEditarUsuario)
        self.lblMsjEditarUsuario.setObjectName(u"lblMsjEditarUsuario")
        self.lblMsjEditarUsuario.setFont(font7)
        self.lblMsjEditarUsuario.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_19.addWidget(self.lblMsjEditarUsuario)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)


        self.horizontalLayout_18.addWidget(self.lblEditarUsuario)


        self.verticalLayout_26.addWidget(self.frame_36, 0, Qt.AlignTop)

        self.frame_27 = QFrame(self.pagEditarUsuario)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_27)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setSizeIncrement(QSize(0, 0))
        self.frame_32.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_32)
        self.verticalLayout_22.setSpacing(14)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_33)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_15 = QLabel(self.frame_33)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_23.addWidget(self.label_15, 0, Qt.AlignTop)

        self.inpEditarNick = QLineEdit(self.frame_33)
        self.inpEditarNick.setObjectName(u"inpEditarNick")
        self.inpEditarNick.setMinimumSize(QSize(0, 30))
        self.inpEditarNick.setFont(font4)
        self.inpEditarNick.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_23.addWidget(self.inpEditarNick)


        self.verticalLayout_22.addWidget(self.frame_33, 0, Qt.AlignTop)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_34)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_16 = QLabel(self.frame_34)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_24.addWidget(self.label_16, 0, Qt.AlignTop)

        self.inpEditarPass = QLineEdit(self.frame_34)
        self.inpEditarPass.setObjectName(u"inpEditarPass")
        self.inpEditarPass.setMinimumSize(QSize(0, 30))
        self.inpEditarPass.setFont(font4)
        self.inpEditarPass.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_24.addWidget(self.inpEditarPass)


        self.verticalLayout_22.addWidget(self.frame_34, 0, Qt.AlignTop)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_35)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_17 = QLabel(self.frame_35)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_25.addWidget(self.label_17, 0, Qt.AlignTop)

        self.inpEditarRol = QComboBox(self.frame_35)
        self.inpEditarRol.setObjectName(u"inpEditarRol")
        self.inpEditarRol.setMinimumSize(QSize(0, 30))
        self.inpEditarRol.setFont(font4)
        self.inpEditarRol.setLayoutDirection(Qt.LeftToRight)
        self.inpEditarRol.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.inpEditarRol)


        self.verticalLayout_22.addWidget(self.frame_35)

        self.btnEditarSubmit = QPushButton(self.frame_32)
        self.btnEditarSubmit.setObjectName(u"btnEditarSubmit")
        self.btnEditarSubmit.setFont(font1)
        self.btnEditarSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditarSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_22.addWidget(self.btnEditarSubmit)


        self.gridLayout_13.addWidget(self.frame_32, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.pagEditarUsuario)
        self.pagAgregarPaciente = QWidget()
        self.pagAgregarPaciente.setObjectName(u"pagAgregarPaciente")
        self.verticalLayout_31 = QVBoxLayout(self.pagAgregarPaciente)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.pagAgregarPaciente)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QSize(0, 120))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_23.setSpacing(12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarAPacientes = QPushButton(self.frame_44)
        self.btnRegresarAPacientes.setObjectName(u"btnRegresarAPacientes")
        self.btnRegresarAPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarAPacientes.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.btnRegresarAPacientes.setIcon(icon12)
        self.btnRegresarAPacientes.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.btnRegresarAPacientes, 0, Qt.AlignLeft)

        self.lblRegresarAPacientes = QLabel(self.frame_44)
        self.lblRegresarAPacientes.setObjectName(u"lblRegresarAPacientes")
        sizePolicy.setHeightForWidth(self.lblRegresarAPacientes.sizePolicy().hasHeightForWidth())
        self.lblRegresarAPacientes.setSizePolicy(sizePolicy)
        self.lblRegresarAPacientes.setFont(font6)
        self.lblRegresarAPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarAPacientes.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_23.addWidget(self.lblRegresarAPacientes)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)


        self.verticalLayout_31.addWidget(self.frame_44, 0, Qt.AlignTop)

        self.frame_43 = QFrame(self.pagAgregarPaciente)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 70))
        self.frame_43.setMaximumSize(QSize(16777215, 264))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(40, -1, 40, -1)
        self.lblRegistroPaciente = QFrame(self.frame_43)
        self.lblRegistroPaciente.setObjectName(u"lblRegistroPaciente")
        self.lblRegistroPaciente.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblRegistroPaciente.setFrameShape(QFrame.StyledPanel)
        self.lblRegistroPaciente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.lblRegistroPaciente)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.lblIconoRegistroPaciente = QPushButton(self.lblRegistroPaciente)
        self.lblIconoRegistroPaciente.setObjectName(u"lblIconoRegistroPaciente")
        self.lblIconoRegistroPaciente.setMinimumSize(QSize(30, 30))
        self.lblIconoRegistroPaciente.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.lblIconoRegistroPaciente.setIcon(icon13)
        self.lblIconoRegistroPaciente.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.lblIconoRegistroPaciente)

        self.lblMsjRegistroPaciente = QLabel(self.lblRegistroPaciente)
        self.lblMsjRegistroPaciente.setObjectName(u"lblMsjRegistroPaciente")
        self.lblMsjRegistroPaciente.setFont(font7)
        self.lblMsjRegistroPaciente.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_22.addWidget(self.lblMsjRegistroPaciente)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)


        self.horizontalLayout_21.addWidget(self.lblRegistroPaciente)


        self.verticalLayout_31.addWidget(self.frame_43, 0, Qt.AlignTop)

        self.frame_38 = QFrame(self.pagAgregarPaciente)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_38)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_16 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy1.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy1)
        self.frame_39.setMinimumSize(QSize(0, 0))
        self.frame_39.setSizeIncrement(QSize(0, 0))
        self.frame_39.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_39)
        self.verticalLayout_27.setSpacing(14)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_40)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_19 = QLabel(self.frame_40)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_28.addWidget(self.label_19, 0, Qt.AlignTop)

        self.inpRegistroNombre = QLineEdit(self.frame_40)
        self.inpRegistroNombre.setObjectName(u"inpRegistroNombre")
        self.inpRegistroNombre.setMinimumSize(QSize(0, 30))
        self.inpRegistroNombre.setFont(font4)
        self.inpRegistroNombre.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.inpRegistroNombre)


        self.verticalLayout_27.addWidget(self.frame_40, 0, Qt.AlignTop)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_41)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_20 = QLabel(self.frame_41)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_29.addWidget(self.label_20, 0, Qt.AlignTop)

        self.inpRegistroApellidos = QLineEdit(self.frame_41)
        self.inpRegistroApellidos.setObjectName(u"inpRegistroApellidos")
        self.inpRegistroApellidos.setMinimumSize(QSize(0, 30))
        self.inpRegistroApellidos.setFont(font4)
        self.inpRegistroApellidos.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.inpRegistroApellidos)


        self.verticalLayout_27.addWidget(self.frame_41, 0, Qt.AlignTop)

        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_42)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_21 = QLabel(self.frame_42)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_30.addWidget(self.label_21, 0, Qt.AlignTop)

        self.inpRegistroEdad = QSpinBox(self.frame_42)
        self.inpRegistroEdad.setObjectName(u"inpRegistroEdad")
        self.inpRegistroEdad.setFont(font4)
        self.inpRegistroEdad.setStyleSheet(u"QSpinBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_30.addWidget(self.inpRegistroEdad)


        self.verticalLayout_27.addWidget(self.frame_42)

        self.btnRegistroPacienteSubmit = QPushButton(self.frame_39)
        self.btnRegistroPacienteSubmit.setObjectName(u"btnRegistroPacienteSubmit")
        self.btnRegistroPacienteSubmit.setFont(font1)
        self.btnRegistroPacienteSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistroPacienteSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_27.addWidget(self.btnRegistroPacienteSubmit)


        self.gridLayout_14.addWidget(self.frame_39, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 1, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.pagAgregarPaciente)
        self.pagEditarPaciente = QWidget()
        self.pagEditarPaciente.setObjectName(u"pagEditarPaciente")
        self.verticalLayout_36 = QVBoxLayout(self.pagEditarPaciente)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.pagEditarPaciente)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setMinimumSize(QSize(0, 120))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_24.setSpacing(12)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarAgPacientes = QPushButton(self.frame_50)
        self.btnRegresarAgPacientes.setObjectName(u"btnRegresarAgPacientes")
        self.btnRegresarAgPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarAgPacientes.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.btnRegresarAgPacientes.setIcon(icon12)
        self.btnRegresarAgPacientes.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.btnRegresarAgPacientes, 0, Qt.AlignLeft)

        self.lblRegresarAgPacientes = QLabel(self.frame_50)
        self.lblRegresarAgPacientes.setObjectName(u"lblRegresarAgPacientes")
        sizePolicy.setHeightForWidth(self.lblRegresarAgPacientes.sizePolicy().hasHeightForWidth())
        self.lblRegresarAgPacientes.setSizePolicy(sizePolicy)
        self.lblRegresarAgPacientes.setFont(font6)
        self.lblRegresarAgPacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarAgPacientes.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_24.addWidget(self.lblRegresarAgPacientes)

        self.label_25 = QLabel(self.frame_50)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"QLabel{\n"
"	margin-left: 20px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_25)

        self.lblEditarPacienteActual = QLabel(self.frame_50)
        self.lblEditarPacienteActual.setObjectName(u"lblEditarPacienteActual")
        self.lblEditarPacienteActual.setFont(font8)

        self.horizontalLayout_24.addWidget(self.lblEditarPacienteActual)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)


        self.verticalLayout_36.addWidget(self.frame_50, 0, Qt.AlignTop)

        self.frame_51 = QFrame(self.pagEditarPaciente)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 70))
        self.frame_51.setMaximumSize(QSize(16777215, 264))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(40, -1, 40, -1)
        self.lblEditarPaciente = QFrame(self.frame_51)
        self.lblEditarPaciente.setObjectName(u"lblEditarPaciente")
        self.lblEditarPaciente.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblEditarPaciente.setFrameShape(QFrame.StyledPanel)
        self.lblEditarPaciente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.lblEditarPaciente)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_24)

        self.lblIconoEditarPaciente = QPushButton(self.lblEditarPaciente)
        self.lblIconoEditarPaciente.setObjectName(u"lblIconoEditarPaciente")
        self.lblIconoEditarPaciente.setMinimumSize(QSize(30, 30))
        self.lblIconoEditarPaciente.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.lblIconoEditarPaciente.setIcon(icon13)
        self.lblIconoEditarPaciente.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.lblIconoEditarPaciente)

        self.lblMsjEditarPaciente = QLabel(self.lblEditarPaciente)
        self.lblMsjEditarPaciente.setObjectName(u"lblMsjEditarPaciente")
        self.lblMsjEditarPaciente.setFont(font7)
        self.lblMsjEditarPaciente.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_26.addWidget(self.lblMsjEditarPaciente)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_25)


        self.horizontalLayout_25.addWidget(self.lblEditarPaciente)


        self.verticalLayout_36.addWidget(self.frame_51, 0, Qt.AlignTop)

        self.frame_45 = QFrame(self.pagEditarPaciente)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_45)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_21 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_21, 0, 0, 1, 1)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy1.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy1)
        self.frame_46.setMinimumSize(QSize(0, 0))
        self.frame_46.setSizeIncrement(QSize(0, 0))
        self.frame_46.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_46)
        self.verticalLayout_32.setSpacing(14)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_47)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_22 = QLabel(self.frame_47)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_33.addWidget(self.label_22, 0, Qt.AlignTop)

        self.inpEditarNombre = QLineEdit(self.frame_47)
        self.inpEditarNombre.setObjectName(u"inpEditarNombre")
        self.inpEditarNombre.setMinimumSize(QSize(0, 30))
        self.inpEditarNombre.setFont(font4)
        self.inpEditarNombre.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_33.addWidget(self.inpEditarNombre)


        self.verticalLayout_32.addWidget(self.frame_47, 0, Qt.AlignTop)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_48)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_23 = QLabel(self.frame_48)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_34.addWidget(self.label_23, 0, Qt.AlignTop)

        self.inpEditarApellidos = QLineEdit(self.frame_48)
        self.inpEditarApellidos.setObjectName(u"inpEditarApellidos")
        self.inpEditarApellidos.setMinimumSize(QSize(0, 30))
        self.inpEditarApellidos.setFont(font4)
        self.inpEditarApellidos.setStyleSheet(u"QLineEdit{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_34.addWidget(self.inpEditarApellidos)


        self.verticalLayout_32.addWidget(self.frame_48, 0, Qt.AlignTop)

        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_49)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_24 = QLabel(self.frame_49)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_35.addWidget(self.label_24, 0, Qt.AlignTop)

        self.inpEditarEdad = QSpinBox(self.frame_49)
        self.inpEditarEdad.setObjectName(u"inpEditarEdad")
        self.inpEditarEdad.setFont(font4)
        self.inpEditarEdad.setStyleSheet(u"QSpinBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_35.addWidget(self.inpEditarEdad)


        self.verticalLayout_32.addWidget(self.frame_49)

        self.btnEditarPacienteSubmit = QPushButton(self.frame_46)
        self.btnEditarPacienteSubmit.setObjectName(u"btnEditarPacienteSubmit")
        self.btnEditarPacienteSubmit.setFont(font1)
        self.btnEditarPacienteSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditarPacienteSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_32.addWidget(self.btnEditarPacienteSubmit)


        self.gridLayout_15.addWidget(self.frame_46, 0, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_22, 0, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 1, 1, 1, 1)


        self.verticalLayout_36.addWidget(self.frame_45)

        self.stackedWidget.addWidget(self.pagEditarPaciente)
        self.pagAgregarCita = QWidget()
        self.pagAgregarCita.setObjectName(u"pagAgregarCita")
        self.verticalLayout_43 = QVBoxLayout(self.pagAgregarCita)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.pagAgregarCita)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setMinimumSize(QSize(0, 120))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_31.setSpacing(12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarACitas = QPushButton(self.frame_56)
        self.btnRegresarACitas.setObjectName(u"btnRegresarACitas")
        self.btnRegresarACitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarACitas.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.btnRegresarACitas.setIcon(icon12)
        self.btnRegresarACitas.setIconSize(QSize(30, 30))

        self.horizontalLayout_31.addWidget(self.btnRegresarACitas, 0, Qt.AlignLeft)

        self.lblRegresarACitas = QLabel(self.frame_56)
        self.lblRegresarACitas.setObjectName(u"lblRegresarACitas")
        sizePolicy.setHeightForWidth(self.lblRegresarACitas.sizePolicy().hasHeightForWidth())
        self.lblRegresarACitas.setSizePolicy(sizePolicy)
        self.lblRegresarACitas.setFont(font6)
        self.lblRegresarACitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarACitas.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_31.addWidget(self.lblRegresarACitas)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_28)


        self.verticalLayout_43.addWidget(self.frame_56, 0, Qt.AlignTop)

        self.frame_55 = QFrame(self.pagAgregarCita)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 70))
        self.frame_55.setMaximumSize(QSize(16777215, 264))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(40, -1, 40, -1)
        self.lblRegistroCita = QFrame(self.frame_55)
        self.lblRegistroCita.setObjectName(u"lblRegistroCita")
        self.lblRegistroCita.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblRegistroCita.setFrameShape(QFrame.StyledPanel)
        self.lblRegistroCita.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.lblRegistroCita)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_26)

        self.lblIconoRegistroCita = QPushButton(self.lblRegistroCita)
        self.lblIconoRegistroCita.setObjectName(u"lblIconoRegistroCita")
        self.lblIconoRegistroCita.setMinimumSize(QSize(30, 30))
        self.lblIconoRegistroCita.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.lblIconoRegistroCita.setIcon(icon13)
        self.lblIconoRegistroCita.setIconSize(QSize(30, 30))

        self.horizontalLayout_30.addWidget(self.lblIconoRegistroCita)

        self.lblMsjRegistroCita = QLabel(self.lblRegistroCita)
        self.lblMsjRegistroCita.setObjectName(u"lblMsjRegistroCita")
        self.lblMsjRegistroCita.setFont(font7)
        self.lblMsjRegistroCita.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_30.addWidget(self.lblMsjRegistroCita)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_27)


        self.horizontalLayout_29.addWidget(self.lblRegistroCita)


        self.verticalLayout_43.addWidget(self.frame_55, 0, Qt.AlignTop)

        self.frame_57 = QFrame(self.pagAgregarCita)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy)
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_57)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_29 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_29, 0, 0, 1, 1)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy1.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy1)
        self.frame_58.setMinimumSize(QSize(0, 0))
        self.frame_58.setSizeIncrement(QSize(0, 0))
        self.frame_58.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_58)
        self.verticalLayout_39.setSpacing(14)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_59)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_27 = QLabel(self.frame_59)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_40.addWidget(self.label_27, 0, Qt.AlignTop)

        self.inpRegistroPacienteCita = QComboBox(self.frame_59)
        self.inpRegistroPacienteCita.setObjectName(u"inpRegistroPacienteCita")
        self.inpRegistroPacienteCita.setFont(font4)
        self.inpRegistroPacienteCita.setStyleSheet(u"QComboBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_40.addWidget(self.inpRegistroPacienteCita)


        self.verticalLayout_39.addWidget(self.frame_59, 0, Qt.AlignTop)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_60)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_28 = QLabel(self.frame_60)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_41.addWidget(self.label_28, 0, Qt.AlignTop)

        self.inpRegistroMedicoCita = QComboBox(self.frame_60)
        self.inpRegistroMedicoCita.setObjectName(u"inpRegistroMedicoCita")
        self.inpRegistroMedicoCita.setFont(font4)
        self.inpRegistroMedicoCita.setStyleSheet(u"QComboBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_41.addWidget(self.inpRegistroMedicoCita)


        self.verticalLayout_39.addWidget(self.frame_60, 0, Qt.AlignTop)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_61)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_29 = QLabel(self.frame_61)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_42.addWidget(self.label_29, 0, Qt.AlignTop)

        self.inpRegistroFechaCita = QCalendarWidget(self.frame_61)
        self.inpRegistroFechaCita.setObjectName(u"inpRegistroFechaCita")
        self.inpRegistroFechaCita.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.inpRegistroFechaCita)


        self.verticalLayout_39.addWidget(self.frame_61)

        self.btnRegistroCitaSubmit = QPushButton(self.frame_58)
        self.btnRegistroCitaSubmit.setObjectName(u"btnRegistroCitaSubmit")
        self.btnRegistroCitaSubmit.setFont(font1)
        self.btnRegistroCitaSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegistroCitaSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_39.addWidget(self.btnRegistroCitaSubmit)


        self.gridLayout_16.addWidget(self.frame_58, 0, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_30, 0, 2, 1, 1)


        self.verticalLayout_43.addWidget(self.frame_57)

        self.stackedWidget.addWidget(self.pagAgregarCita)
        self.pagEditarCita = QWidget()
        self.pagEditarCita.setObjectName(u"pagEditarCita")
        self.verticalLayout = QVBoxLayout(self.pagEditarCita)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.pagEditarCita)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setMinimumSize(QSize(0, 120))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_32.setSpacing(12)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(20, 20, 20, 20)
        self.btnRegresarAgCitas = QPushButton(self.frame_62)
        self.btnRegresarAgCitas.setObjectName(u"btnRegresarAgCitas")
        self.btnRegresarAgCitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRegresarAgCitas.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"}")
        self.btnRegresarAgCitas.setIcon(icon12)
        self.btnRegresarAgCitas.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.btnRegresarAgCitas, 0, Qt.AlignLeft)

        self.lblRegresarAgCitas = QLabel(self.frame_62)
        self.lblRegresarAgCitas.setObjectName(u"lblRegresarAgCitas")
        sizePolicy.setHeightForWidth(self.lblRegresarAgCitas.sizePolicy().hasHeightForWidth())
        self.lblRegresarAgCitas.setSizePolicy(sizePolicy)
        self.lblRegresarAgCitas.setFont(font6)
        self.lblRegresarAgCitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblRegresarAgCitas.setStyleSheet(u"QLabel{\n"
"	color: #3E3E3E;\n"
"}")

        self.horizontalLayout_32.addWidget(self.lblRegresarAgCitas)

        self.label_2 = QLabel(self.frame_62)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	margin-left: 20px;\n"
"}")

        self.horizontalLayout_32.addWidget(self.label_2)

        self.lblEditarCitaActual = QLabel(self.frame_62)
        self.lblEditarCitaActual.setObjectName(u"lblEditarCitaActual")
        self.lblEditarCitaActual.setFont(font8)

        self.horizontalLayout_32.addWidget(self.lblEditarCitaActual)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_31)


        self.verticalLayout.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.pagEditarCita)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 70))
        self.frame_63.setMaximumSize(QSize(16777215, 264))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(40, -1, 40, -1)
        self.lblEditarCita = QFrame(self.frame_63)
        self.lblEditarCita.setObjectName(u"lblEditarCita")
        self.lblEditarCita.setStyleSheet(u"QFrame{\n"
"	background-color: #22c55e;\n"
"	border-radius: 5px;\n"
"}")
        self.lblEditarCita.setFrameShape(QFrame.StyledPanel)
        self.lblEditarCita.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.lblEditarCita)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_32)

        self.lblIconoEditarCita = QPushButton(self.lblEditarCita)
        self.lblIconoEditarCita.setObjectName(u"lblIconoEditarCita")
        self.lblIconoEditarCita.setMinimumSize(QSize(30, 30))
        self.lblIconoEditarCita.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.lblIconoEditarCita.setIcon(icon13)
        self.lblIconoEditarCita.setIconSize(QSize(30, 30))

        self.horizontalLayout_34.addWidget(self.lblIconoEditarCita)

        self.lblMsjEditarCita = QLabel(self.lblEditarCita)
        self.lblMsjEditarCita.setObjectName(u"lblMsjEditarCita")
        self.lblMsjEditarCita.setFont(font7)
        self.lblMsjEditarCita.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_34.addWidget(self.lblMsjEditarCita)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_33)


        self.horizontalLayout_33.addWidget(self.lblEditarCita)


        self.verticalLayout.addWidget(self.frame_63, 0, Qt.AlignTop)

        self.frame_64 = QFrame(self.pagEditarCita)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy)
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_64)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_34 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_34, 0, 0, 1, 1)

        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy1.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy1)
        self.frame_65.setMinimumSize(QSize(0, 0))
        self.frame_65.setSizeIncrement(QSize(0, 0))
        self.frame_65.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #737373;\n"
"	border-radius: 8px;\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_65)
        self.verticalLayout_44.setSpacing(14)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_66)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_30 = QLabel(self.frame_66)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_45.addWidget(self.label_30, 0, Qt.AlignTop)

        self.inpEditarPacienteCita = QComboBox(self.frame_66)
        self.inpEditarPacienteCita.setObjectName(u"inpEditarPacienteCita")
        self.inpEditarPacienteCita.setFont(font4)
        self.inpEditarPacienteCita.setStyleSheet(u"QComboBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_45.addWidget(self.inpEditarPacienteCita)


        self.verticalLayout_44.addWidget(self.frame_66, 0, Qt.AlignTop)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_67)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_31 = QLabel(self.frame_67)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_46.addWidget(self.label_31, 0, Qt.AlignTop)

        self.inpEditarMedicoCita = QComboBox(self.frame_67)
        self.inpEditarMedicoCita.setObjectName(u"inpEditarMedicoCita")
        self.inpEditarMedicoCita.setFont(font4)
        self.inpEditarMedicoCita.setStyleSheet(u"QComboBox{\n"
"	padding: 4px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #57534e;\n"
"	color: #404040;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")

        self.verticalLayout_46.addWidget(self.inpEditarMedicoCita)


        self.verticalLayout_44.addWidget(self.frame_67, 0, Qt.AlignTop)

        self.frame_68 = QFrame(self.frame_65)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_68)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_32 = QLabel(self.frame_68)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"QLabel{\n"
"	color: #404040;\n"
"}")

        self.verticalLayout_47.addWidget(self.label_32, 0, Qt.AlignTop)

        self.inpEditarFechaCita = QCalendarWidget(self.frame_68)
        self.inpEditarFechaCita.setObjectName(u"inpEditarFechaCita")
        self.inpEditarFechaCita.setStyleSheet(u"#inpEditarFechaCita QToolButton QMenu::item:selected:enabled{\n"
"	background-color: #55aaff;\n"
"}\n"
"\n"
"#inpEditarFechaCita QAbstractItemView:enabled{\n"
"	selection-background-color: #0284c7;\n"
"	selection-color: #fff;\n"
"}")

        self.verticalLayout_47.addWidget(self.inpEditarFechaCita)


        self.verticalLayout_44.addWidget(self.frame_68)

        self.btnEditarCitaSubmit = QPushButton(self.frame_65)
        self.btnEditarCitaSubmit.setObjectName(u"btnEditarCitaSubmit")
        self.btnEditarCitaSubmit.setFont(font1)
        self.btnEditarCitaSubmit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditarCitaSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: #3b82f6;\n"
"	padding: 12px;\n"
"	border-radius: 8px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #2563eb;\n"
"}")

        self.verticalLayout_44.addWidget(self.btnEditarCitaSubmit)


        self.gridLayout_17.addWidget(self.frame_65, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_35, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_64)

        self.stackedWidget.addWidget(self.pagEditarCita)

        self.gridLayout_10.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hopital Blabla", None))
        self.pushButton_10.setText("")
        self.lblLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hospital<br/>Blabla</p></body></html>", None))
        self.btnMenu.setText("")
        self.pushButton_6.setText("")
        self.lblUsuarios.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.pushButton_7.setText("")
        self.lblPacientes.setText(QCoreApplication.translate("MainWindow", u"Pacientes", None))
        self.pushButton_8.setText("")
        self.lblCitas.setText(QCoreApplication.translate("MainWindow", u"Citas", None))
        self.pushButton_9.setText("")
        self.lblAnalisis.setText(QCoreApplication.translate("MainWindow", u"Analisis", None))
        self.pushButton_11.setText("")
        self.lblSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.lblBienvenenida.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.pushButton_13.setText("")
        self.lblUsuarios_3.setText(QCoreApplication.translate("MainWindow", u"Pacientes:", None))
        self.lblContadorPacientes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText("")
        self.lblUsuarios_2.setText(QCoreApplication.translate("MainWindow", u"Usuarios:", None))
        self.lblContadorUsuarios.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_14.setText("")
        self.lblUsuarios_4.setText(QCoreApplication.translate("MainWindow", u"Citas:", None))
        self.lblContadorCitas.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_15.setText("")
        self.lblBienvenenida_2.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.btnAgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"      Agregar Usuario", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.inpUsuariosBusqueda.setText("")
        ___qtablewidgetitem = self.tblUsuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tblUsuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nickname", None));
        ___qtablewidgetitem2 = self.tblUsuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Rol", None));
        ___qtablewidgetitem3 = self.tblUsuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Editar", None));
        ___qtablewidgetitem4 = self.tblUsuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None));
        self.pushButton_16.setText("")
        self.lblBienvenenida_3.setText(QCoreApplication.translate("MainWindow", u"Pacientes", None))
        self.btnAgregarPaciente.setText(QCoreApplication.translate("MainWindow", u"      Agregar Paciente", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.inpBusquedaPacientes.setText("")
        ___qtablewidgetitem5 = self.tblPacientes.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tblPacientes.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem7 = self.tblPacientes.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None));
        ___qtablewidgetitem8 = self.tblPacientes.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem9 = self.tblPacientes.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Editar", None));
        ___qtablewidgetitem10 = self.tblPacientes.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None));
        self.pushButton_17.setText("")
        self.lblBienvenenida_4.setText(QCoreApplication.translate("MainWindow", u"Citas", None))
        self.btnAgregarCita.setText(QCoreApplication.translate("MainWindow", u"      Agendar Cita", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.inpBusquedaCitas.setText("")
        ___qtablewidgetitem11 = self.tblCitas.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tblCitas.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem13 = self.tblCitas.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Medico", None));
        ___qtablewidgetitem14 = self.tblCitas.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem15 = self.tblCitas.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Editar", None));
        ___qtablewidgetitem16 = self.tblCitas.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None));
        self.pushButton_18.setText("")
        self.lblBienvenenida_5.setText(QCoreApplication.translate("MainWindow", u"Analisis", None))
        self.btnAgregarCita_2.setText(QCoreApplication.translate("MainWindow", u"      Agendar Cita", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.inpBusquedaCitas_2.setText("")
        ___qtablewidgetitem17 = self.tblCitas_2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.tblCitas_2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem19 = self.tblCitas_2.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Medico", None));
        ___qtablewidgetitem20 = self.tblCitas_2.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem21 = self.tblCitas_2.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Editar", None));
        ___qtablewidgetitem22 = self.tblCitas_2.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None));
        self.btnRegresarAUsuarios.setText("")
        self.lblRegresarAgUsuarios.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.lblIconoRegistroUsuario.setText("")
        self.lblMsjRegistroUsuario.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.inpRegistroNick.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rol", None))
        self.btnRegistroSubmit.setText(QCoreApplication.translate("MainWindow", u"Registrar usuario", None))
        self.btnRegresarAUsuarios2.setText("")
        self.lblRegresarAgUsuarios2.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Editando Usuario: ", None))
        self.lblEditarUsuarioActual.setText("")
        self.lblIconoEditarUsuario.setText("")
        self.lblMsjEditarUsuario.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.inpEditarNick.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Rol", None))
        self.btnEditarSubmit.setText(QCoreApplication.translate("MainWindow", u"Guardar Cambios", None))
        self.btnRegresarAPacientes.setText("")
        self.lblRegresarAPacientes.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.lblIconoRegistroPaciente.setText("")
        self.lblMsjRegistroPaciente.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.inpRegistroNombre.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.btnRegistroPacienteSubmit.setText(QCoreApplication.translate("MainWindow", u"Registrar usuario", None))
        self.btnRegresarAgPacientes.setText("")
        self.lblRegresarAgPacientes.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Editando Paciente: ", None))
        self.lblEditarPacienteActual.setText("")
        self.lblIconoEditarPaciente.setText("")
        self.lblMsjEditarPaciente.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.inpEditarNombre.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.btnEditarPacienteSubmit.setText(QCoreApplication.translate("MainWindow", u"Guardar Cambios", None))
        self.btnRegresarACitas.setText("")
        self.lblRegresarACitas.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.lblIconoRegistroCita.setText("")
        self.lblMsjRegistroCita.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Paciente", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Medico", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.btnRegistroCitaSubmit.setText(QCoreApplication.translate("MainWindow", u"Agendar Cita", None))
        self.btnRegresarAgCitas.setText("")
        self.lblRegresarAgCitas.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Editando Cita:", None))
        self.lblEditarCitaActual.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblIconoEditarCita.setText("")
        self.lblMsjEditarCita.setText(QCoreApplication.translate("MainWindow", u"Registro realizado exitosamente", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Paciente", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Medico", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.btnEditarCitaSubmit.setText(QCoreApplication.translate("MainWindow", u"Cambiar Cita", None))
    # retranslateUi

