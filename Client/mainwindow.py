# -*- coding: utf-8 -*-


from winreg import SetValue
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QImage, QTextDocument
from PySide2.QtWidgets import QMainWindow, QFileDialog, QWidget
from PySide2.QtCore import QUrl

import os
import sys
import socket
import threading
import struct
import time

from main_ui import Ui_client_main

filepath_lst = []

state = 0

progress = 0


class MyMainWindow(QMainWindow, Ui_client_main):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # self.automaticSetup(1)
        self.current_task = 0

        # self.sk.bind((socket.gethostbyname(socket.gethostname()), 62263))

        # 绑定槽函数
        self.connect_BTN.clicked.connect(self.clientInitialize)
        self.sendmsg_BTN.clicked.connect(self.clientSendMsgs)
        self.downloadfile_BTN.clicked.connect(self.clientFetchServerFilelst)
        # self.downloadfile_BTN.clicked.connect(self.clientFetchServerFilelst_Thread)
        self.uploadfile_BTN.clicked.connect(self.clientSendFiles)

    def automaticSetup(self, num):
        self.IP_address_LE.setText('192.168.1.101')
        # self.IP_address_LE.setText('192.168.210.174')
        self.portnum_LE.setText('80')
        self.password_LE.setText('123')
        if num == 1:
            self.stunum_LE.setText('2021080902018')
        elif num == 2:
            self.stunum_LE.setText('2021080902024')
        elif num == 3:
            self.stunum_LE.setText('2021080902002')
        elif num == 4:
            self.stunum_LE.setText('2021080902031')

    def clientInitialize(self):
        self.server_ip = self.IP_address_LE.text()
        self.server_port = self.portnum_LE.text()
        self.coursename = self.coursename_LE.text()
        self.stunum = self.stunum_LE.text()
        self.pwd = self.password_LE.text()
        self.clientConnectServer_Thread()

    def clientConnectServer(self):
        try:
            self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sk_for_download = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sk_for_upload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            self.sk.connect((self.server_ip, int(self.server_port)))
        except OSError:
            pass
        if self.sk.recv(1024).decode() == '#00':  # 00: 发送连接请求
            self.sk.send(self.stunum.encode())
            self.sk.send(self.pwd.encode())
            try:
                data = self.sk.recv(1024).decode()
                if data.split()[0] == '#01':  # 01: 回应验证通过
                    self.allmsg_TB.append(data.split()[1])
                    data = self.sk.recv(1024).decode()
                    self.stunum = data.split()[0]
                    self.name = data.split()[1]
                    recv_thread = threading.Thread(target=self.clientReceiveMsgs, args=())
                    recv_thread.start()
                elif data.split()[0] == '#02':  # 02: 验证不通过
                    self.allmsg_TB.append(data.split()[1])
                    self.sk.close()
                    return
            except (ConnectionResetError, ConnectionError):
                return

    def clientConnectServer_Thread(self):
        thread = threading.Thread(target=self.clientConnectServer, args=())
        thread.start()

    def clientRetryConnectServer(self):
        self.sk.send('#00'.encode())
        if self.sk.recv(1024).decode() == '#00':
            self.sk.send(self.stunum.encode())
            self.sk.send(self.pwd.encode())
            try:
                data = self.sk.recv(1024).decode()
                if data.split()[0] == '#01':
                    self.allmsg_TB.append(data.split()[1])
                    data = self.sk.recv(1024).decode()
                    self.stunum = data.split()[0]
                    self.name = data.split()[1]
                    thread = threading.Thread(target=self.clientReceiveMsgs, args=())
                    thread.start()
                elif data.split()[0] == '#02':
                    self.allmsg_TB.append(data.split()[1])
                    return
            except:
                return

    def clientSendMsgs(self):
        # self.send_data = self.sendmsg_TE.toMarkdown()
        self.send_data = self.sendmsg_TE.toPlainText()
        self.sk.send(self.send_data.encode())
        self.sendmsg_TE.clear()
        self.allmsg_TB.append("%s %s: %s" % (self.stunum, self.name, self.send_data))

    def clientReceiveMsgs(self):
        self.filenum = 0
        self.filelst = []
        while True:
            try:
                recv_data = self.sk.recv(1024).decode()
                if recv_data == '#':
                    self.sk.send("#".encode())
                elif recv_data.startswith('#03'):
                    self.filenum = 0
                    self.filelst = []
                    self.filenum = int(recv_data.split()[1])
                    self.sk.send("#03".encode())
                    for i in range(self.filenum):
                        file = self.sk.recv(1024).decode()
                        self.filelst.append(file.split(','))
                        self.current_task = 3
                        # self.formFilelstTable(filenum, filelst)
                elif recv_data.split()[0] == '#04':
                    pass
                elif recv_data.split()[0] == '#05':
                    for filename in self.todownload_list:
                        self.sk.send(filename.encode())
                elif recv_data.split(',')[0] == '#06':
                    filename = recv_data.split(',')[1]
                    self.downloadFiles(filename)
                elif recv_data.split(',')[0] == '#07':
                    filename = recv_data.split(',')[1]
                    self.receivePics(filename)
                elif recv_data.split(',')[0] == '#08':
                    filename = recv_data.split(',')[1]
                    self.receiveFiles(filename)
                else:
                    self.allmsg_TB.append(recv_data)
            except (ConnectionResetError, OSError):
                break
        return

    def clientFetchServerFilelst(self):
        self.sk.send("#03".encode())
        while self.current_task != 3:
            time.sleep(0.2)
        self.current_task = 0
        self.formFilelstTable(self.filenum, self.filelst)
        # self.formFilelstTable(filenum, filelst)

    # aborted
    def clientFetchServerFilelst_Thread(self):
        thread = threading.Thread(target=self.clientFetchServerFilelst, args=())
        thread.start()

    def openFileList(self):
        filesrcs = QFileDialog.getOpenFileNames(self, '打开本地文件', '', 'All Files(*)')
        return filesrcs[0]

    def clientSendFiles(self):
        filesrcs = self.openFileList()
        for i in range(len(filesrcs)):
            filesrcs[i] = [filesrcs[i], os.path.getsize(filesrcs[i])]
        # self.formFilelstTable(len(filesrcs), filesrcs)
        self.formFilelstTable(len(filesrcs), filesrcs)

    def sendFiles(self, filepathlist):
        for filepath in filepathlist:
            self.sk.send(('%s,%s' % ('#04', filepath[0])).encode())
            size = os.stat(filepath[0]).st_size
            f = struct.pack("l", size)
            self.sk.send(f)

            file = open(filepath[0], 'rb')
            self.sk.send(file.read())
            print("ok")
        self.MainWindow.close()

    def clientDownloadFiles(self, item):
        self.sk.send(("%s %d" % ('#05', len(self.todownload_list))).encode())

    def downloadFiles(self, filename):
        global progress
        self.Form.label.setText('')
        d = self.sk.recv(struct.calcsize("l"))
        size = struct.unpack("l", d)
        num = size[0] // 1024
        data = b''
        times = num // 10
        self.Form.progressBar.setValue(0)
        for i in range(num+1):
            progress = int(i * 100 / num)
            self.Form.label.setText("%s%s" % (str(progress), r"%"))
            if int(i / times) == i / times or i == num:
                progress = int(i * 100 / num)
                # self.Form.progressBar.setValue(progress)
            if i < num:
                data += self.sk.recv(1024)
            else:
                data += self.sk.recv(size[0] % 1024)

        with open(('%s/%s' % ('filerecv', filename)), 'wb') as f:
            f.write(data)
        self.Form.label.setText('下载完成！')
        print('ok')

    def receivePics(self, filename):
        d = self.sk.recv(struct.calcsize("l"))
        size = struct.unpack("l", d)
        num = size[0] // 1024
        data = b''
        times = num // 10
        for i in range(num+1):
            if i < num:
                data += self.sk.recv(1024)
            else:
                data += self.sk.recv(size[0] % 1024)

        with open(('%s/%s' % ('cache/pic', filename)), 'wb') as f:
            f.write(data)
        print('ok')

        image = QImage('%s/%s' % ('cache/pic', filename))
        thumb_w = 300
        thumb_h = int(300 * int(image.height()) / int(image.width()))
        del image
        self.allmsg_TB.append("server:")
        self.allmsg_TB.insertHtml("<html><head></head><body><img src=%s width=%d height=%d></body></html>" % ('%s/%s' % ('cache/pic', filename), thumb_w, thumb_h))

    def receiveFiles(self, filename):
        d = self.sk.recv(struct.calcsize("l"))
        size = struct.unpack("l", d)
        num = size[0] // 1024
        data = b''
        times = num // 10
        for i in range(num+1):
            if i < num:
                data += self.sk.recv(1024)
            else:
                data += self.sk.recv(size[0] % 1024)

        with open(('%s/%s' % ('filerecv', filename)), 'wb') as f:
            f.write(data)
        print('ok')

    def formFilelstTable(self, filenum, filelst):
        import downloadfile_ui
        self.MainWindow = QtWidgets.QMainWindow()
        self.Form = downloadfile_ui.download_file_ui()
        self.Form.setupUi(self.MainWindow)

        self.MainWindow.resize(695, filenum * 40 + 90)
        self.Form.tableWidget.setGeometry(QtCore.QRect(30, 10, 641, filenum * 40))
        self.Form.tableWidget.setColumnCount(3)
        self.Form.tableWidget.setRowCount(filenum)
        self.Form.download_BTN.setGeometry(QtCore.QRect(40, filenum*40 + 35, 75, 24))
        self.Form.upload_BTN.setGeometry(QtCore.QRect(130, filenum*40 + 35, 75, 24))
        self.Form.progressBar.setGeometry(QtCore.QRect(250, filenum*40 + 35, 320, 24))
        self.Form.label.setGeometry(QtCore.QRect(600, filenum*40 + 35, 75, 24))
        for i, fileitem in enumerate(filelst):
            newItem = QtWidgets.QTableWidgetItem(str(i+1))
            self.Form.tableWidget.setItem(i, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(fileitem[0])
            self.Form.tableWidget.setItem(i, 1, newItem)
            tmp = int(fileitem[1])
            j = 0
            suffix = ['字节', 'KB', 'MB', 'GB']
            while tmp >= 1024:
                tmp = tmp / 1024
                j += 1
            newItem = QtWidgets.QTableWidgetItem("%.2f%s" % (tmp, suffix[j]))
            # newItem = QtWidgets.QTableWidgetItem(fileitem[1])
            self.Form.tableWidget.setItem(i, 2, newItem)

        self.Form.tableWidget.setShowGrid(False)
        self.Form.tableWidget.horizontalHeader().setVisible(False)
        self.Form.tableWidget.verticalHeader().setVisible(False)
        self.Form.tableWidget.resizeColumnsToContents()

        self.Form.upload_BTN.clicked.connect(lambda: self.sendFiles(filelst))
        self.Form.tableWidget.itemClicked.connect(self.formDownloadFilelist)
        self.Form.download_BTN.clicked.connect(self.clientDownloadFiles)

        self.MainWindow.show()

    def formDownloadFilelist(self, item=None):
        self.todownload_list = []
        self.todownload_list.append(item.text())
        print(self.todownload_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
