#coding=gbk
'''
Created on 2014年7月17日

@author: Administrator
'''
import socket

HOST = '127.0.0.1'
PORT = 10001

print "Attempting connection"
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    mySocket.connect((HOST,PORT))
except socket.error:
    print "Call to connect failed"
    
print "Connect to Server"

serverMessage = mySocket.recv(1024)
while serverMessage != "SERVER>>> TERMINATE":
    if not serverMessage:
        break
    print serverMessage
    clientMessage = raw_input("CLIENT>>> ")
    mySocket.send("CLIENT>>> " + clientMessage)
    temp = mySocket.recv(1024)
    while temp:
        serverMessage += temp
        temp = mySocket.recv(1024)
    
print "Connection terminated"
mySocket.close()

