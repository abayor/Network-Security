import  socket
s= socket.socket()                        

target = 'packtpub.samsclass.info' 
port = input("Port Number:")
try:
        
        s.connect((target, int(port)))
        req = 'HEAD / HTTP/1.1\r\nHost: '+ target+'\r\n\r\n'
        print('Sending.......')
        print(req)
        a = req.encode('utf-8')
        s.send(a)
       
        print(s.recv(1024))
        print(".....Received!! \n Done")
        s.close()
except socket.error as err:
        print(err)

