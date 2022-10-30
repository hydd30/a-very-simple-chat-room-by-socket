import os
import socket
import struct
from tqdm.gui import tqdm_gui


def fetchFileList(src):
    filelst = os.listdir(src)
    with open("temp/filelst.txt", "w") as f:
        for i, file in enumerate(filelst):
            f.write("%d %s\n" % (i, file))

    return filelst


def receiveFiles(filename, conn):
    d = conn.recv(struct.calcsize("l"))
    size = struct.unpack("l", d)
    num = size[0] // 1024
    data = b''
    for i in range(num+1):
        if i < num:
            data += conn.recv(1024)
        else:
            data += conn.recv(size[0] % 1024)

    with open(('%s/%s' % ('filerecv', filename)), 'wb') as f:
        f.write(data)

    conn.sendall(('%s传输成功！' % filename).encode())


def sendFiles(filenamelst, conn):
    for filename in filenamelst:
        conn.sendall(("%s,%s" % ('#06', filename)).encode())
        filepath = "%s%s" % ('C:/Users/30455/Desktop/Python_Program/resources/', filename)
        size = os.stat(filepath).st_size
        f = struct.pack("l", size)
        conn.sendall(f)

        file = open(filepath, 'rb')
        conn.sendall(file.read())


def sendPics(filesrclst, conn):
    for filesrc in filesrclst:
        print(filesrc)
        conn.sendall(("%s,%s" % ('#07', filesrc.split('/')[len(filesrc.split('/'))-1])).encode())
        size = os.stat(filesrc).st_size
        f = struct.pack("l", size)
        conn.sendall(f)

        file = open(filesrc, 'rb')
        conn.sendall(file.read())
