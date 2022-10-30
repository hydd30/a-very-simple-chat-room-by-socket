# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QImage, QTextDocument
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import QUrl

import sys
import threading
import xlrd

from main_ui import Ui_MainWindow
from lite_test_ui import Ui_MainWindow_litetest
from loginverify import loginMainFunction, establishSocket, fetchStuList, acceptClientLogin, conn_list
from msgexchange import receiveMsg
from filetransfer import fetchFileList, sendFiles, sendPics, sendPics


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pic_src_list = []
        # self.automaticSetup()

        self.set_up_ip_BTN.clicked.connect(self.setupParameter)
        # self.start_test_BTN.clicked.connect(self.openLiteTestWindow)
        self.send_msg_BTN.clicked.connect(self.fetchAndSendMsg)
        self.insert_jpg_BTN.clicked.connect(self.insertPictures)
        # self.send_file_BTN.clicked.connect(self.testFileTransferWidget)
        self.print_absent_BTN.clicked.connect(self.printAbsentStudents)
        self.stu_list_src_BTN.clicked.connect(self.selectStuList)

    def automaticSetup(self):
        self.ip_address_TEXT.setText('192.168.1.101')
        # self.ip_address_TEXT.setText('192.168.210.174')
        self.port_num_TEXT.setText('80')
        # self.stu_list_src_TEXT.setText(r'C:\Users\30455\Desktop\Python_Program\temp\test.xlsx')

    # 设定初始参数 槽函数<--set_up_ip_BTN
    def setupParameter(self):
        self.ip = self.ip_address_TEXT.text()
        self.port = int(self.port_num_TEXT.text())
        self.stu_list_src = self.stu_list_src_TEXT.text()
        self.lesson_name = self.lesson_name_TEXT.text()
        self.stu_list = fetchStuList(self.stu_list_src)
        self.verifyLogin_Thread()

    # 登陆验证 & 接收消息
    def verifyLogin(self):
        sk_list = establishSocket(self.ip, self.port)
        sk = sk_list[0]
        while True:
            sk.listen(5)
            conn, addr = sk.accept()
            sk_list[1].listen(5)
            conn_dl, addr_dl = sk.accept()
            sk_list[2].listen(5)
            conn_up, addr_up = sk.accept()
            connset = [conn, conn_dl, conn_up]
            arg_tuple = (self.stu_list, connset, addr, self.stu_sign_in_TB, self.stu_num_LCD, self.all_message_TB, self.stu_list_src)
            verify_thread = threading.Thread(target=acceptClientLogin, args=arg_tuple)
            verify_thread.start()

    # 创建登录线程
    def verifyLogin_Thread(self):
        thread = threading.Thread(target=self.verifyLogin, args=())
        thread.start()

    def printAbsentStudents(self):
        data = xlrd.open_workbook(self.stu_list_src)
        table = data.sheets()[0]
        stu_num = table.nrows
        stu_state = table.ncols

        import downloadfile_ui
        self.MainWindow = QtWidgets.QMainWindow()
        self.Form = downloadfile_ui.Ui_MainWindow()
        self.Form.setupUi(self.MainWindow)
        self.MainWindow.resize(695, stu_num * 40 + 90)
        self.Form.tableWidget.setGeometry(QtCore.QRect(30, 10, 641, stu_num * 40))
        self.Form.tableWidget.setColumnCount(3)
        self.Form.tableWidget.setRowCount(stu_num)

        for i in range(stu_num):
            item = table.row_values(i)
            newItem = QtWidgets.QTableWidgetItem(item[0])
            self.Form.tableWidget.setItem(i, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(item[1])
            self.Form.tableWidget.setItem(i, 1, newItem)
            newItem = QtWidgets.QTableWidgetItem(item[table.ncols - 1])
            self.Form.tableWidget.setItem(i, 2, newItem)

        self.Form.tableWidget.setShowGrid(False)
        self.Form.tableWidget.horizontalHeader().setVisible(False)
        self.Form.tableWidget.verticalHeader().setVisible(False)

        self.MainWindow.show()

    # 发送消息线程
    def fetchAndSendMsg(self):
        global conn_list
        if not self.send_msg_TEXT.toMarkdown().startswith('!'):
            self.send_data = self.send_msg_TEXT.toPlainText()
            for i, con in enumerate(conn_list):
                try:
                    con["Conn"].sendall(("%s %s" % ('server:', self.send_data)).encode())
                except OSError:
                    con["Conn"].close()
                    conn_list.pop(i)
            self.send_msg_TEXT.clear()
            self.all_message_TB.append("%s %s" % ("server:", self.send_data))
        else:
            for i, con in enumerate(conn_list):
                sendPics(self.pic_src_list, con["Conn"])
            self.all_message_TB.append("server:")
            self.all_message_TB.insertHtml("<html><head></head><body><img src=%s width=%d height=%d></body></html>" % (self.pic_src_list[0], self.thumb_lst_temp[0][1], self.thumb_lst_temp[0][2]))
            self.send_msg_TEXT.clear()

    # 槽函数：打开小测窗口

    # def openLiteTestWindow(self):
    #     import lite_test_ui
    #     self.MainWindow_litetest = QtWidgets.QMainWindow()
    #     self.lite_test_window = Ui_MainWindow_litetest()
    #     self.lite_test_window.setupUi(self.MainWindow_litetest)
    #     self.MainWindow_litetest.show()

    def openFileList(self):
        files = QFileDialog.getOpenFileNames(self, '打开本地文件', '', '*.jpg; *.png;;All Files(*)')
        return files[0]

    def selectStuList(self):
        files = QFileDialog.getOpenFileNames(self, '打开本地文件', '', '*.xls; *.xlsx;;All Files(*)')
        self.stu_list_src_TEXT.setText(files[0][0])
        # print(files[0][0])

    def insertPictures(self):
        self.img_lst_temp = []
        self.thumb_lst_temp = []
        self.pic_src_list = self.openFileList()
        for i, pic_src in enumerate(self.pic_src_list):
            image = QImage(pic_src)
            cursor = self.send_msg_TEXT.textCursor()
            document = self.send_msg_TEXT.document()
            document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
            thumb_w = 300
            thumb_h = int(300 * int(image.height()) / int(image.width()))
            thumb = image.scaled(4 * thumb_w, 4 * thumb_h).smoothScaled(thumb_w, thumb_h)
            cursor.insertImage(thumb)
            self.img_lst_temp.append(image)
            self.thumb_lst_temp.append([thumb, thumb_w, thumb_h])
        print(self.pic_src_list)
        print(self.thumb_lst_temp)

    def testFileTransferWidget(self):
        self.foldersrc = "temp"
        filelst = fetchFileList(self.foldersrc)
        filenum = len(filelst)
        import downloadfile_ui
        self.MainWindow = QtWidgets.QMainWindow()
        self.Form = downloadfile_ui.Ui_MainWindow()
        self.Form.setupUi(self.MainWindow)
        self.MainWindow.resize(695, filenum * 40 + 90)
        self.Form.tableWidget.setGeometry(QtCore.QRect(30, 10, 641, filenum * 40))
        self.Form.tableWidget.setColumnCount(2)
        self.Form.tableWidget.setRowCount(filenum)
        self.Form.pushButton.setGeometry(QtCore.QRect(40, filenum*40 + 35, 75, 24))

        for i, fileitem in enumerate(filelst):
            newItem = QtWidgets.QTableWidgetItem(str(i+1))
            self.Form.tableWidget.setItem(i, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(fileitem)
            self.Form.tableWidget.setItem(i, 1, newItem)

        self.Form.tableWidget.setShowGrid(False)
        self.Form.tableWidget.horizontalHeader().setVisible(False)
        self.Form.tableWidget.verticalHeader().setVisible(False)

        self.MainWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
