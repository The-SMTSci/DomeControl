# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ComPortDialogUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QWidget)

class Ui_ComPortDialog(object):
    def setupUi(self, ComPortDialog):
        if not ComPortDialog.objectName():
            ComPortDialog.setObjectName(u"ComPortDialog")
        ComPortDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        ComPortDialog.resize(533, 168)
        ComPortDialog.setStyleSheet(u"background-color : rgb(50,50,50);\n"
"color: white;\n"
"\n"
"")
        self.buttonBox = QDialogButtonBox(ComPortDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(340, 125, 176, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.ComLabel = QLabel(ComPortDialog)
        self.ComLabel.setObjectName(u"ComLabel")
        self.ComLabel.setGeometry(QRect(15, 5, 100, 16))
        self.ComLabel.setStyleSheet(u"QLabel::item {\n"
"   color : rgb(192, 28, 40);\n"
"}")
        self.BaudLable = QLabel(ComPortDialog)
        self.BaudLable.setObjectName(u"BaudLable")
        self.BaudLable.setGeometry(QRect(15, 55, 100, 16))
        self.StartLabel = QLabel(ComPortDialog)
        self.StartLabel.setObjectName(u"StartLabel")
        self.StartLabel.setGeometry(QRect(230, 55, 91, 16))
        self.StopLabel = QLabel(ComPortDialog)
        self.StopLabel.setObjectName(u"StopLabel")
        self.StopLabel.setGeometry(QRect(335, 55, 91, 16))
        self.PartiyLable = QLabel(ComPortDialog)
        self.PartiyLable.setObjectName(u"PartiyLable")
        self.PartiyLable.setGeometry(QRect(440, 55, 86, 16))
        self.PortValue = QComboBox(ComPortDialog)
        self.PortValue.setObjectName(u"PortValue")
        self.PortValue.setGeometry(QRect(15, 25, 511, 23))
        self.BaudValue = QComboBox(ComPortDialog)
        self.BaudValue.setObjectName(u"BaudValue")
        self.BaudValue.setGeometry(QRect(15, 75, 96, 23))
        self.StartValue = QComboBox(ComPortDialog)
        self.StartValue.setObjectName(u"StartValue")
        self.StartValue.setGeometry(QRect(230, 75, 91, 23))
        self.StopValue = QComboBox(ComPortDialog)
        self.StopValue.setObjectName(u"StopValue")
        self.StopValue.setGeometry(QRect(335, 75, 91, 23))
        self.ParityValue = QComboBox(ComPortDialog)
        self.ParityValue.setObjectName(u"ParityValue")
        self.ParityValue.setGeometry(QRect(440, 75, 86, 23))
        self.BitsValue = QComboBox(ComPortDialog)
        self.BitsValue.setObjectName(u"BitsValue")
        self.BitsValue.setGeometry(QRect(125, 75, 91, 23))
        self.BitsLabel = QLabel(ComPortDialog)
        self.BitsLabel.setObjectName(u"BitsLabel")
        self.BitsLabel.setGeometry(QRect(125, 55, 91, 16))
        self.StopValue.raise_()
        self.PartiyLable.raise_()
        self.BitsLabel.raise_()
        self.buttonBox.raise_()
        self.StartLabel.raise_()
        self.PortValue.raise_()
        self.BitsValue.raise_()
        self.StopLabel.raise_()
        self.BaudValue.raise_()
        self.BaudLable.raise_()
        self.StartValue.raise_()
        self.ParityValue.raise_()
        self.ComLabel.raise_()

        self.retranslateUi(ComPortDialog)
        self.buttonBox.accepted.connect(ComPortDialog.accept)
        self.buttonBox.rejected.connect(ComPortDialog.reject)

        QMetaObject.connectSlotsByName(ComPortDialog)
    # setupUi

    def retranslateUi(self, ComPortDialog):
        ComPortDialog.setWindowTitle(QCoreApplication.translate("ComPortDialog", u"Com Port Dialog", None))
        self.ComLabel.setText(QCoreApplication.translate("ComPortDialog", u"Com Port", None))
        self.BaudLable.setText(QCoreApplication.translate("ComPortDialog", u"Baud Rate", None))
        self.StartLabel.setText(QCoreApplication.translate("ComPortDialog", u"Start Bits", None))
        self.StopLabel.setText(QCoreApplication.translate("ComPortDialog", u"Stop Bits", None))
        self.PartiyLable.setText(QCoreApplication.translate("ComPortDialog", u"Parity", None))
        self.BitsLabel.setText(QCoreApplication.translate("ComPortDialog", u"Bits", None))
    # retranslateUi

