import os
import win32con,  win32api
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_MainWindow import Ui_MainWindow
from 内网登录 import *

data_name = "./CJLU_Login_data.txt"

class MainWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self,  parent=None):
        super(MainWindow,  self).__init__(parent)
        self.setupUi(self)
        self.read_data()
        self.check_internet()
    
    def get_ip(self):
        self.ip = GetIP()

    def get_data(self):
        self.account = self.lineEdit_account.text()
        self.password = self.lineEdit_password.text()
        if self.savepassword_status is True:
            self.save_data(2)
        elif self.saveaccount_status is True:
            self.save_data(1)
        else:
            if os.path.exists(data_name) is True:
                os.remove(data_name)
        if self.intenet_status is True:
            self.account = "__" + self.account
            
    def read_data(self):
        data = []
        self.data_status = os.path.exists(data_name)
        if self.data_status is True:
            with open(data_name) as f:
                for line in f:
                    data.append(line.replace('\n',''))
            self.account = data[0]
            self.lineEdit_account.setText(self.account)
            self.checkBox_account.setChecked(True)
            if len(data) == 2:
                self.password = data[1]
                self.lineEdit_password.setText(self.password)
                self.checkBox_password.setChecked(True)
                
    def save_data(self,  data_line):
        if os.path.exists(data_name) is True:
                os.remove(data_name)
        with open(data_name,  "w") as f:
            if data_line == 1:
                f.write(self.account)
            elif data_line == 2:
                f.write(self.account + "\n")
                f.write(self.password)
        win32api.SetFileAttributes(data_name,win32con.FILE_ATTRIBUTE_HIDDEN)
        
    def get_check(self):
        self.saveaccount_status = self.checkBox_account.isChecked()
        self.savepassword_status = self.checkBox_password.isChecked()
        self.intenet_status = self.checkBox_Internet.isChecked()
        
    def check_internet(self):
        self.init_Inetrnet_status = CheckInternet()
        if(self.init_Inetrnet_status == 1):
            self.label_status.setText("Internet连接正常。")
            self.pushButton_login.setEnabled(False)
        elif(self.init_Inetrnet_status == 2):
            self.label_status.setText("Internet仅连接学校内网。")
            self.pushButton_login.setEnabled(False)
        elif(self.init_Inetrnet_status == 3):
            self.label_status.setText("网络连接正常，请登录。")
            self.pushButton_logout.setEnabled(False)
        elif(self.init_Inetrnet_status == 2):
            self.label_status.setText("网络连接异常，请检查网络。")
            self.pushButton_login.setEnabled(False)
            self.pushButton_logout.setEnabled(False)
        
    def login(self):
        self.get_ip()
        self.get_check()
        self.get_data()
        self.status = Login(self.ip,  self.account,  self.password)
        if(self.status is True):
            self.label_status.setText("登录成功。")
            self.pushButton_login.setEnabled(False)
            self.pushButton_logout.setEnabled(True)
        else:
            self.label_status.setText("登录失败，请重试。")
        
    def logout(self):
        self.status = Logout()
        self.label_status.setText("注销成功。")
        self.pushButton_login.setEnabled(True)
        self.pushButton_logout.setEnabled(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
