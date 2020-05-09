from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QAbstractItemView, QMessageBox, QDataWidgetMapper)
from PyQt5.QtCore import (pyqtSlot, Qt, QItemSelectionModel,
                          QModelIndex, QFile, QIODevice, QDate)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery, QSqlQueryModel
from PlotlyDraw import DemoWindow
from myUI import Ui_MainWindow
import plotly.graph_objs as go
import plotly.offline as pyof
from collections import Counter
import numpy as np
import time
import sys
import os


# 在这里去绑定相应的signal和slot，实现业务逻辑
class MainWindow(QMainWindow):  # 继承主窗口函数的类, 继承编写的主函数
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化运行A窗口类下的 setupUi 函数
        self.open_alltable()
        self.enterList = {}
        self.outList = {}
        self.name_RFID = {'直齿轮': '01B0E00000020010B1', '斜齿轮': '01B0E00000030010B2',
                          '齿轮轴': '01A0E00000010010A1', '光轴': '01A0E00000010010A2',
                          '曲柄': '01C0E00000020010C1', '摇杆': '01C0E00000010010C2'}
        self.RFID_kind = dict([(value, key) for (key, value) in self.name_RFID.items()])
        self.capacity = {'直齿轮': 18, '斜齿轮': 18, '齿轮轴': 24, '光轴': 24, '曲柄': 36, '摇杆': 36}
        self.nameNum = {'直齿轮': 3, '斜齿轮': 3, '齿轮轴': 4, '光轴': 4, '曲柄': 6, '摇杆': 6}
        self.locateName = {'直齿轮': ['A', 'B', 1], '斜齿轮': ['C', 'D', 1], '齿轮轴': ['A', 'B', 2],
                           '光轴': ['C', 'D', 2], '曲柄': ['A', 'B', 3], '摇杆': ['C', 'D', 3]}
        self.get_locState()  # 获取所有货位的空闲状态
        # 初始化出入库按钮使能状态
        self.ui.outScan_pushButton.setEnabled(False)
        self.ui.enterScan_pushButton.setEnabled(False)
        self.currentList = self.Absolute_statis('current')  # 获取入库记录里各种工件的数量
        print(self.currentList)

    def open_alltable(self):
        ##   tableView显示属性设置
        self.ui.current_tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.current_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.current_tableView.setAlternatingRowColors(True)  # 设置相邻记录的不同颜色
        self.ui.current_tableView.verticalHeader().setDefaultSectionSize(22)  # 单元格高度
        self.ui.current_tableView.horizontalHeader().setDefaultSectionSize(160)  # 单元格宽度

        self.ui.enter_tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.enter_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.enter_tableView.setAlternatingRowColors(True)  # 设置相邻记录的不同颜色
        self.ui.enter_tableView.verticalHeader().setDefaultSectionSize(22)  # 单元格高度
        self.ui.enter_tableView.horizontalHeader().setDefaultSectionSize(160)  # 单元格宽度

        self.ui.out_tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.out_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.out_tableView.setAlternatingRowColors(True)  # 设置相邻记录的不同颜色
        self.ui.out_tableView.verticalHeader().setDefaultSectionSize(22)  # 单元格高度
        self.ui.out_tableView.horizontalHeader().setDefaultSectionSize(160)  # 单元格宽度

        self.ui.VICEtableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.VICEtableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.VICEtableView.setAlternatingRowColors(True)  # 设置相邻记录的不同颜色
        self.ui.VICEtableView.verticalHeader().setDefaultSectionSize(22)  # 单元格高度
        self.ui.VICEtableView.horizontalHeader().setDefaultSectionSize(240)  # 单元格宽度

        # 连接到数据库并打开
        self.DB = QSqlDatabase.addDatabase('QSQLITE')  # 建立与数据库的连接，即QSqlDatabase对象
        self.DB.setDatabaseName('MES5.db')  # 设置数据库名称
        self.DB.open()  # 打开数据库
        print('数据库打开成功')
        ## 打开现有库存数据表
        self.current_tabModel = QSqlTableModel(self, self.DB)  # 创建数据表的模型
        self.current_tabModel.setTable('工件信息表')  # 设置需要连接的数据表
        self.current_tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        ## 打开入库记录表
        self.enter_tabModel = QSqlTableModel(self, self.DB)  # 创建数据表的模型
        self.enter_tabModel.setTable('入库记录表')  # 设置需要连接的数据表
        self.enter_tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        ## 打开出库记录表
        self.out_tabModel = QSqlTableModel(self, self.DB)  # 创建数据表的模型
        self.out_tabModel.setTable('出库记录表')  # 设置需要连接的数据表
        self.out_tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

        ## 打开固定批RFID表========================================================
        self.vice_tabModel = QSqlTableModel(self, self.DB)  # 创建数据表的模型
        self.vice_tabModel.setTable('新建表')  # 设置需要连接的数据表
        self.vice_tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.ui.VICEtableView.setModel(self.vice_tabModel)  # 为一个QTableView组件设置一个QSqlTabelModel模型
        self.vice_tabModel.select()
        # 建立RFID与组件的映射关系
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.vice_tabModel)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)

        ##界面组件与tabelmodel的具体字段之间的联系
        self.mapper.addMapping(self.ui.RFIDlineEdit, 0)
        self.mapper.toFirst()  # 移动到首记录

        # 选中数据时信号的发射
        self.selModel = QItemSelectionModel(self.vice_tabModel)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)
        self.ui.VICEtableView.setSelectionModel(self.selModel)  # 设置选择模型
        # ===============================================================================

        self.refresh()
        print('数据表打开成功')

        ##获取字段名和序号的字典数据
        empty = self.current_tabModel.record()  # 得到的是一个空的记录，获取表的字段定义
        self.fldNum = {}
        for i in range(empty.count()):
            filedname = empty.fieldName(i)
            empty.field(filedname).setReadOnly(True)  # 每个字段设置为只读
            self.fldNum.setdefault(filedname, i)  # 如果字典中包含有给定键，则返回该键对应的值，否则将键添加到字典中，默认值为None
        print(self.fldNum)
        print(self.current_tabModel.record().count())

    def do_currentRowChanged(self, current):
        self.mapper.setCurrentIndex(current.row())

    def refresh(self):
        self.ui.current_tableView.setModel(self.current_tabModel)
        self.current_tabModel.select()
        self.ui.enter_tableView.setModel(self.enter_tabModel)  # 为一个QTableView组件设置一个QSqlTabelModel模型
        self.enter_tabModel.select()
        self.ui.out_tableView.setModel(self.out_tabModel)  # 为一个QTableView组件设置一个QSqlTabelModel模型
        self.out_tabModel.select()
        self.inventory_used()

    #################################路径规划与货位分配###########################################
    def get_locState(self):  # 获取所有货位的状态
        self.locationState = {}
        DecodeLoc = {'A': 0, 'B': 1, 'C': 0, 'D': 1}  # 解码字典
        for key, value in self.nameNum.items():
            self.locationState[key] = np.zeros((2, 3, value), dtype=int)
        if self.current_tabModel.record(0).isNull('货位') == True:
            pass
        else:
            currentRow = self.current_tabModel.rowCount()  # 库存的已记录数
            # 根据现有库存更新货位的状态
            for i in range(currentRow):
                curRec = self.current_tabModel.record(i)
                location = curRec.value('货位')
                kindname = curRec.value('种类')
                x = DecodeLoc[location[0]]  # 对已有的工件的货位编码进行解码
                y = int(location[1]) - 1
                z = int(location[5]) - 1
                self.locationState[kindname][x][y][z] = 1
    #货位分配函数
    def allocation(self, name, num, label):  # 输入工件名称和对应的数量
        if label == 'i':
            sign = 0
        else:
            sign = 1
        itsloc = self.locationState[name]
        for i in range(3):
            data = itsloc[:, 0:i + 1]
            data=data.reshape(1,-1)[0]
            itsum = sum(data == sign)
            if itsum >= num:
                forward_double = i + 1
                break
        idle_loc = np.where(itsloc[:, 0:forward_double] == sign)  # 寻找前forward_double对货架的空闲货位
        locating = []  # 存放接收工件的货位
        for i in range(num):
            x = idle_loc[0][i]
            y = idle_loc[1][i]
            z = idle_loc[2][i]
            self.locationState[name][x][y][z] = 1 - sign  # 分配好后即更新货位状态
            locating.append([x, y, z])
        EncodeLoc = []
        for i in locating:
            s = self.locateName[name][i[0]] + str(i[1] + 1) + '-' + \
                str(self.locateName[name][2]) + '-' + str(i[2] + 1)
            EncodeLoc.append(s)
        return EncodeLoc, forward_double

    def getLocation(self, outList, direct):
        ALLlocation = []
        forwardLocation = {}
        for key, value in outList.items():
            location, position = self.allocation(key, value,direct)
            ALLlocation = ALLlocation + location
            forwardLocation[key] = position - 1
        return ALLlocation, forwardLocation
    # 表里的工件统计
    def statistics(self, model):
        n = model.rowCount()  # 总行数
        all_list = {}
        for i in range(n):  # 统计入库记录里各种工件的数量
            rec = model.record(i)
            if rec.value('种类') in all_list:
                all_list[rec.value('种类')] += 1
            else:
                all_list[rec.value('种类')] = 1
        return all_list
    def Absolute_statis(self,label):
        myModel = QSqlQueryModel(self)
        if label=='current':
            myModel.setQuery("select 种类 from 工件信息表")
        elif label=='enter':
            myModel.setQuery("select 种类 from 入库记录表")
        elif label=='out':
            myModel.setQuery("select 种类 from 出库记录表")
        allnum = myModel.rowCount()
        all_dict={}
        for i in range(allnum):
            rec = myModel.record(i)
            if rec.value('种类') in all_dict:
                all_dict[rec.value('种类')] += 1
            else:
                all_dict[rec.value('种类')] = 1
        return all_dict
    #寻找出入库记录的最大批次
    def getMaxbatch(self,label):
        myModel = QSqlQueryModel(self)
        if label=='enter':
            myModel.setQuery("select 批次 from 入库记录表")
        elif label=='out':
            myModel.setQuery("select 批次 from 出库记录表")
        n=myModel.rowCount()
        if myModel.record(0).isNull('批次') == True:  # 检测入库记录里的最大批次
            max_batch = 0
        else:
            max_batch = myModel.record(n - 1).value('批次')  # 批次按顺序排列，查找最大批次
            print('共有%d条记录，最大批次为%d'%(n,max_batch))
        return max_batch
    #################################主操作界面####################################################
    # 容量不足信息打印
    def on_enterNum_spinBox_valueChanged(self):
        self.enter_Warning()

    def on_enterKind_comboBox_currentIndexChanged(self):
        self.enter_Warning()

    def enter_Warning(self):
        num = self.ui.enterNum_spinBox.value()
        enterKind = self.ui.enterKind_comboBox.currentText()
        if enterKind not in self.currentList:
            currentNum = 0
        else:
            currentNum = self.currentList[enterKind]
        if num + currentNum > self.capacity[enterKind]:
            self.ui.enterList_pushButton.setEnabled(False)
            # self.ui.enterScan_pushButton.setEnabled(False)
            warningText = '⚠警告！' + enterKind + '已经超出库容上限！'
        else:
            self.ui.enterList_pushButton.setEnabled(True)
            # self.ui.enterScan_pushButton.setEnabled(True)
            warningText = ''
        self.ui.textEdit.setPlainText(warningText)

    #############入库函数
    ##入库添加工件及对应数量
    @pyqtSlot()
    def on_enterList_pushButton_clicked(self):
        enterKind = self.ui.enterKind_comboBox.currentText()
        enterNum = self.ui.enterNum_spinBox.value()
        if enterKind in self.enterList:
            self.enterList[enterKind] += enterNum
        else:
            self.enterList[enterKind] = enterNum
        # 激活出库按钮使能状态
        self.ui.enterScan_pushButton.setEnabled(True)
        print(self.enterList)


    ##扫描入库
    @pyqtSlot()
    def on_enterScan_pushButton_clicked(self):
        # 根据入库记录里的RFID生成新的RFID
        enteredList = self.statistics(self.enter_tabModel)  # 获取入库记录里各种工件的数量
        RFID_list = []
        for key in self.enterList.keys():  # 对要入库的工件种类进行迭代
            for i in range(self.enterList[key]):
                if key not in enteredList:
                    no = i + 6
                else:
                    no = enteredList[key] + i + 6
                RFID = self.name_RFID[key] + str(no).zfill(6)
                RFID_list.append(RFID)
        # 将RFID写入txt文件来模拟货物
        filename = '卸货区'
        if not os.path.isdir(filename):
            os.makedirs(filename)
        with open('卸货区\待入库货工件.txt', 'w', encoding='utf8') as f:
            for s in RFID_list:
                f.write(s + '\n')
        # 从卸货区寻找模拟货物
        dbFilename, flt = QFileDialog.getOpenFileName(self, "寻找入库货物", "",
                                                      "模拟货物(*.txt)")
        if (dbFilename == ''):
            return
        with open(dbFilename, 'r', encoding='utf8') as f:
            enterRFID = f.readlines()

        all_location, forwardLocation = self.getLocation(self.enterList,'i')
        self.ui.widget.get_path(forwardLocation, 'i')  # 绘制路径
        self.enter(enterRFID, all_location)  # 入库操作

    def enter(self, enterRFID, all_location):
        #print('入库函数，enterRFID=',enterRFID,'all_location=',all_location)
        # 准备写入工件信息表和入库记录表
        currentQuery = QSqlQuery(self.DB)
        enterQuery = QSqlQuery(self.DB)
        currentQuery.prepare('''INSERT INTO 工件信息表 (RFID,种类,货位,生产商,
                      批次,入库日期,入库时间,重量) VALUES(:RFID,:kind,:location,:manufacture,:batch,
                      :enterDate,:enterTime,:weight)''')
        enterQuery.prepare('''INSERT INTO 入库记录表 (RFID,种类,生产商,
                      批次,入库日期,入库时间) VALUES(:RFID,:kind, :manufacture,:batch,
                      :enterDate,:enterTime)''')

        # 准备数据（都是恒量）

        RFID_manufacture = {'E0000001': '西安交大一厂', 'E0000002': '西安交大二厂', 'E0000003': '西安交大三厂'}
        max_batch=self.getMaxbatch('enter')
        enterDate = self.ui.dealdate.date().toString(Qt.ISODate)  # 获取日期
        enterTime = time.strftime('%H:%M:%S', time.localtime(time.time()))  # 获取时分秒
        weightList = {'直齿轮': 15, '斜齿轮': 20, '齿轮轴': 7, '光轴': 5, '曲柄': 2, '摇杆': 1}
        check = True
        # 扫码并写入记录表

        for i in range(len(enterRFID)):
            # 解码
            s = enterRFID[i].rstrip('\n')
            kind = self.RFID_kind[s[0:18]]
            manufacture = RFID_manufacture[s[4:12]]
            weight = weightList[kind]
            # 加入现有库存
            currentQuery.bindValue(":RFID", s)
            currentQuery.bindValue(":kind", kind)
            currentQuery.bindValue(":location", all_location[i])
            currentQuery.bindValue(":manufacture", manufacture)
            currentQuery.bindValue(":batch", max_batch + 1)
            currentQuery.bindValue(":enterDate", enterDate)
            currentQuery.bindValue(":enterTime", enterTime)
            currentQuery.bindValue(":weight", weight);
            res = currentQuery.exec()  # 执行SQL语句
            check = check & res
            # 加入入库记录表
            enterQuery.bindValue(":RFID", s)
            enterQuery.bindValue(":kind", kind)
            enterQuery.bindValue(":manufacture", manufacture)
            enterQuery.bindValue(":batch", max_batch + 1)
            enterQuery.bindValue(":enterDate", enterDate)
            enterQuery.bindValue(":enterTime", enterTime)
            enterQuery.exec()  # 执行SQL语句

        if check == False:
            QMessageBox.critical(self, "错误",
                                 "添加记录出现错误\n" + currentQuery.lastError().text())
            print('入库异常')
        else:
            self.enterList = {}
            self.refresh()
            self.ui.enterScan_pushButton.setEnabled(False)
            self.ui.textEdit.setPlainText('入库操作成功')

    #############出库函数
    # 库存不足信息打印

    def on_outNum_spinBox_valueChanged(self):
        self.out_Warning()

    def on_outKind_comboBox_currentIndexChanged(self):
        self.out_Warning()

    def out_Warning(self):
        num = self.ui.outNum_spinBox.value()
        outKind = self.ui.outKind_comboBox.currentText()
        self.currentList = self.Absolute_statis('current')
        if outKind not in self.currentList:  # 防止有些工件没有时作为字典的键出错
            currentNum = 0
        else:
            currentNum = self.currentList[outKind]
        if num > currentNum:
            self.ui.outList_pushButton.setEnabled(False)
            # self.ui.outScan_pushButton.setEnabled(False)
            warningText = '⚠警告！' + outKind + '已经超出库存上限！'
        else:
            self.ui.outList_pushButton.setEnabled(True)
            # self.ui.outScan_pushButton.setEnabled(True)
            warningText = ''
        self.ui.textEdit.setPlainText(warningText)

    # 添加出库工件
    @pyqtSlot()
    def on_outList_pushButton_clicked(self):
        outKind = self.ui.outKind_comboBox.currentText()
        outNum = self.ui.outNum_spinBox.value()
        if outKind in self.outList:
            self.outList[outKind] += outNum
        else:
            self.outList[outKind] = outNum
        self.ui.outScan_pushButton.setEnabled(True)
        print("要出库的货物：",self.outList)


    @pyqtSlot()
    def on_outScan_pushButton_clicked(self):
        currentRow = self.current_tabModel.rowCount()  # 库存的已记录数
        RFID_list = []
        outLocation, forwardLocation = self.getLocation(self.outList, 'o')
        # 从现有库存里取符合条件的RFID
        for i in range(currentRow):
            curRec = self.current_tabModel.record(i)
            location = curRec.value('货位')
            if location in outLocation:
                RFID_list.append(curRec.value('RFID'))
        # 将RFID写入模拟货物
        filename = '发货区'
        if not os.path.isdir(filename):
            os.makedirs(filename)
        with open('发货区\待出库货工件.txt', 'w', encoding='utf8') as f:
            for s in RFID_list:
                f.write(s + '\n')
        # 从卸货区寻找模拟货物
        dbFilename, flt = QFileDialog.getOpenFileName(self, "寻找出库货物", "",
                                                      "模拟货物(*.txt)")
        if (dbFilename == ''):
            return

        with open(dbFilename, 'r', encoding='utf8') as f:
            outRFID = f.readlines()
            for i in range(len(outRFID)):  # 去除所有的换行符
                outRFID[i] = outRFID[i].rstrip('\n')

        self.ui.widget.get_path(forwardLocation, 'o')  #出库路径绘制
        self.out(outRFID)

    def out(self, outRFID):  # 出库函数，参数只有RFID列表
        currentRow = self.current_tabModel.rowCount()  # 库存的已记录数
        currentQuery = QSqlQuery(self.DB)  # 准备删除
        outQuery = QSqlQuery(self.DB)  # 准备插入
        outQuery.prepare('''INSERT INTO 出库记录表 (RFID,种类,生产商,
                              批次,出库日期,出库时间) VALUES(:RFID,:kind, :manufacture,:batch,
                              :outDate,:outTime)''')
        currentQuery.prepare('''DELETE FROM 工件信息表 WHERE RFID=:ID''')
        # 获取出库记录表里的最大批次
        batch=self.getMaxbatch('out')
        outDate = self.ui.dealdate.date().toString(Qt.ISODate)
        outTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        check = True
        # 读取要出库的工件的RFID
        for i in range(currentRow):  # 遍历现有库存找到要出库的RFID
            curRec = self.current_tabModel.record(i)
            if curRec.value('RFID') in outRFID:
                outQuery.bindValue(":RFID", curRec.value('RFID'))
                outQuery.bindValue(":kind", curRec.value('种类'))
                outQuery.bindValue(":manufacture", curRec.value('生产商'))
                outQuery.bindValue(":batch", batch + 1)
                outQuery.bindValue(":outDate", outDate)
                outQuery.bindValue(":outTime", outTime)
                outQuery.exec()  # 执行SQL语句
                currentQuery.bindValue(":ID", curRec.value('RFID'))
                res = currentQuery.exec()
                check = check & res
        if check == False:
            QMessageBox.critical(self, "错误",
                                 "出库记录出现错误\n" + currentQuery.lastError().text())
        else:
            self.refresh()
            self.outList = {}
            self.ui.outScan_pushButton.setEnabled(False)
            self.ui.textEdit.setPlainText('出库操作成功')
            self.out_Warning()  # 库存不足则打印信息，改变按键使能状态

    # =================================副操作界面==================================================
    def getCurrentNum(self):
        currentQryModel = QSqlQueryModel(self)
        currentQryModel.setQuery("select RFID from 工件信息表")
        allnum = currentQryModel.rowCount()
        return allnum, currentQryModel
    ##单件扫描
    @pyqtSlot()
    def on_emitPushButton_pressed(self):
        RFID = self.ui.RFIDlineEdit.text()
        forwardLocation = {}
        kind = self.RFID_kind[RFID[0:18]]
        kindlist = []
        kindlist.append(RFID)
        allnum, currentQryModel = self.getCurrentNum()
        for i in range(allnum):
            cur = currentQryModel.record(i)
            if RFID == cur.value('RFID'):
                self.out(kindlist)
                self.get_locState()
                return
                # 因为已经指定了RFID，所以出库没有路径规划
        location, position = self.allocation(kind, 1,'i')
        self.enter(kindlist, location)
        forwardLocation[kind] = position - 1
        self.ui.widget.get_path(forwardLocation, 'i')
    ##多件扫描
    @pyqtSlot()
    def on_ScanPushButton_pressed(self):
        outRFID = []
        inkindNum = {}
        dbFilename, flt = QFileDialog.getOpenFileName(self, "寻找入库货物", "",
                                                      "模拟货物(*.txt)")
        if (dbFilename == ''):
            return
        with open(dbFilename, 'r', encoding='utf8') as f:
            RFID = f.readlines()
            for i in range(len(RFID)):  # 去除所有的换行符
                RFID[i] = RFID[i].rstrip('\n')
        allnum, currentQryModel = self.getCurrentNum()
        for i in range(allnum):
            cur = currentQryModel.record(i)
            if cur.value('RFID') in RFID:
                outRFID.append(cur.value('RFID'))  # 如果现有库存里存在，则添加到出库RFID列表中
                RFID.remove(cur.value('RFID'))  # 移除
        if outRFID != []:
            self.out(outRFID)
            self.get_locState()
        if RFID != []:
            for i in RFID:
                kind = self.RFID_kind[i[0:18]]
                if kind in inkindNum:
                    inkindNum[kind] += 1
                else:
                    inkindNum[kind] = 1
            inLocation, forwardLocation = self.getLocation(inkindNum, 'i')
            self.ui.widget.get_path(forwardLocation, 'i')  #绘制路径
            self.enter(RFID, inLocation)  #入库操作



    #################################现有库存界面####################################################
    ##种类过滤
    def on_currentComboBox_currentIndexChanged(self, curText):
        self.current_filter()

    ##批次过滤
    def on_batchSpinBox_valueChanged(self, num):
        self.current_filter()

    ##是否选择批次
    def on_batchCheckBox_stateChanged(self):
        self.current_filter()

    def current_filter(self):
        kind = self.ui.currentComboBox.currentText()
        batch = self.ui.batchSpinBox.value()
        if kind == '全选':
            if self.ui.batchCheckBox.isChecked() == True:
                self.current_tabModel.setFilter("批次='%d'" % (batch))
            else:
                self.current_tabModel.setFilter("")
        else:

            if self.ui.batchCheckBox.isChecked() == True:
                self.current_tabModel.setFilter("批次='%d' and 种类='%s'" % (batch, kind))
            else:
                self.current_tabModel.setFilter("种类='%s'" % (kind))

    # 已用库存百分比显示
    def inventory_used(self):
        # 通过进度条表示库存余量
        currentQryModel = QSqlQueryModel(self)
        currentQryModel.setQuery("select RFID from 工件信息表")
        allnum = currentQryModel.rowCount()
        progress = int((100 * allnum / 156) + 0.5)
        self.ui.progressBar.setValue(progress)


    @pyqtSlot()
    def on_delete_pushButton_pressed(self):
        query = QSqlQuery(self.DB)
        print('开始删除')
        query.exec("DELETE FROM 工件信息表 WHERE 批次>=0")
        query.exec("DELETE FROM 出库记录表 WHERE 批次>=0")
        check = query.exec("DELETE FROM 入库记录表 WHERE 批次>=0")
        if check == False:
            QMessageBox.critical(self, "错误",
                                 "删除记录出现错误\n" + query.lastError().text())
        else:
            self.refresh()

    #################################入库记录界面####################################################
    ##种类过滤
    def on_enterComboBox_currentIndexChanged(self):
        self.enter_filter()

    ##日期过滤
    def on_enterDate_dateChanged(self):
        self.enter_filter()

    ##是否选择批次
    def on_enterCheckBox_stateChanged(self):
        self.enter_filter()

    def enter_filter(self):
        kind = self.ui.enterComboBox.currentText()
        date = self.ui.enterDate.date().toString(Qt.ISODate)
        if self.ui.enterCheckBox.isChecked() == True:
            if kind == '全选':
                self.enter_tabModel.setFilter("入库日期='%s'" % (date))
            else:
                self.enter_tabModel.setFilter("入库日期='%s' and 种类='%s'" % (date, kind))
        else:
            if kind == '全选':
                self.enter_tabModel.setFilter("")
            else:
                self.enter_tabModel.setFilter("种类='%s'" % (kind))

    # 入库记录可视化
    @pyqtSlot()
    def on_drawEnter_pushButton_pressed(self):
        self.recordDemo(self.enter_tabModel)

    #################################出库记录界面####################################################
    ##种类过滤
    def on_outComboBox_currentIndexChanged(self):
        self.out_filter()

    ##日期过滤
    def on_outDate_dateChanged(self):
        self.out_filter()

    ##是否选择批次
    def on_outCheckBox_stateChanged(self):
        self.out_filter()

    def out_filter(self):
        kind = self.ui.outComboBox.currentText()
        date = self.ui.outDate.date().toString(Qt.ISODate)
        if self.ui.outCheckBox.isChecked() == True:
            if kind == '全选':
                self.out_tabModel.setFilter("出库日期='%s'" % (date))
            else:
                self.out_tabModel.setFilter("出库日期='%s' and 种类='%s'" % (date, kind))
        else:
            if kind == '全选':
                self.out_tabModel.setFilter("")
            else:
                self.out_tabModel.setFilter("种类='%s'" % (kind))

    # 出库记录可视化
    @pyqtSlot()
    def on_drawOut_pushButton_pressed(self):
        self.recordDemo(self.out_tabModel)
    #################################数据可视化################################################
    # 现有库存可视化
    @pyqtSlot()
    def on_drawCurrent_pushButton_pressed(self):
        # def demo(self):
        #self.currentList = self.statistics(self.current_tabModel)
        self.currentList =self.Absolute_statis('current')
        labels = []
        values = []
        for key, value in self.currentList.items():
            labels.append(key)
            values.append(value)
        if self.ui.pie_radioButton.isChecked() == True:
            trace = [go.Pie(labels=labels, values=values)]
            layout = go.Layout(
                title='工件库存比例配比图',
            )
        elif self.ui.bar_radioButton.isChecked() == True:
            trace = [go.Bar(x=labels, y=values)]
            layout = go.Layout(
                title='工件库存直方图',
            )
        print(labels)
        print(values)
        fig = go.Figure(data=trace, layout=layout)
        file = 'F:\source\python代码\MES库存管理\VisualData'
        if not os.path.isdir(file):
            os.makedirs(file)
        filename = 'F:\source\python代码\MES库存管理\VisualData\\currentDemo.html'
        pyof.plot(fig, filename=filename, auto_open=False)
        win = DemoWindow(filename)
        win.exec()


    def recordDemo(self, model):
        record = {}
        enterRow = model.rowCount()  # 库存的已记录数
        dateName = model.record().fieldName(4)  # 入库日期&出库日期
        TimeName=model.record().fieldName(5)
        for i in range(enterRow):
            curRec = model.record(i)
            kind = curRec.value('种类')
            date = curRec.value(dateName)
            Time=curRec.value(TimeName)
            dateTime=date+' '+Time
            dateRecord = {}
            if kind not in record:  # 工件种类第一次检索到，将其添加到reord中
                dateRecord[dateTime] = 1  # 同时将对应的日期添加到record中
                record[kind] = dateRecord
            else:
                if dateTime not in record[kind]:  # 种类存在，但是第一次检索到某个日期时
                    record[kind][dateTime] = 1
                else:
                    record[kind][dateTime] += 1
        traces = []
        for key1 in record.keys():
            x = []
            y = []
            for key2 in record[key1].keys():
                x.append(key2)
                y.append(record[key1][key2])
            trace = go.Scatter(
                x=x,
                y=y,
                # mode = 'markers',
                name=key1
            )
            traces.append(trace)
        layout = go.Layout(title=dateName[0:2] + '记录', )
        fig = go.Figure(data=traces, layout=layout)
        file = 'F:\source\python代码\MES库存管理\VisualData'
        if not os.path.isdir(file):
            os.makedirs(file)
        filename = 'F:\source\python代码\MES库存管理\VisualData\\recordDemo.html'
        pyof.plot(fig, filename=filename, auto_open=False)
        win = DemoWindow(filename)
        win.exec()


# 在main中实例化MainWindow，调用show方法显示
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
