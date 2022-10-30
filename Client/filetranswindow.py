from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QImage, QTextDocument
from PySide2.QtWidgets import QMainWindow, QFileDialog, QWidget
from PySide2.QtCore import QUrl

from downloadfile_ui import download_file_ui
from mainwindow import MyMainWindow


class FiletransWindow(MyMainWindow, download_file_ui):
    def __init__(self, parent=None):
        super(FiletransWindow, self).__init__(parent)
        # MyMainWindow.__init__(self)
        # download_file_ui.setupUi(self)
        self.setupUi(self)

        self.upload_BTN.clicked.connect(self.clientSendFiles)
        self.download_BTN.clicked.connect(self.clientFetchServerFilelst)

    def formTable(self, filenum, filesrcs):
        MainWindow = QtWidgets.QMainWindow()
        self.Form = download_file_ui()
        self.Form.setupUi(self.MainWindow)

        MainWindow.resize(695, filenum * 40 + 90)
        self.Form.tableWidget.setGeometry(QtCore.QRect(30, 10, 641, filenum * 40))
        self.Form.tableWidget.setColumnCount(3)
        self.Form.tableWidget.setRowCount(filenum)
        self.Form.download_BTN.setGeometry(QtCore.QRect(40, filenum*40 + 35, 75, 24))
        self.Form.upload_BTN.setGeometry(QtCore.QRect(130, filenum*40, 75, 24))
        for i, fileitem in enumerate(filesrcs):
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

        MainWindow.show()
