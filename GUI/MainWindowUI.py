# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(204, 467)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow {\n"
"   background-color: rgb(36, 31, 49);\n"
"}")
        self.action_Serial = QAction(MainWindow)
        self.action_Serial.setObjectName(u"action_Serial")
        self.action_Network = QAction(MainWindow)
        self.action_Network.setObjectName(u"action_Network")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"   background-color: rgb(36, 31, 49);\n"
"}")
        self.Decimal_pushButton = QPushButton(self.centralwidget)
        self.Decimal_pushButton.setObjectName(u"Decimal_pushButton")
        self.Decimal_pushButton.setGeometry(QRect(120, 210, 41, 41))
        self.Nine_pushButton = QPushButton(self.centralwidget)
        self.Nine_pushButton.setObjectName(u"Nine_pushButton")
        self.Nine_pushButton.setGeometry(QRect(120, 170, 41, 41))
        self.Clear_pushButton = QPushButton(self.centralwidget)
        self.Clear_pushButton.setObjectName(u"Clear_pushButton")
        self.Clear_pushButton.setGeometry(QRect(40, 210, 41, 41))
        self.Three_pushButton = QPushButton(self.centralwidget)
        self.Three_pushButton.setObjectName(u"Three_pushButton")
        self.Three_pushButton.setGeometry(QRect(120, 90, 41, 41))
        self.Five_pushButton = QPushButton(self.centralwidget)
        self.Five_pushButton.setObjectName(u"Five_pushButton")
        self.Five_pushButton.setGeometry(QRect(80, 130, 41, 41))
        self.Go_pushButton = QPushButton(self.centralwidget)
        self.Go_pushButton.setObjectName(u"Go_pushButton")
        self.Go_pushButton.setGeometry(QRect(40, 320, 121, 41))
        self.Go_pushButton.setStyleSheet(u"QPushButton#Go_pushButton {\n"
"     background-color: rgb(9, 132, 41);\n"
"}")
        self.Zero_pushButton = QPushButton(self.centralwidget)
        self.Zero_pushButton.setObjectName(u"Zero_pushButton")
        self.Zero_pushButton.setGeometry(QRect(80, 210, 41, 41))
        self.Six_pushButton = QPushButton(self.centralwidget)
        self.Six_pushButton.setObjectName(u"Six_pushButton")
        self.Six_pushButton.setGeometry(QRect(120, 130, 41, 41))
        self.Two_pushButton = QPushButton(self.centralwidget)
        self.Two_pushButton.setObjectName(u"Two_pushButton")
        self.Two_pushButton.setGeometry(QRect(80, 90, 41, 41))
        self.One_pushButton = QPushButton(self.centralwidget)
        self.One_pushButton.setObjectName(u"One_pushButton")
        self.One_pushButton.setGeometry(QRect(40, 90, 41, 41))
        self.Home_pushButton = QPushButton(self.centralwidget)
        self.Home_pushButton.setObjectName(u"Home_pushButton")
        self.Home_pushButton.setGeometry(QRect(40, 360, 121, 41))
        self.Home_pushButton.setStyleSheet(u"QPushButton#Home_pushButton{\n"
"   background-color:rgb(165, 29, 45);\n"
"}")
        self.CurrentPosition_label = QLabel(self.centralwidget)
        self.CurrentPosition_label.setObjectName(u"CurrentPosition_label")
        self.CurrentPosition_label.setGeometry(QRect(40, 10, 121, 30))
        self.CurrentPosition_label.setStyleSheet(u"QLabel#CurrentPosition_label {\n"
"   background-color: rgb(229, 165, 10);\n"
"   qproperty-alignment: AlignCenter;\n"
"}")
        self.Seven_pushButton = QPushButton(self.centralwidget)
        self.Seven_pushButton.setObjectName(u"Seven_pushButton")
        self.Seven_pushButton.setGeometry(QRect(40, 170, 41, 41))
        self.Four_pushButton = QPushButton(self.centralwidget)
        self.Four_pushButton.setObjectName(u"Four_pushButton")
        self.Four_pushButton.setGeometry(QRect(40, 130, 41, 41))
        self.Eight_pushButton = QPushButton(self.centralwidget)
        self.Eight_pushButton.setObjectName(u"Eight_pushButton")
        self.Eight_pushButton.setGeometry(QRect(80, 170, 41, 41))
        self.Entry_lineEdit = QLineEdit(self.centralwidget)
        self.Entry_lineEdit.setObjectName(u"Entry_lineEdit")
        self.Entry_lineEdit.setGeometry(QRect(40, 50, 121, 30))
        self.Entry_lineEdit.setStyleSheet(u"QLineEdit#Entry_lineEdit {\n"
"   background-color:rgb(255, 255, 255);\n"
"   color: rgb(165, 29, 45)\n"
"}")
        self.JogCW_pushButton = QPushButton(self.centralwidget)
        self.JogCW_pushButton.setObjectName(u"JogCW_pushButton")
        self.JogCW_pushButton.setGeometry(QRect(40, 250, 41, 41))
        self.JogCW_pushButton.setStyleSheet(u"QPushButton#JogCW_pushButton {\n"
"     background-color:rgb(246, 97, 81);\n"
"}")
        self.JogCCW_pushButton = QPushButton(self.centralwidget)
        self.JogCCW_pushButton.setObjectName(u"JogCCW_pushButton")
        self.JogCCW_pushButton.setGeometry(QRect(120, 250, 41, 41))
        self.JogCCW_pushButton.setStyleSheet(u"QPushButton#JogCCW_pushButton {\n"
"     background-color:rgb(246, 97, 81);\n"
"}")
        self.messageArea = QLabel(self.centralwidget)
        self.messageArea.setObjectName(u"messageArea")
        self.messageArea.setGeometry(QRect(10, 410, 181, 23))
        self.messageArea.setStyleSheet(u"QLabel#messageArea {\n"
"   color: rgb(237, 51, 59);\n"
"   background-color: rgb(0, 0, 0);\n"
"   qproperty-alignment: AlignCenter;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 204, 28))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"  background-color: rgb(0,0,0);   // rgb(36, 31, 49)\n"
"}")
        self.menuComm = QMenu(self.menubar)
        self.menuComm.setObjectName(u"menuComm")
        self.menuComm.setStyleSheet(u".QMenu {\n"
"   background-color: rgb(0, 0, 0);\n"
"   color: rgb(246, 245, 244);\n"
"}")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuComm.menuAction())
        self.menuComm.addAction(self.action_Serial)
        self.menuComm.addAction(self.action_Network)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Serial.setText(QCoreApplication.translate("MainWindow", u"&Serial", None))
        self.action_Network.setText(QCoreApplication.translate("MainWindow", u"&Network", None))
        self.Decimal_pushButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Nine_pushButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Three_pushButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Five_pushButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Go_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.Zero_pushButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Six_pushButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Two_pushButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.One_pushButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Home_pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.CurrentPosition_label.setText(QCoreApplication.translate("MainWindow", u"Currently", None))
        self.Seven_pushButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Four_pushButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Eight_pushButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.JogCW_pushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.JogCCW_pushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.messageArea.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.menuComm.setTitle(QCoreApplication.translate("MainWindow", u"Comm", None))
    # retranslateUi

