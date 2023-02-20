# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 90, 531, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_folder = QLabel(self.horizontalLayoutWidget)
        self.label_folder.setObjectName(u"label_folder")
        sizePolicy.setHeightForWidth(self.label_folder.sizePolicy().hasHeightForWidth())
        self.label_folder.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(10)
        self.label_folder.setFont(font)

        self.horizontalLayout.addWidget(self.label_folder)

        self.btn_sel_folder = QPushButton(self.horizontalLayoutWidget)
        self.btn_sel_folder.setObjectName(u"btn_sel_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_sel_folder.sizePolicy().hasHeightForWidth())
        self.btn_sel_folder.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.btn_sel_folder.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_sel_folder)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.btn_go = QPushButton(self.horizontalLayoutWidget)
        self.btn_go.setObjectName(u"btn_go")
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        self.btn_go.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_go)

        self.horizontalLayout.setStretch(0, 1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 461, 41))
        font3 = QFont()
        font3.setFamilies([u"Courier New"])
        font3.setPointSize(16)
        self.label.setFont(font3)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 60, 530, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_folder.setText(QCoreApplication.translate("MainWindow", u"folder location...", None))
        self.btn_sel_folder.setText(QCoreApplication.translate("MainWindow", u"select folder", None))
        self.btn_go.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[ images to ico ] Generator", None))
    # retranslateUi

