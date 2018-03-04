# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\CJLU\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 178)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_login = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_login.setEnabled(True)
        self.pushButton_login.setGeometry(QtCore.QRect(50, 120, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_logout = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 268, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_account = QtWidgets.QLabel(self.layoutWidget)
        self.label_account.setObjectName("label_account")
        self.horizontalLayout.addWidget(self.label_account)
        self.lineEdit_account = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_account.setText("")
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.horizontalLayout.addWidget(self.lineEdit_account)
        self.checkBox_account = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_account.setObjectName("checkBox_account")
        self.horizontalLayout.addWidget(self.checkBox_account)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.checkBox_password = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_password.setChecked(False)
        self.checkBox_password.setObjectName("checkBox_password")
        self.horizontalLayout_2.addWidget(self.checkBox_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_status = QtWidgets.QLabel(self.centralWidget)
        self.label_status.setGeometry(QtCore.QRect(119, 92, 161, 16))
        self.label_status.setObjectName("label_status")
        self.checkBox_Internet = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_Internet.setGeometry(QtCore.QRect(21, 92, 81, 16))
        self.checkBox_Internet.setChecked(True)
        self.checkBox_Internet.setObjectName("checkBox_Internet")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 271, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_login.clicked.connect(MainWindow.login)
        self.pushButton_logout.clicked.connect(MainWindow.logout)
        self.checkBox_password.clicked['bool'].connect(self.checkBox_account.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CJLU内网有线登录 V1.0.0"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_logout.setText(_translate("MainWindow", "注销"))
        self.label_account.setText(_translate("MainWindow", "账号："))
        self.checkBox_account.setText(_translate("MainWindow", "保存账号  "))
        self.label_password.setText(_translate("MainWindow", "密码："))
        self.checkBox_password.setText(_translate("MainWindow", "保存密码  "))
        self.label_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">网络连接检测中。</p></body></html>"))
        self.checkBox_Internet.setText(_translate("MainWindow", "访问互联网"))
        self.label.setText(_translate("MainWindow", "开发：14光电的浩宝宝   邮箱：625607188@qq.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

