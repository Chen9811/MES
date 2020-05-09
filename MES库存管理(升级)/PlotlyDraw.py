# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PlotlyDialog import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DemoWindow(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, filename):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super().__init__()
        self.setupUi(self)

        self.filename=filename
        self.qwebengine.setGeometry(QRect(50, 20, 1200, 600))
        self.qwebengine.load(QUrl.fromLocalFile(self.filename))