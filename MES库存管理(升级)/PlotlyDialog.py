# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plotly_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 674)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.qwebengine = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.qwebengine.setAutoFillBackground(False)
        self.qwebengine.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.qwebengine.setObjectName("qwebengine")
        self.gridLayout.addWidget(self.qwebengine, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Demo"))
from PyQt5 import QtWebEngineWidgets
