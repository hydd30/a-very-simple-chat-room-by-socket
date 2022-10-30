from PySide2 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title1_LB = QtWidgets.QLabel(self.centralwidget)
        self.title1_LB.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.title1_LB.setObjectName("title1_LB")

        self.lesson_name_LB = QtWidgets.QLabel(self.centralwidget)
        self.lesson_name_LB.setGeometry(QtCore.QRect(10, 50, 53, 16))
        self.lesson_name_LB.setTextFormat(QtCore.Qt.MarkdownText)
        self.lesson_name_LB.setObjectName("lesson_name_LB")
        self.lesson_name_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.lesson_name_TEXT.setGeometry(QtCore.QRect(70, 50, 161, 21))
        self.lesson_name_TEXT.setObjectName("lesson_name_TEXT")

        self.ip_address_LB = QtWidgets.QLabel(self.centralwidget)
        self.ip_address_LB.setGeometry(QtCore.QRect(10, 110, 53, 16))
        self.ip_address_LB.setTextFormat(QtCore.Qt.MarkdownText)
        self.ip_address_LB.setObjectName("ip_address_LB")
        self.ip_address_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_address_TEXT.setGeometry(QtCore.QRect(70, 110, 161, 21))
        self.ip_address_TEXT.setObjectName("ip_address_TEXT")

        self.port_num_LB = QtWidgets.QLabel(self.centralwidget)
        self.port_num_LB.setGeometry(QtCore.QRect(10, 140, 53, 16))
        self.port_num_LB.setTextFormat(QtCore.Qt.MarkdownText)
        self.port_num_LB.setObjectName("port_num_LB")

        self.port_num_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.port_num_TEXT.setGeometry(QtCore.QRect(70, 140, 71, 21))
        self.port_num_TEXT.setObjectName("port_num_TEXT")

        self.stu_list_src_LB = QtWidgets.QLabel(self.centralwidget)
        self.stu_list_src_LB.setGeometry(QtCore.QRect(10, 80, 53, 16))
        self.stu_list_src_LB.setTextFormat(QtCore.Qt.MarkdownText)
        self.stu_list_src_LB.setObjectName("stu_list_src_LB")

        self.stu_list_src_TEXT = QtWidgets.QLineEdit(self.centralwidget)
        self.stu_list_src_TEXT.setGeometry(QtCore.QRect(70, 80, 161, 21))
        self.stu_list_src_TEXT.setObjectName("stu_list_src_TEXT")

        self.stu_list_src_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.stu_list_src_BTN.setGeometry(QtCore.QRect(233, 80, 21, 21))
        self.stu_list_src_BTN.setObjectName("stu_list_src_BTN")

        # 设置完成 PushButton
        self.set_up_ip_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.set_up_ip_BTN.setGeometry(QtCore.QRect(160, 140, 75, 24))
        self.set_up_ip_BTN.setObjectName("set_up_ip_BTN")
        #self.set_up_ip_BTN.clicked.connect(lambda: threading.Thread(target=self.verifyLogin, args=()))
        # self.set_up_ip_BTN.clicked.connect(self.verifyLogin)    # 信号->登陆验证

        # 显示学生签到情况 TextBox
        self.stu_sign_in_TB = QtWidgets.QTextBrowser(self.centralwidget)
        self.stu_sign_in_TB.setGeometry(QtCore.QRect(280, 40, 491, 121))
        self.stu_sign_in_TB.setObjectName("stu_sign_in_TB")

        # 显示未签到学生 PushButton
        self.print_absent_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.print_absent_BTN.setGeometry(QtCore.QRect(280, 180, 101, 24))
        self.print_absent_BTN.setObjectName("print_absent_BTN")

        # 显示已签到人数 LCDNumber
        self.stu_num_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.stu_num_LCD.setGeometry(QtCore.QRect(660, 40, 81, 51))
        self.stu_num_LCD.setObjectName("stu_num_LCD")
        self.stu_num_LCD.setDigitCount(3)
        self.stu_num_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.all_message_TB = QtWidgets.QTextBrowser(self.centralwidget)
        self.all_message_TB.setGeometry(QtCore.QRect(280, 250, 491, 211))
        self.all_message_TB.setObjectName("all_message_TB")

        self.send_msg_TEXT = QtWidgets.QTextEdit(self.centralwidget)
        self.send_msg_TEXT.setGeometry(QtCore.QRect(280, 470, 491, 131))
        self.send_msg_TEXT.setObjectName("send_msg_TEXT")

        self.send_msg_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.send_msg_BTN.setGeometry(QtCore.QRect(280, 620, 75, 24))
        self.send_msg_BTN.setObjectName("send_msg_BTN")

        self.insert_jpg_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.insert_jpg_BTN.setGeometry(QtCore.QRect(380, 620, 75, 24))
        self.insert_jpg_BTN.setObjectName("insert_jpg_BTN")

        # self.send_file_BTN = QtWidgets.QPushButton(self.centralwidget)
        # self.send_file_BTN.setGeometry(QtCore.QRect(480, 620, 75, 24))
        # self.send_file_BTN.setObjectName("send_file_BTN")

        # 开启小测 PushButton
        # self.start_test_BTN = QtWidgets.QPushButton(self.centralwidget)
        # self.start_test_BTN.setGeometry(QtCore.QRect(10, 250, 75, 24))
        # self.start_test_BTN.setObjectName("start_test_BTN")
        # self.start_test_BTN.clicked.connect(self.openLiteTestWindow)
        # self.set_up_ip_BTN.clicked.connect(lambda: threading.Thread(target=self.openLiteTestWindow, args=()))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title1_LB.setText(_translate("MainWindow", "课程信息与IP设置"))
        self.lesson_name_LB.setText(_translate("MainWindow", "课程名称"))
        self.ip_address_LB.setText(_translate("MainWindow", "IP地址"))
        self.port_num_LB.setText(_translate("MainWindow", "端口号"))
        self.stu_list_src_LB.setText(_translate("MainWindow", "学生名单"))
        self.stu_list_src_BTN.setText(_translate("MainWindow", "..."))
        self.set_up_ip_BTN.setText(_translate("MainWindow", "设置完成"))
        self.print_absent_BTN.setText(_translate("MainWindow", "显示未签到学生"))
        self.send_msg_BTN.setText(_translate("MainWindow", "发送消息"))
        self.insert_jpg_BTN.setText(_translate("MainWindow", "插入图片"))
        # self.send_file_BTN.setText(_translate("MainWindow", "插入文件"))
        # self.start_test_BTN.setText(_translate("MainWindow", "开启小测"))
