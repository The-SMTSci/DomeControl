# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkDialogUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_DomeNetwork(object):
    def setupUi(self, DomeNetwork):
        if not DomeNetwork.objectName():
            DomeNetwork.setObjectName(u"DomeNetwork")
        DomeNetwork.setWindowModality(Qt.WindowModality.ApplicationModal)
        DomeNetwork.resize(416, 230)
        DomeNetwork.setStyleSheet(u"background-color : rgb(50,50,50);\n"
"color: white;")
        self.buttonBox = QDialogButtonBox(DomeNetwork)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(130, 180, 191, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.Host_Label = QLabel(DomeNetwork)
        self.Host_Label.setObjectName(u"Host_Label")
        self.Host_Label.setGeometry(QRect(10, 90, 111, 23))
        self.Host_Label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Host_Label.setMargin(5)
        self.Port_Label = QLabel(DomeNetwork)
        self.Port_Label.setObjectName(u"Port_Label")
        self.Port_Label.setGeometry(QRect(10, 130, 111, 23))
        self.Port_Label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Port_Label.setMargin(5)
        self.Hostname = QLineEdit(DomeNetwork)
        self.Hostname.setObjectName(u"Hostname")
        self.Hostname.setGeometry(QRect(130, 90, 251, 30))
        self.Hostname.setStyleSheet(u"background-color: rgb(218, 200, 37);\n"
"color: black")
        self.Port = QLineEdit(DomeNetwork)
        self.Port.setObjectName(u"Port")
        self.Port.setGeometry(QRect(130, 130, 251, 30))
        self.Port.setStyleSheet(u"background-color: rgb(218, 200, 37);\n"
"color: black")
        self.Password_Label = QLabel(DomeNetwork)
        self.Password_Label.setObjectName(u"Password_Label")
        self.Password_Label.setGeometry(QRect(10, 50, 111, 23))
        self.Password_Label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Password_Label.setMargin(5)
        self.Password = QLineEdit(DomeNetwork)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(130, 50, 251, 30))
        self.Password.setStyleSheet(u"background-color: rgb(218, 200, 37);\n"
"color: black")
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Username_Label = QLabel(DomeNetwork)
        self.Username_Label.setObjectName(u"Username_Label")
        self.Username_Label.setGeometry(QRect(10, 10, 111, 23))
        self.Username_Label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Username_Label.setMargin(5)
        self.Username = QLineEdit(DomeNetwork)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(130, 10, 251, 30))
        self.Username.setStyleSheet(u"background-color: rgb(218, 200, 37);\n"
"color: black")

        self.retranslateUi(DomeNetwork)
        self.buttonBox.accepted.connect(DomeNetwork.accept)
        self.buttonBox.rejected.connect(DomeNetwork.reject)

        QMetaObject.connectSlotsByName(DomeNetwork)
    # setupUi

    def retranslateUi(self, DomeNetwork):
        DomeNetwork.setWindowTitle(QCoreApplication.translate("DomeNetwork", u"Dome Network", None))
        self.Host_Label.setText(QCoreApplication.translate("DomeNetwork", u"Hostname", None))
        self.Port_Label.setText(QCoreApplication.translate("DomeNetwork", u"Port", None))
#if QT_CONFIG(tooltip)
        self.Hostname.setToolTip(QCoreApplication.translate("DomeNetwork", u"IP or Hostname", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Port.setToolTip(QCoreApplication.translate("DomeNetwork", u"Port", None))
#endif // QT_CONFIG(tooltip)
        self.Password_Label.setText(QCoreApplication.translate("DomeNetwork", u"Password", None))
#if QT_CONFIG(tooltip)
        self.Password.setToolTip(QCoreApplication.translate("DomeNetwork", u"IP or Hostname", None))
#endif // QT_CONFIG(tooltip)
        self.Username_Label.setText(QCoreApplication.translate("DomeNetwork", u"Username", None))
#if QT_CONFIG(tooltip)
        self.Username.setToolTip(QCoreApplication.translate("DomeNetwork", u"IP or Hostname", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

