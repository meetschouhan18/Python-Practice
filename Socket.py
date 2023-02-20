import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org' , 80) )
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#encode converts unicode(string) in UTF-8 code
mysock.send(cmd)
while True:
    data = mysock.recv(512)
#data variable recieves 512 characters
    if (len(data) < 1):
        break
    print(data.decode())
#converts UTF-8 encoded data into unicode
mysock.close()
