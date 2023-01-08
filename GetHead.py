import  socket                        

target = 'packthub.samsclass.info'
port = input("Port Number:")
try:
        
        s.connect((target, port))
        req = 'HEAD / HTTP/1.1\r\nHost: '+ target+'\r\n\r\n'
        print('Sending')
        print(req)
        s.send(req)
        print(s.recv(1024))
        s.close()
except socket.error as err:
        print(err)

