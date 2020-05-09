import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtCore import Qt, QRect,QPoint

from PyQt5.QtGui import (QPainter, QPen, QBrush, QPalette,QPolygon,QColor)


class QwareHouse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体

        self.setPalette(QPalette(QColor(252,245,203)))  # 设置窗口为白色背景
        self.setAutoFillBackground(True)
        self.resize(900, 600)
        self.setWindowTitle("仓库平面图")
        self.kindY={'直齿轮': 0, '斜齿轮': 2, '齿轮轴': 0, '光轴': 2, '曲柄': 0, '摇杆': 2}#一区为哦
        self.x=[8,14,20]
        self.y=[5,6,13,14]
        self.allPoint = []
        self.outPoint={0:[[3,5],[3,6]],2:[[3,5],[5,5],[5,13],[4,14],[4,6],[3,6]]}
        self.inPoint = {0: [[3, 13], [4, 13], [4, 5], [5, 6], [5, 14], [3, 14]],
                        2: [[3, 13],[3, 14] ]}
    def get_path(self,dict,direction):
        self.allPoint=[]
        if direction=='o':
            points=self.outPoint
        else:
            points=self.inPoint
        for key,value in dict.items():
            zone=self.kindY[key]
            point1=[self.x[value],self.y[zone]]
            point2=[self.x[value],self.y[zone+1]]
            l=int(len(points[zone])/2)
            kindpoint=points[zone].copy()
            kindpoint.insert(l,point2)
            kindpoint.insert(l,point1)
            self.allPoint.append(kindpoint)
        print(self.allPoint)
        self.repaint()

    def paintEvent(self, event):  # 在窗口上绘图
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        ##设置画笔
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(pen)
        ##设置画刷
        brush = QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        ##绘制货架
        W = self.width()
        H = self.height()
        rect1 = QRect(0, H*4/ 18, W*3 / 24, H*3 / 17)
        rect2 = QRect(0, H * 12 / 18, W*3 / 24, H *3/ 17)
        painter.drawRects(rect1,rect2)

        font = painter.font()
        font.setPointSize(0.0225*W)
        font.setBold(True)
        painter.setFont(font)
        rect = QRect(0, 0, W, H / 8)
        painter.drawText(rect, Qt.AlignCenter, '仓库平面图')
        painter.drawText(rect1,Qt.AlignCenter,'出口')
        painter.drawText(rect2, Qt.AlignCenter, '入口')
        shelfName=[['A1','A2','A3'],['B1','B2','B3'],
                   ['C1','C2','C3'],['D1','D2','D3']]

        horGap, horWidth, horDistance = 2, 4, 2
        verGap, verWidth, verDistance = 1, 2, 3
        horlen = 4 * horGap + 3 * horWidth + 2 * horDistance  #24
        verlen = 3 * verGap + 4 * verWidth + 3 * verDistance-2  #17

        for i in range(4):
            for j in range(3):
                if i==2:
                    ver=3-2/2
                elif i==3:
                    ver=3-2/3
                else:
                    ver = verDistance
                rect = QRect(W * (3*horGap + j * (horWidth + horDistance)) / horlen,
                             H * (2*verGap + i * (verWidth + ver)) / verlen,
                             W * (horWidth) / horlen, H * (verWidth) / verlen)
                painter.drawRect(rect)
                painter.drawText(rect, Qt.AlignCenter, shelfName[i][j])
        colorsix=[QColor(255,181,73),QColor(65,182,230),QColor(254,95,85),
                  QColor(30,227,207),QColor(13,63,103),QColor(228,23,73)]
        if self.allPoint!=[]:
            for i in range(len(self.allPoint)):
                points = []
                pen.setColor(colorsix[i])
                painter.setPen(pen)
                for point in self.allPoint[i]:
                    points.append(QPoint(point[0]*W/horlen-6*i,point[1]*H/verlen+6*i))
                painter.drawPolyline(QPolygon(points))

if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QwareHouse()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
