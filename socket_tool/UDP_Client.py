
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *
import sys
import time
import os
import math

host='172.0.0.1'
port = 8989

starttime = time.time()
udpClientSocket = socket(AF_INET, SOCK_STREAM)


serAddr = (host, port)
udpClientSocket.connect(serAddr)
#Disable nalge
#udpClientSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, True)
udpClientSocket.send(b"\x02\xfd\x00\xe4\xe4\xe4\xe4\x07\x0e\x80\x00\x00\x00\x00\x00")	
# Routing activation request
#udpClientSocket.send(b"\x02\xfd\x00\x05\x00\x00\x00\x07\x0e\x80\x00\x00\x00\x00\x00")	
# # Routing activation response
# recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# # 10 03
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x06\x0e\x80\x00\x22\x10\x01")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)


# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x07\x0e\x80\x00\x22\x22\xf1\x80")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)
# exit()
# # # 31 01 02 03
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x08\x0e\x80\x00\x22\x31\x01\x02\03")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# #31 01 0202 Checksum 
# appchecksum = 0
# payloadLen = 12
# appchecksumbytes = appchecksum.to_bytes(4,byteorder='little')
# sendData = b"\x02\xfd\x80\x01"+payloadLen.to_bytes(4,byteorder='big')+b"\x0e\x80\x00\x22\x31\x01\x02\x02"+appchecksumbytes
# udpClientSocket.send(sendData)
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)
# exit()
# # #85 02 functional e4 00
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x06\xe4\x00\x00\x22\x85\x02")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# # #28 03 01 functional e4 00
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x07\xe4\x00\x00\x22\x28\x03\x01")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x07\x0e\x80\x00\x22\x22\xf1\x80")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# # # #22 f1 80
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x07\x0e\x80\x00\x22\x22\xf1\x84")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# # 10 02
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x06\x0e\x80\x00\x22\x10\x02")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)
# # exit()

# #27 07
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x06\x0e\x80\x00\x22\x27\x07")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)


# #27 08
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x0A\x0e\x80\x00\x22\x27\x08\x00\x00\x00\x00")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)



# # exit();
# #2e f1 84
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x1c\x0e\x80\x00\x22\x2e\xf1\x84\x02\x03\x04\x05\x06\x07\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x0A")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)

# # exit()

# #open bin file
# filepath = "D:\\Code\\yxx\\DCU_Code_CAL.bin"
# binfile = open(filepath,"rb")
# size = os.path.getsize(filepath)



# #31 01 FF 00 Erase memory
# # bytesSize = size.to_bytes(4,byteorder='little')
# bytesSize = size.to_bytes(4,byteorder='little')
# payloadLen = 17
# sendData = b"\x02\xfd\x80\x01"+payloadLen.to_bytes(4,byteorder='big')+b"\x0e\x80\x00\x22\x31\x01\xFF\x00\x44\x00\x00\x00\x00"+bytesSize
# udpClientSocket.send(sendData)
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)


# #34 00 44 00000000 
# bytesSize = size.to_bytes(4,byteorder='big')
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x0F\x0e\x80\x00\x22\x34\x00\x44\x00\x00\x00\x00"+bytesSize)
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)

# #4096 bytes one packet
# #36 xx data
# # appchecksum = 0

# packetnum = math.ceil(size/4096)
# seqCnt = 0
# for i in range(packetnum):
#     data = binfile.read(4096)
#     checksum = 0
#     for j in range(len(data)):
#         appchecksum += data[j]
    
#     payloadLen = 6+len(data)
#     seqCnt+=1

#     sendData = b"\x02\xfd\x80\x01"+payloadLen.to_bytes(4,byteorder='big')+b"\x0e\x80\x00\x22\x36"+(seqCnt%256).to_bytes(1,byteorder='big')+data
    
#     udpClientSocket.send(sendData)

#     recvdata = udpClientSocket.recv(1024)
#     recvdata = udpClientSocket.recv(1024)


# #37 
# payloadLen = 4+1
# sendData = b"\x02\xfd\x80\x01"+payloadLen.to_bytes(4,byteorder='big')+b"\x0e\x80\x00\x22\x37"
# udpClientSocket.send(sendData)
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)


# # #31 01 0202 Checksum 
# # payloadLen = 12
# # appchecksumbytes = appchecksum.to_bytes(4,byteorder='little')
# # sendData = b"\x02\xfd\x80\x01"+payloadLen.to_bytes(4,byteorder='big')+b"\x0e\x80\x00\x22\x31\x01\x02\x02"+appchecksumbytes
# # udpClientSocket.send(sendData)
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)


# # #31h 01h FFh 01h
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x08\x0e\x80\x00\x22\x31\x01\xff\x01")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)

# #2e f1 99
# udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x0a\x0e\x80\x00\x22\x2e\xf1\x99\x00\x00\x00")
# recvdata = udpClientSocket.recv(1024)
# recvdata = udpClientSocket.recv(1024)

# # # Reset MCU 11 01
# # udpClientSocket.send(b"\x02\xfd\x80\x01\x00\x00\x00\x06\x0e\x80\x00\x22\x11\x01")
# # recvdata = udpClientSocket.recv(1024)
# # recvdata = udpClientSocket.recv(1024)





# udpClientSocket.close()

# endtime = time.time()

# print(endtime-starttime)
