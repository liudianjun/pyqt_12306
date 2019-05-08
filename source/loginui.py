# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '12306.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(600, 400))
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(111111, 111111))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setEnabled(True)
        self.username.setGeometry(QtCore.QRect(10, 20, 241, 41))
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(10, 80, 241, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.dm = QPushButton(self.widget)
        self.dm.setGeometry(QtCore.QRect(450, 320, 79, 24))
        self.dm.setObjectName("dm")
        self.refresh = QPushButton(self.widget)
        self.refresh.setGeometry(QtCore.QRect(300, 320, 79, 24))
        self.refresh.setObjectName("refresh")
        self.login = QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(10, 150, 241, 41))
        self.login.setObjectName("login")
        self.yzm = QtWidgets.QLabel(self.widget)
        self.yzm.setGeometry(QtCore.QRect(280, 0, 293, 290))
        self.yzm.setMinimumSize(QtCore.QSize(293, 290))
        self.yzm.setMaximumSize(QtCore.QSize(290, 190))
        self.yzm.setStyleSheet("background-color: rgb(188, 239, 233);")
        self.yzm.setObjectName("yzm")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 230, 251, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.login.clicked.connect(Form.login)
        self.refresh.clicked.connect(Form.refresh)
        self.dm.clicked.connect(Form.dm)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setPlaceholderText(_translate("Form", "输入12306账号"))
        self.password.setPlaceholderText(_translate("Form", "输入12306密码"))
        self.dm.setText(_translate("Form", "打码"))
        self.refresh.setText(_translate("Form", "刷新"))
        self.login.setText(_translate("Form", "登                 录"))
        self.yzm.setText(_translate("Form", "TextLabel"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019-04</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">author：<span style=\" font-style:italic;\">liudianjun </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">email: <span style=\" font-style:italic;\">liu296387831</span></p></body></html>"))

