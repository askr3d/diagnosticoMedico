# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deletewindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        if not DeleteWindow.objectName():
            DeleteWindow.setObjectName(u"DeleteWindow")
        DeleteWindow.resize(431, 201)
        DeleteWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #f3f4f6;\n"
"}")
        self.verticalLayout = QVBoxLayout(DeleteWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(DeleteWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.lblEliminarRegistroID = QLabel(self.frame)
        self.lblEliminarRegistroID.setObjectName(u"lblEliminarRegistroID")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.lblEliminarRegistroID.setFont(font1)
        self.lblEliminarRegistroID.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblEliminarRegistroID)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(DeleteWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnEliminarAceptar = QPushButton(self.frame_2)
        self.btnEliminarAceptar.setObjectName(u"btnEliminarAceptar")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnEliminarAceptar.setFont(font2)
        self.btnEliminarAceptar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarAceptar.setStyleSheet(u"QPushButton{\n"
"	background-color: #22c55e;\n"
"	color: #fff;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #16a34a;\n"
"}")

        self.verticalLayout_3.addWidget(self.btnEliminarAceptar)

        self.btnEliminarCancelar = QPushButton(self.frame_2)
        self.btnEliminarCancelar.setObjectName(u"btnEliminarCancelar")
        self.btnEliminarCancelar.setFont(font2)
        self.btnEliminarCancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarCancelar.setStyleSheet(u"QPushButton{\n"
"	background-color: #ef4444;\n"
"	color: #fff;\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #dc2626;\n"
"}")

        self.verticalLayout_3.addWidget(self.btnEliminarCancelar)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(DeleteWindow)

        QMetaObject.connectSlotsByName(DeleteWindow)
    # setupUi

    def retranslateUi(self, DeleteWindow):
        DeleteWindow.setWindowTitle(QCoreApplication.translate("DeleteWindow", u"Eliminar Registro", None))
        self.label.setText(QCoreApplication.translate("DeleteWindow", u"\u00bfSeguro que quieres eliminar el registro?", None))
        self.lblEliminarRegistroID.setText(QCoreApplication.translate("DeleteWindow", u"ID: 00", None))
        self.btnEliminarAceptar.setText(QCoreApplication.translate("DeleteWindow", u"Aceptar", None))
        self.btnEliminarCancelar.setText(QCoreApplication.translate("DeleteWindow", u"Cancelar", None))
    # retranslateUi

