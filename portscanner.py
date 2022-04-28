import socket
import sys
import pyfiglet
from _datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("what ip are we checking: "))


#Banner
print("_" * 50)
print("scanning target: " + target)
print("scanning started at: " + str(datetime.now()))
print("_" * 50)

try:

    #scan every port on the system ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open" .format(port))
        s.close()

except KeyboardInterrupt:
        print("\n Exiting :( ")
        sys.exit()

except socket.error:
        print("\ Host Not responding :(")
        sys.exit()








