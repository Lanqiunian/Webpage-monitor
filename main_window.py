# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_url = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(70, 10, 251, 21))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_interval = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_interval.setGeometry(QtCore.QRect(70, 40, 91, 21))
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.textEdit_log = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_log.setGeometry(QtCore.QRect(10, 130, 321, 311))
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_TimesOfChange = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_TimesOfChange.setGeometry(QtCore.QRect(70, 90, 51, 16))
        self.label_TimesOfChange.setObjectName("label_TimesOfChange")
        self.pushButton_operator = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_operator.setGeometry(QtCore.QRect(270, 70, 61, 51))
        self.pushButton_operator.setObjectName("pushButton_operator")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_startTime = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_startTime.setGeometry(QtCore.QRect(69, 70, 141, 16))
        self.label_startTime.setObjectName("label_startTime")
        self.label_status = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(190, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color:rgb(1, 255, 81)")
        self.label_status.setObjectName("label_status")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 40, 21, 20))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 337, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        self.about_menu = QtWidgets.QMenu(parent=self.menuBar)
        self.about_menu.setObjectName("about_menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.about_menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网页变动监控工具"))
        self.label.setText(_translate("MainWindow", "检测网址："))
        self.label_2.setText(_translate("MainWindow", "检测间隔:"))
        self.label_3.setText(_translate("MainWindow", "监控日志："))
        self.label_4.setText(_translate("MainWindow", "变化次数："))
        self.label_TimesOfChange.setText(_translate("MainWindow", "0"))
        self.pushButton_operator.setText(_translate("MainWindow", "开始"))
        self.label_6.setText(_translate("MainWindow", "开始时间："))
        self.label_startTime.setText(_translate("MainWindow", "监控未开始"))
        self.label_status.setText(_translate("MainWindow", "监控未开始"))
        self.label_5.setText(_translate("MainWindow", " 秒"))
        self.menu.setTitle(_translate("MainWindow", "功能"))
        self.about_menu.setTitle(_translate("MainWindow", "帮助与提示"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))