import socket
import sys
import pyperclip

class Ping:

    def __init__(self):
        if len(sys.argv) > 0:
            try:
                self.ping_server(sys.argv[1])
            except:
                print("An error occured")


        else:
            print("Enter a valid ip")


    def ping_server(self, ip):
        self.ipaddr = socket.gethostbyname(ip)
        print(self.ipaddr)
        pyperclip.copy(self.ipaddr)


Ping()
