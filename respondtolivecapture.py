"""
Usage: thisfile.py <interface> <physicalsystem> <packetThreshold> <monitorDuration>

"""

import pyshark
import os
import subprocess

howLong = 10
print("ADS is working")

cap = pyshark.LiveCapture(interface="h1-eth0")
cap.sniff(timeout = howLong)

usualNumberOfPacket = 80

print(cap)

if len(cap)>5:
    print("[!] DOS attack detected")
    print("[!] Monitoring Matrix Flag Changed from 0 to 1.")

    output = subprocess.check_output("xterm -e bash ~/script.sh;bash\"", shell=True)
    print output
