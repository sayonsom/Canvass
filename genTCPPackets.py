#!/usr/bin/python
from scapy.all import *

ip=IP(src="10.0.0.1", dst="10.0.0.2")
TCP_SYN=TCP(sport=1500, dport=80, flags="S", seq=100)
TCP_SYNACK=sr1(ip/TCP_SYN)

my_ack = TCP_SYNACK.seq + 1
TCP_ACK=TCP(sport=1500, dport=80, flags="A", seq=101, ack=my_ack)
send(ip/TCP_ACK)

my_payload="space for rent!"
TCP_PUSH=TCP(sport=1500, dport=80, flags="PA", seq=102, ack=my_ack)
try:
    send(ip/TCP_PUSH/my_payload)
except:
    print("Sorry not working")
