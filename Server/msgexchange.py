import socket
import threading
import time
from PIL import Image
import os

from filetransfer import fetchFileList, receiveFiles, sendFiles

current_task = 0


def receiveMsg(name, num, addr, conn, textbrowser):
    from loginverify import conn_list
    conn.sendall(('%s %s' % (num, name)).encode())
    # test_connection_thread = threading.Thread(target=isClientStillConnected, args=(conn, ))
    # test_connection_thread.start()
    while True:
        try:
            data = conn.recv(1024).decode()
            if data == '#03':  # 03功能符：请求文件列表
                current_task = 3
                foldersrc = r'resources'
                filelst = fetchFileList(foldersrc)
                # time.sleep(2)
                conn.sendall(("%s %d" % ("#03", len(filelst))).encode())
                # conn.sendall(str(len(filelst)).encode())
                if conn.recv(1024).decode() == "#03":
                    for i, file in enumerate(filelst):
                        # conn.sendall(file.encode())
                        conn.sendall(("%s,%d" % (file, os.path.getsize("%s/%s" % (foldersrc, file)))).encode())
            elif data.split(',')[0] == '#04':
                filepath = data.split(',')[1]
                filename = filepath.split('/')[len(filepath.split('/')) - 1]
                receiveFiles(filename, conn)
            elif data.split()[0] == '#05':
                tosend_num = data.split()[1]
                tosend_list = []
                print(tosend_num)
                conn.sendall("#05".encode())
                for i in range(int(tosend_num)):
                    filename = conn.recv(1024).decode()
                    tosend_list.append(filename)
                print(tosend_list)
                sendFiles(tosend_list, conn)
            elif data != '#':
                textbrowser.append("%s %s%s: %s" % (str(addr), num, name, data))
                for i, con in enumerate(conn_list):
                    if con["StuNo"] != num:
                        con["Conn"].sendall(("%s %s: %s" % (num, name, data)).encode())

        except (ConnectionResetError, OSError):
            break


def isClientStillConnected(conn):
    while True:
        if current_task == 3:
            break
        else:
            try:
                conn.send("#".encode())
                time.sleep(8)
            except (ConnectionResetError, OSError):
                conn.close()
                break
    abortTask()


def abortTask(conn):
    while True:
        if current_task != 3:
            break
    isClientStillConnected(conn)
