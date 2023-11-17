# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(500, 500))
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(280, 10, 111, 31))
        self.result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.result.setMargin(10)
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(12, 50, 381, 61))
        self.display.setStyleSheet(u"padding-right: 10px")
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 381, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"height:40; \n"
"background-color: #DBAC00;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_18, 6, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_19, 6, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_15, 4, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_14, 4, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_13, 4, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_16, 4, 3, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"height:40; background-color: #DBAC00; color: black")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"height:40;\n"
"background-color: #1e1b18")

        self.gridLayout.addWidget(self.pushButton_17, 6, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"height:40")

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"height:40; \n"
"background-color: #DBAC00;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_20, 6, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setStyleSheet(u"height:40;\n"
"background-color: deepskyblue;\n"
"color: black")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.display.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_17.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"*", None))
    # retranslateUi

