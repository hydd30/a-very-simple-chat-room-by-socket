# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_client_main(object):
    def setupUi(self, client_main_ui):
        client_main_ui.setObjectName("client_main_ui")
        client_main_ui.resize(804, 404)
        self.coursename_LB = QtWidgets.QLabel(client_main_ui)
        self.coursename_LB.setGeometry(QtCore.QRect(20, 20, 53, 16))
        self.coursename_LB.setObjectName("coursename_LB")
        self.stunum_LB = QtWidgets.QLabel(client_main_ui)
        self.stunum_LB.setGeometry(QtCore.QRect(20, 110, 53, 16))
        self.stunum_LB.setObjectName("stunum_LB")
        self.passwd_LB = QtWidgets.QLabel(client_main_ui)
        self.passwd_LB.setGeometry(QtCore.QRect(20, 140, 53, 16))
        self.passwd_LB.setObjectName("passwd_LB")
        self.IP_address_LB = QtWidgets.QLabel(client_main_ui)
        self.IP_address_LB.setGeometry(QtCore.QRect(20, 50, 53, 16))
        self.IP_address_LB.setObjectName("IP_address_LB")
        self.portnum_LB = QtWidgets.QLabel(client_main_ui)
        self.portnum_LB.setGeometry(QtCore.QRect(20, 80, 53, 16))
        self.portnum_LB.setObjectName("portnum_LB")
        self.coursename_LE = QtWidgets.QLineEdit(client_main_ui)
        self.coursename_LE.setGeometry(QtCore.QRect(80, 20, 113, 21))
        self.coursename_LE.setText("")
        self.coursename_LE.setObjectName("coursename_LE")
        self.IP_address_LE = QtWidgets.QLineEdit(client_main_ui)
        self.IP_address_LE.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.IP_address_LE.setObjectName("IP_address_LE")
        self.portnum_LE = QtWidgets.QLineEdit(client_main_ui)
        self.portnum_LE.setGeometry(QtCore.QRect(80, 80, 113, 21))
        self.portnum_LE.setObjectName("portnum_LE")
        self.stunum_LE = QtWidgets.QLineEdit(client_main_ui)
        self.stunum_LE.setGeometry(QtCore.QRect(80, 110, 113, 21))
        self.stunum_LE.setObjectName("stunum_LE")
        self.password_LE = QtWidgets.QLineEdit(client_main_ui)
        self.password_LE.setGeometry(QtCore.QRect(80, 140, 113, 21))
        self.password_LE.setObjectName("password_LE")
        self.connect_BTN = QtWidgets.QPushButton(client_main_ui)
        self.connect_BTN.setGeometry(QtCore.QRect(20, 180, 71, 24))
        self.connect_BTN.setObjectName("connect_BTN")
        self.signin_BTN = QtWidgets.QPushButton(client_main_ui)
        self.signin_BTN.setGeometry(QtCore.QRect(120, 180, 71, 24))
        self.signin_BTN.setObjectName("signin_BTN")
        self.allmsg_TB = QtWidgets.QTextBrowser(client_main_ui)
        self.allmsg_TB.setGeometry(QtCore.QRect(260, 20, 511, 211))
        self.allmsg_TB.setObjectName("allmsg_TB")
        self.sendmsg_BTN = QtWidgets.QPushButton(client_main_ui)
        self.sendmsg_BTN.setGeometry(QtCore.QRect(260, 340, 75, 24))
        self.sendmsg_BTN.setObjectName("sendmsg_BTN")
        self.insertimg_BTN = QtWidgets.QPushButton(client_main_ui)
        self.insertimg_BTN.setGeometry(QtCore.QRect(350, 340, 75, 24))
        self.insertimg_BTN.setObjectName("insertimg_BTN")
        self.insertfile_BTN = QtWidgets.QPushButton(client_main_ui)
        self.insertfile_BTN.setGeometry(QtCore.QRect(440, 340, 75, 24))
        self.insertfile_BTN.setObjectName("insertfile_BTN")
        self.sendmsg_TE = QtWidgets.QTextEdit(client_main_ui)
        self.sendmsg_TE.setGeometry(QtCore.QRect(260, 250, 511, 71))
        self.sendmsg_TE.setObjectName("sendmsg_TE")
        self.uploadfile_BTN = QtWidgets.QPushButton(client_main_ui)
        self.uploadfile_BTN.setGeometry(QtCore.QRect(20, 250, 71, 24))
        self.uploadfile_BTN.setObjectName("uploadfile_BTN")
        self.downloadfile_BTN = QtWidgets.QPushButton(client_main_ui)
        self.downloadfile_BTN.setGeometry(QtCore.QRect(120, 250, 71, 24))
        self.downloadfile_BTN.setObjectName("downloadfile_BTN")

        self.retranslateUi(client_main_ui)
        QtCore.QMetaObject.connectSlotsByName(client_main_ui)

    def retranslateUi(self, client_main_ui):
        _translate = QtCore.QCoreApplication.translate
        client_main_ui.setWindowTitle(_translate("client_main_ui", "客户端"))
        self.coursename_LB.setText(_translate("client_main_ui", "课程名称"))
        self.stunum_LB.setText(_translate("client_main_ui", "学号"))
        self.passwd_LB.setText(_translate("client_main_ui", "密码"))
        self.IP_address_LB.setText(_translate("client_main_ui", "IP地址"))
        self.portnum_LB.setText(_translate("client_main_ui", "端口"))
        self.connect_BTN.setText(_translate("client_main_ui", "连接"))
        self.signin_BTN.setText(_translate("client_main_ui", "报道"))
        self.sendmsg_BTN.setText(_translate("client_main_ui", "发送"))
        self.insertimg_BTN.setText(_translate("client_main_ui", "插入图片"))
        self.insertfile_BTN.setText(_translate("client_main_ui", "插入文件"))
        self.uploadfile_BTN.setText(_translate("client_main_ui", "上传文件"))
        self.downloadfile_BTN.setText(_translate("client_main_ui", "下载文件"))
