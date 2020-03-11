# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
#
# Author: Alina Povazhnyuk

import cv2
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from BullionClass import Bullion, CounturClass


def Show(img1):
    cv2.namedWindow("window", cv2.WINDOW_NORMAL)
    cv2.imshow("window", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 872)
        MainWindow.setFixedSize(1156, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(9, 9, 1139, 665))
        self.image.setText("")
        first_image_name = "hayam.jpg"
        self.image.setPixmap(QtGui.QPixmap(first_image_name))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.bullion = Bullion(first_image_name)
        self.ContourButton = QtWidgets.QPushButton(self.centralwidget)
        self.ContourButton.setGeometry(QtCore.QRect(320, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ContourButton.setFont(font)
        self.ContourButton.setObjectName("ContourButton")

        self.ContourButton.clicked.connect(self.on_ContourButton)

        self.ContourPointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ContourPointsButton.setEnabled(False)
        self.ContourPointsButton.setGeometry(QtCore.QRect(410, 700, 95, 48))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ContourPointsButton.setFont(font)
        self.ContourPointsButton.setAcceptDrops(False)
        self.ContourPointsButton.setObjectName("ContourPointsButton")
        self.ContourPointsButton.setToolTip('Enter how many measures should be!')

        self.ContourPointsButton.clicked.connect(self.on_ContourPointsButton)

        self.RectButton = QtWidgets.QPushButton(self.centralwidget)
        self.RectButton.setGeometry(QtCore.QRect(320, 740, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.RectButton.setFont(font)
        self.RectButton.setObjectName("RectButton")

        self.RectButton.clicked.connect(self.on_RectButton)

        self.rectPointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.rectPointsButton.setEnabled(False)
        self.rectPointsButton.setGeometry(QtCore.QRect(410, 760, 96, 48))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.rectPointsButton.setFont(font)
        self.rectPointsButton.setMouseTracking(False)
        self.rectPointsButton.setAutoRepeat(False)
        self.rectPointsButton.setAutoExclusive(False)
        self.rectPointsButton.setAutoDefault(False)
        self.rectPointsButton.setObjectName("rectPointsButton")
        self.rectPointsButton.setToolTip('Enter how many measures should be!')

        self.rectPointsButton.clicked.connect(self.on_rectPointsButton)

        self.Len = QtWidgets.QLineEdit(self.centralwidget)
        self.Len.setGeometry(QtCore.QRect(80, 720, 133, 20))
        self.Len.setObjectName("Len")
        self.Wid = QtWidgets.QLineEdit(self.centralwidget)
        self.Wid.setGeometry(QtCore.QRect(80, 770, 133, 20))
        self.Wid.setObjectName("Wid")

        self.Len.textChanged.connect(self.on_len)
        self.Wid.textChanged.connect(self.on_wid)


        self.CalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateButton.setGeometry(QtCore.QRect(110, 800, 75, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.setEnabled(False)


        self.CalculateButton.clicked.connect(self.on_CalculateButton)

        self.Report = QtWidgets.QTextBrowser(self.centralwidget)
        self.Report.setGeometry(QtCore.QRect(517, 706, 313, 116))
        self.Report.setObjectName("Report")
        self.Average = QtWidgets.QTextBrowser(self.centralwidget)
        self.Average.setGeometry(QtCore.QRect(836, 706, 312, 116))
        self.Average.setObjectName("Average")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(836, 680, 157, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(517, 680, 49, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(29, 700, 262, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(29, 752, 255, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(320, 780, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName("ClearButton")

        self.ClearButton.clicked.connect(self.on_ClearButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.actionNew_file.triggered.connect(self.browseFile)


        self.menuFile.addAction(self.actionNew_file)
        self.menubar.addAction(self.menuFile.menuAction())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Books"))
        self.ContourButton.setText(_translate("MainWindow", "Contour"))
        self.ContourPointsButton.setText(_translate("MainWindow", "Show points\n"
"on contour"))
        self.RectButton.setText(_translate("MainWindow", "Rectangle"))
        self.rectPointsButton.setText(_translate("MainWindow", "Show points\n"
"on rectangle"))
        self.CalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Result (average sizes)"))
        self.label_2.setText(_translate("MainWindow", "Report"))
        self.label_3.setText(_translate("MainWindow", "Enter how many measures on length:"))
        self.label_4.setText(_translate("MainWindow", "Enter how many measures on width:"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_file.setText(_translate("MainWindow", "New file..."))

    def browseFile(self):
        self.Report.clear()
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', None, "*.png *.jpg")[0]
        # self.Report.append(str(name))
        self.image.setPixmap(QtGui.QPixmap(str(name)))
        self.bullion = Bullion(name)

    def on_len(self):
        text_len = str(self.Len.text())
        text_wid = str(self.Wid.text())
        if text_len.isdigit() and text_len!='0' and text_wid.isdigit() and text_wid!='0':
            self.CalculateButton.setEnabled(True)
            self.rectPointsButton.setEnabled(True)
            self.ContourPointsButton.setEnabled(True)
        else:
            self.rectPointsButton.setEnabled(False)
            self.ContourPointsButton.setEnabled(False)

    def on_wid(self):
        text_len = str(self.Len.text())
        text_wid = str(self.Wid.text())
        if text_len.isdigit() and text_len != '0' and text_wid.isdigit() and text_wid != '0':
            self.CalculateButton.setEnabled(True)
            self.rectPointsButton.setEnabled(True)
            self.ContourPointsButton.setEnabled(True)
        else:
            self.rectPointsButton.setEnabled(False)
            self.ContourPointsButton.setEnabled(False)

    def on_ContourButton(self):
        self.Report.append('Draw contours {}'.format(datetime.datetime.now()))
        self.bullion.drawContours()


        height, width, channel = self.bullion.img_processed.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img_processed.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))

    def on_RectButton(self):
        self.Report.append('Draw rectangle {}'.format(datetime.datetime.now()))
        self.bullion.drawRectangle()

        height, width, channel = self.bullion.img_processed.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img_processed.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))

    def on_ClearButton(self):
        self.Report.clear()
        self.Average.clear()
        self.bullion.clearBullion()

        height, width, channel = self.bullion.img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))

    def on_ContourPointsButton(self):
        self.Report.append('Draw points on contour {}'.format(datetime.datetime.now()))
        self.bullion.lens = int(self.Len.text())
        self.bullion.widths = int(self.Wid.text())
        self.bullion.lines('contour')

        height, width, channel = self.bullion.img_processed.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img_processed.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))

    def on_rectPointsButton(self):
        self.Report.append('Draw points on rectangle {}'.format(datetime.datetime.now()))
        self.bullion.lens = int(self.Len.text())
        self.bullion.widths = int(self.Wid.text())
        self.bullion.lines('rect')

        height, width, channel = self.bullion.img_processed.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img_processed.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))

    def on_CalculateButton(self):
        self.bullion.clearBullion()
        self.bullion.lens = int(self.Len.text())
        self.bullion.widths = int(self.Wid.text())
        self.bullion.drawContours()
        self.bullion.lines('contour')
        self.bullion.drawLines()

        wid_summary = 0
        len_summary = 0
        widths, lengths = self.bullion.measureExplore()
        self.Average.append('{} x {}'.format(self.bullion.lens, self.bullion.widths))
        self.Report.append('MEASURING LENGTHS: {}'.format(datetime.datetime.now()))
        for id, item in enumerate(lengths):
            len_summary += item
            self.Report.append('Measure {}: {}mm'.format(id+1, item))
        self.Report.append('\nMEASURING WIDTHS: {}'.format(datetime.datetime.now()))
        for id, item in enumerate(widths):
            wid_summary += item
            self.Report.append('Measure {}: {}mm'.format(id+1, item))
        self.Report.append('\n')

        wid_average = wid_summary/len(widths)
        len_average = len_summary/len(lengths)
        self.Average.append('Average of lengths is: {}mm'.format(len_average))
        self.Average.append('Average of widths is: {}mm\n'.format(wid_average))

        height, width, channel = self.bullion.img_processed.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.bullion.img_processed.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)

        self.image.setPixmap(QtGui.QPixmap(qImg))






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
