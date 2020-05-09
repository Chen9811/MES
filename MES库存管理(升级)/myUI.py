# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QwareHouse(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.dealdate = QtWidgets.QDateEdit(self.tab)
        self.dealdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 4, 20), QtCore.QTime(0, 0, 0)))
        self.dealdate.setCalendarPopup(True)
        self.dealdate.setDate(QtCore.QDate(2020, 4, 20))
        self.dealdate.setObjectName("dealdate")
        self.horizontalLayout.addWidget(self.dealdate)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.enterKind_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.enterKind_comboBox.setObjectName("enterKind_comboBox")
        self.enterKind_comboBox.addItem("")
        self.enterKind_comboBox.addItem("")
        self.enterKind_comboBox.addItem("")
        self.enterKind_comboBox.addItem("")
        self.enterKind_comboBox.addItem("")
        self.enterKind_comboBox.addItem("")
        self.verticalLayout.addWidget(self.enterKind_comboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.enterNum_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.enterNum_spinBox.setMinimum(1)
        self.enterNum_spinBox.setMaximum(999)
        self.enterNum_spinBox.setObjectName("enterNum_spinBox")
        self.verticalLayout_2.addWidget(self.enterNum_spinBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.enterList_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.enterList_pushButton.setObjectName("enterList_pushButton")
        self.horizontalLayout_5.addWidget(self.enterList_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.enterScan_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.enterScan_pushButton.setObjectName("enterScan_pushButton")
        self.verticalLayout_3.addWidget(self.enterScan_pushButton)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.outKind_comboBox_2 = QtWidgets.QLabel(self.groupBox_3)
        self.outKind_comboBox_2.setObjectName("outKind_comboBox_2")
        self.verticalLayout_5.addWidget(self.outKind_comboBox_2)
        self.outKind_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.outKind_comboBox.setObjectName("outKind_comboBox")
        self.outKind_comboBox.addItem("")
        self.outKind_comboBox.addItem("")
        self.outKind_comboBox.addItem("")
        self.outKind_comboBox.addItem("")
        self.outKind_comboBox.addItem("")
        self.outKind_comboBox.addItem("")
        self.verticalLayout_5.addWidget(self.outKind_comboBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.outNum_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.outNum_spinBox.setMinimum(1)
        self.outNum_spinBox.setMaximum(999)
        self.outNum_spinBox.setObjectName("outNum_spinBox")
        self.verticalLayout_6.addWidget(self.outNum_spinBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.outList_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.outList_pushButton.setObjectName("outList_pushButton")
        self.horizontalLayout_6.addWidget(self.outList_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.outScan_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.outScan_pushButton.setObjectName("outScan_pushButton")
        self.verticalLayout_4.addWidget(self.outScan_pushButton)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.confirmDeal_pushButton = QtWidgets.QPushButton(self.tab)
        self.confirmDeal_pushButton.setObjectName("confirmDeal_pushButton")
        self.verticalLayout_7.addWidget(self.confirmDeal_pushButton)
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_7.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.VICEtableView = QtWidgets.QTableView(self.tab_5)
        self.VICEtableView.setObjectName("VICEtableView")
        self.gridLayout_6.addWidget(self.VICEtableView, 0, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.RFIDlineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.RFIDlineEdit.setEnabled(True)
        self.RFIDlineEdit.setMinimumSize(QtCore.QSize(320, 0))
        self.RFIDlineEdit.setObjectName("RFIDlineEdit")
        self.horizontalLayout_4.addWidget(self.RFIDlineEdit)
        spacerItem6 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.emitPushButton = QtWidgets.QPushButton(self.tab_5)
        self.emitPushButton.setObjectName("emitPushButton")
        self.horizontalLayout_4.addWidget(self.emitPushButton)
        self.ScanPushButton = QtWidgets.QPushButton(self.tab_5)
        self.ScanPushButton.setObjectName("ScanPushButton")
        self.horizontalLayout_4.addWidget(self.ScanPushButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(276, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.current_tableView = QtWidgets.QTableView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.current_tableView.sizePolicy().hasHeightForWidth())
        self.current_tableView.setSizePolicy(sizePolicy)
        self.current_tableView.setObjectName("current_tableView")
        self.gridLayout_3.addWidget(self.current_tableView, 0, 0, 3, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 2, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 1, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 0, 2, 1, 1)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.currentComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.currentComboBox.setObjectName("currentComboBox")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.currentComboBox.addItem("")
        self.verticalLayout_9.addWidget(self.currentComboBox)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.batchCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.batchCheckBox.setObjectName("batchCheckBox")
        self.verticalLayout_10.addWidget(self.batchCheckBox)
        self.batchSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.batchSpinBox.setMinimum(1)
        self.batchSpinBox.setObjectName("batchSpinBox")
        self.verticalLayout_10.addWidget(self.batchSpinBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_10.addWidget(self.progressBar)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_22.addWidget(self.groupBox_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem12)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pie_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.pie_radioButton.setChecked(True)
        self.pie_radioButton.setObjectName("pie_radioButton")
        self.verticalLayout_8.addWidget(self.pie_radioButton)
        self.bar_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.bar_radioButton.setEnabled(True)
        self.bar_radioButton.setChecked(False)
        self.bar_radioButton.setObjectName("bar_radioButton")
        self.verticalLayout_8.addWidget(self.bar_radioButton)
        self.drawCurrent_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.drawCurrent_pushButton.setObjectName("drawCurrent_pushButton")
        self.verticalLayout_8.addWidget(self.drawCurrent_pushButton)
        self.delete_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.verticalLayout_8.addWidget(self.delete_pushButton)
        self.verticalLayout_22.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.verticalLayout_22, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_13.addWidget(self.label_18)
        self.enterComboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.enterComboBox.setObjectName("enterComboBox")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.enterComboBox.addItem("")
        self.verticalLayout_13.addWidget(self.enterComboBox)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.enterCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.enterCheckBox.setObjectName("enterCheckBox")
        self.verticalLayout_14.addWidget(self.enterCheckBox)
        self.enterDate = QtWidgets.QDateEdit(self.groupBox_5)
        self.enterDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 4, 20), QtCore.QTime(0, 0, 0)))
        self.enterDate.setCalendarPopup(True)
        self.enterDate.setDate(QtCore.QDate(2020, 4, 20))
        self.enterDate.setObjectName("enterDate")
        self.verticalLayout_14.addWidget(self.enterDate)
        self.verticalLayout_12.addLayout(self.verticalLayout_14)
        self.verticalLayout_23.addWidget(self.groupBox_5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(spacerItem13)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.drawEnter_pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.drawEnter_pushButton.setObjectName("drawEnter_pushButton")
        self.verticalLayout_16.addWidget(self.drawEnter_pushButton)
        self.verticalLayout_23.addWidget(self.groupBox_6)
        self.gridLayout_5.addLayout(self.verticalLayout_23, 3, 2, 1, 1)
        self.enter_tableView = QtWidgets.QTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.enter_tableView.sizePolicy().hasHeightForWidth())
        self.enter_tableView.setSizePolicy(sizePolicy)
        self.enter_tableView.setObjectName("enter_tableView")
        self.gridLayout_5.addWidget(self.enter_tableView, 0, 0, 7, 1)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 3, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem15, 4, 2, 3, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem16, 0, 2, 3, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.out_tableView = QtWidgets.QTableView(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.out_tableView.sizePolicy().hasHeightForWidth())
        self.out_tableView.setSizePolicy(sizePolicy)
        self.out_tableView.setObjectName("out_tableView")
        self.gridLayout_4.addWidget(self.out_tableView, 0, 0, 5, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem17, 3, 2, 2, 1)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_19 = QtWidgets.QLabel(self.groupBox_10)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_20.addWidget(self.label_19)
        self.outComboBox = QtWidgets.QComboBox(self.groupBox_10)
        self.outComboBox.setObjectName("outComboBox")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.outComboBox.addItem("")
        self.verticalLayout_20.addWidget(self.outComboBox)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.outCheckBox = QtWidgets.QCheckBox(self.groupBox_10)
        self.outCheckBox.setObjectName("outCheckBox")
        self.verticalLayout_21.addWidget(self.outCheckBox)
        self.outDate = QtWidgets.QDateEdit(self.groupBox_10)
        self.outDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 4, 20), QtCore.QTime(0, 0, 0)))
        self.outDate.setCalendarPopup(True)
        self.outDate.setDate(QtCore.QDate(2020, 4, 20))
        self.outDate.setObjectName("outDate")
        self.verticalLayout_21.addWidget(self.outDate)
        self.verticalLayout_19.addLayout(self.verticalLayout_21)
        self.verticalLayout_24.addWidget(self.groupBox_10)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem18)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.drawOut_pushButton = QtWidgets.QPushButton(self.groupBox_8)
        self.drawOut_pushButton.setObjectName("drawOut_pushButton")
        self.verticalLayout_17.addWidget(self.drawOut_pushButton)
        self.verticalLayout_24.addWidget(self.groupBox_8)
        self.gridLayout_4.addLayout(self.verticalLayout_24, 2, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 2, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem20, 0, 2, 2, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "西交库存管理系统"))
        self.label_17.setText(_translate("MainWindow", "操作日期"))
        self.dealdate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.groupBox_2.setTitle(_translate("MainWindow", "入库信息填写"))
        self.label_2.setText(_translate("MainWindow", "工件类型"))
        self.enterKind_comboBox.setItemText(0, _translate("MainWindow", "直齿轮"))
        self.enterKind_comboBox.setItemText(1, _translate("MainWindow", "斜齿轮"))
        self.enterKind_comboBox.setItemText(2, _translate("MainWindow", "光轴"))
        self.enterKind_comboBox.setItemText(3, _translate("MainWindow", "齿轮轴"))
        self.enterKind_comboBox.setItemText(4, _translate("MainWindow", "曲柄"))
        self.enterKind_comboBox.setItemText(5, _translate("MainWindow", "摇杆"))
        self.label.setText(_translate("MainWindow", "工件数量"))
        self.enterList_pushButton.setText(_translate("MainWindow", "添加至入库单"))
        self.enterScan_pushButton.setText(_translate("MainWindow", "扫码入库"))
        self.groupBox_3.setTitle(_translate("MainWindow", "出库信息填写"))
        self.outKind_comboBox_2.setText(_translate("MainWindow", "工件类型"))
        self.outKind_comboBox.setItemText(0, _translate("MainWindow", "直齿轮"))
        self.outKind_comboBox.setItemText(1, _translate("MainWindow", "斜齿轮"))
        self.outKind_comboBox.setItemText(2, _translate("MainWindow", "光轴"))
        self.outKind_comboBox.setItemText(3, _translate("MainWindow", "齿轮轴"))
        self.outKind_comboBox.setItemText(4, _translate("MainWindow", "曲柄"))
        self.outKind_comboBox.setItemText(5, _translate("MainWindow", "摇杆"))
        self.label_7.setText(_translate("MainWindow", "工件数量"))
        self.outList_pushButton.setText(_translate("MainWindow", "添加至出库单"))
        self.outScan_pushButton.setText(_translate("MainWindow", "扫码出库"))
        self.confirmDeal_pushButton.setText(_translate("MainWindow", "确认操作"))
        self.label_8.setText(_translate("MainWindow", "提示信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主操作界面"))
        self.label_3.setText(_translate("MainWindow", "RFID"))
        self.emitPushButton.setText(_translate("MainWindow", "单件扫描"))
        self.ScanPushButton.setText(_translate("MainWindow", "多件扫描"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "副操作界面"))
        self.groupBox_4.setTitle(_translate("MainWindow", "数据过滤"))
        self.label_16.setText(_translate("MainWindow", "工件种类"))
        self.currentComboBox.setItemText(0, _translate("MainWindow", "全选"))
        self.currentComboBox.setItemText(1, _translate("MainWindow", "直齿轮"))
        self.currentComboBox.setItemText(2, _translate("MainWindow", "斜齿轮"))
        self.currentComboBox.setItemText(3, _translate("MainWindow", "光轴"))
        self.currentComboBox.setItemText(4, _translate("MainWindow", "齿轮轴"))
        self.currentComboBox.setItemText(5, _translate("MainWindow", "曲柄"))
        self.currentComboBox.setItemText(6, _translate("MainWindow", "摇杆"))
        self.batchCheckBox.setText(_translate("MainWindow", "批次"))
        self.label_5.setText(_translate("MainWindow", "已用库存"))
        self.groupBox.setTitle(_translate("MainWindow", "数据可视化"))
        self.pie_radioButton.setText(_translate("MainWindow", "饼图"))
        self.bar_radioButton.setText(_translate("MainWindow", "柱状图"))
        self.drawCurrent_pushButton.setText(_translate("MainWindow", "绘制"))
        self.delete_pushButton.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "现有库存"))
        self.groupBox_5.setTitle(_translate("MainWindow", "数据过滤"))
        self.label_18.setText(_translate("MainWindow", "工件种类"))
        self.enterComboBox.setItemText(0, _translate("MainWindow", "全选"))
        self.enterComboBox.setItemText(1, _translate("MainWindow", "直齿轮"))
        self.enterComboBox.setItemText(2, _translate("MainWindow", "斜齿轮"))
        self.enterComboBox.setItemText(3, _translate("MainWindow", "光轴"))
        self.enterComboBox.setItemText(4, _translate("MainWindow", "齿轮轴"))
        self.enterComboBox.setItemText(5, _translate("MainWindow", "曲柄"))
        self.enterComboBox.setItemText(6, _translate("MainWindow", "摇杆"))
        self.enterCheckBox.setText(_translate("MainWindow", "日期"))
        self.enterDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.groupBox_6.setTitle(_translate("MainWindow", "入库记录可视化"))
        self.drawEnter_pushButton.setText(_translate("MainWindow", "绘制"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "入库记录"))
        self.groupBox_10.setTitle(_translate("MainWindow", "数据过滤"))
        self.label_19.setText(_translate("MainWindow", "工件种类"))
        self.outComboBox.setItemText(0, _translate("MainWindow", "全选"))
        self.outComboBox.setItemText(1, _translate("MainWindow", "直齿轮"))
        self.outComboBox.setItemText(2, _translate("MainWindow", "斜齿轮"))
        self.outComboBox.setItemText(3, _translate("MainWindow", "光轴"))
        self.outComboBox.setItemText(4, _translate("MainWindow", "齿轮轴"))
        self.outComboBox.setItemText(5, _translate("MainWindow", "曲柄"))
        self.outComboBox.setItemText(6, _translate("MainWindow", "摇杆"))
        self.outCheckBox.setText(_translate("MainWindow", "日期"))
        self.outDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.groupBox_8.setTitle(_translate("MainWindow", "出库记录可视化"))
        self.drawOut_pushButton.setText(_translate("MainWindow", "绘制"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "出库记录"))
from warehouse import QwareHouse
