# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_windows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setAutoFillBackground(True)
        self.username_text = QtWidgets.QLineEdit(Form)
        self.username_text.setEnabled(True)
        self.username_text.setGeometry(QtCore.QRect(10, 30, 241, 41))
        self.username_text.setClearButtonEnabled(True)
        self.username_text.setObjectName("username_text")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 240, 251, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setEnabled(True)
        self.login_btn.setGeometry(QtCore.QRect(10, 160, 241, 41))
        self.login_btn.setObjectName("login_btn")
        self.yzm = SzLable(Form)
        self.yzm.setGeometry(QtCore.QRect(280, 10, 293, 190))
        self.yzm.setMinimumSize(QtCore.QSize(293, 190))
        self.yzm.setMaximumSize(QtCore.QSize(290, 190))
        self.yzm.setStyleSheet("background-color: rgb(188, 239, 233);")
        self.yzm.setObjectName("yzm")
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(290, 270, 79, 24))
        self.refresh.setObjectName("refresh")
        self.password_text = QtWidgets.QLineEdit(Form)
        self.password_text.setEnabled(True)
        self.password_text.setGeometry(QtCore.QRect(10, 90, 241, 41))
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password_text.setClearButtonEnabled(True)
        self.password_text.setObjectName("password_text")
        self.dm = QtWidgets.QPushButton(Form)
        self.dm.setGeometry(QtCore.QRect(420, 270, 79, 24))
        self.dm.setObjectName("dm")

        self.retranslateUi(Form)
        self.login_btn.clicked.connect(Form.login_check)
        self.refresh.clicked.connect(Form.refresh_code)
        self.dm.clicked.connect(Form.dm_auto)
        self.username_text.textChanged['QString'].connect(Form.auto_enable_login_btn)
        self.password_text.textChanged['QString'].connect(Form.auto_enable_login_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username_text.setText(_translate("Form", "15165363708"))
        self.username_text.setPlaceholderText(_translate("Form", "输入12306账号"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019-04</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">author：<span style=\" font-style:italic;\">liudianjun </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">email: <span style=\" font-style:italic;\">liu296387831</span></p></body></html>"))
        self.login_btn.setText(_translate("Form", "登                 录"))
        self.yzm.setText(_translate("Form", "TextLabel"))
        self.refresh.setText(_translate("Form", "刷新"))
        self.password_text.setText(_translate("Form", "19890513a"))
        self.password_text.setPlaceholderText(_translate("Form", "输入12306密码"))
        self.dm.setText(_translate("Form", "打码"))

from Szlable import SzLable
