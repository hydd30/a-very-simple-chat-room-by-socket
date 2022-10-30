import socket
import threading
import time
import xlrd
from xlutils.copy import copy
from msgexchange import receiveMsg

conn_list = []


def establishSocket(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((ip, port))
    sk_for_download = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk_for_download.bind((ip, port+1))
    sk_for_upload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk_for_upload.bind((ip, port+2))
    return [sk, sk_for_download, sk_for_upload]


def fetchStuList(filesrc):
    data = xlrd.open_workbook(filesrc)
    table = data.sheets()[0]
    stu_list = []
    for row in range(table.nrows):
        stu_list.append(table.row_values(row))
    for i in range(len(stu_list)):
        stu_list[i].append(0)

    new_xls = copy(data)
    sheet = new_xls.get_sheet(0)
    for i, row in enumerate(range(table.nrows)):
        sheet.write(i, table.ncols, '未签到')
    new_xls.save(filesrc)
    return stu_list


def acceptClientLogin(stu_list, conn, addr, textBrowser1, lcdnumber, textBrowser2, filesrc):
    data = xlrd.open_workbook(filesrc)
    table = data.sheets()[0]
    new_xls = copy(data)
    sheet = new_xls.get_sheet(0)

    global conn_list
    conn.sendall("#00".encode())
    username = conn.recv(1024).decode()
    password = conn.recv(1024).decode()
    login_stu_num = 0
    for i in range(len(stu_list)):
        if stu_list[i][len(stu_list[i]) - 1] == 1:
            login_stu_num = login_stu_num + 1

    i = 0
    while True:
        try:
            if stu_list[i][0] == username and password == '123':
                if stu_list[i][len(stu_list[i]) - 1] == 1:
                    try:
                        conn.sendall('#01 已登录！请勿重复登录'.encode())
                    except ConnectionResetError:
                        pass
                    for j in range(len(conn_list)):
                        if conn_list[j]["StuNo"] == stu_list[i][0]:
                            conn_list.pop(j)
                            conn_list.append({"StuNo": stu_list[i][0], "Name": stu_list[i][1], "Conn": conn, "Addr": addr})
                else:
                    # textBrowser1.append(str(addr) + stu_list[i][0] + stu_list[i][1] + ' 登录')
                    textBrowser1.append("%s %s%s登陆成功" % (str(addr), stu_list[i][0], stu_list[i][1]))
                    conn.sendall('#01 登陆成功！'.encode())
                    stu_list[i].append(1)
                    login_stu_num = login_stu_num + 1
                    lcdnumber.display(login_stu_num)
                    conn_list.append({"StuNo": stu_list[i][0], "Name": stu_list[i][1], "Conn": conn, "Addr": addr})

                    sheet.write(i, table.ncols-1, '已签到')
                    new_xls.save(filesrc)
                recv_thread = threading.Thread(target=receiveMsg, args=(stu_list[i][1], stu_list[i][0], addr, conn, textBrowser2))
                recv_thread.start()
                break
            else:
                i = i + 1
        except IndexError:
            conn.sendall("#02 用户名或密码错误！请重试".encode())
            conn.close()
            break


def loginMainFunction(ip, port, filesrc, widget):
    sk = establishSocket(ip, port)
    stu_list = fetchStuList(filesrc)
    while True:
        sk.listen(5)
        conn, addr = sk.accept()
        verify_thread = threading.Thread(target=acceptClientLogin, args=(stu_list, conn, addr, widget))
        verify_thread.start()
