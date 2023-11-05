#coding=gbk
'''
Created on 2014年7月17日

@author: Administrator
'''

import socket
import sqlite3

def food_query(query):
    
    conn = sqlite3.connect('../../tmp/food.db')
    curs = conn.cursor()
    query = 'select * from food where %s' % (query)
    curs.execute(query)
    result = ''
    column_name = [des[0] for des in curs.description]
    for row in curs.fetchall():
        for pair in zip(column_name,row):
            result += str(pair[0]) + ':' + str(pair[1]) + '\n'
        result += '\n'
    return result
    
     

HOST = '127.0.0.1'
PORT = 10001
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mySocket.bind((HOST,PORT))
except socket.error:
    print "Call to bind failed"

print 'Waiting for connecting'
mySocket.listen(1)

while True:
    connection,address = mySocket.accept()
    print "Connection","received from:",address[0]
    
    connection.send('SERVER>>> Connection successful')
    clientMessage = connection.recv(1024)
    while clientMessage != 'CLIENT>>> TERMINATE':
        if not clientMessage:
            break
        
        print clientMessage
        
        content = str(clientMessage).split(' ')
        #print content
        
        serverMessage = food_query(content[1])
        print serverMessage
        connection.send("SERVER>>> \n" + serverMessage)
        clientMessage = connection.recv(1024)
        
    print 'Connection termianted'
    connection.close()

