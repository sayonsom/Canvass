#!/usr/bin/python

"""Usage:
    simpleattack.py <model> busno <busnumber> [--scada] [--livecapture]

Options:
    -h --help           This file is used to operate the power system model.
    --version           (c) Sayonsom Chanda, 2017. Canvass 0.0.1
                        MIT License. Attribution required.
                        Software provided AS IS. No WARRANTIES.
    --verbose           This prints out a very detailed log of whats going on.
                        Helpful for debugging purposes.
    -s --scada          Write to a simulated SCADA server. Default configured to be
                        a Matrikon OPC Server, running on a Windows Machine.
                        USE THIS OPTION CAREFULLY.
                        ---------------------------
                        DO NOT USE THIS UNLESS YOU HAVE WINDOWS MACHINE SET UP
                        WITH SCADA SERVER SET UP
                        ----------------------------
                        You may need to disable Windows Firewall for this to work
                        properly.
                        Before writing to SCADA server, you will be asked to
                        input the IP Address of the Windows Machine each time.

    -l --livecapture    Captures Live Packets and saves them as a PCAP file for
                        later analysis
"""

from __future__ import unicode_literals
from shutil import *
from docopt import docopt
import os
import sys
import subprocess
from scapy.all import *
import time

reload(sys)
sys.setdefaultencoding('utf8')


def launchDOS(filename, choice):
    print("[~] Requesting physical model information")
    attStr = "python pf.py "+filename+" getinfoX"
    output = subprocess.check_output(attStr, shell=True)
    #print("[i] %s state of all buses" %filename)
    print(output)
    output = output.splitlines()
    #print("[i] Specifically, here's information about Bus Index %s:" %choice)

    interest = output[3+int(choice)]
    #print(interest)

    interest = interest.split( )
    busNo = interest[1]
    busP = interest[2]
    #busPinMW = int(busP)/1000.0
    busQ = interest[3]
    #busQinMVAR = int(busQ)/1000.0
    busStatus = interest[4]
    if busStatus == "True":
        busStatusSt = "[i] It is in service."
    else:
        busStatusSt = "[i] However, it is not in service."

    print("[i] Detected: Bus {0[1]} is connected {0[2]} kW, {0[3]} kVAR load now.\n{1}".format(interest, busStatusSt))

    changeStatus = raw_input("[?] Do you want to change the bus status? [PRESS 1 to CHANGE, any other key to Continue] >>>")
    if changeStatus == "1":
        attStr = "python pf.py "+filename+" flipBusBreakerX "+choice
        #os.system(attStr)
        output = subprocess.check_output(attStr, shell=True)
        #print(output)
        #output = subprocess.check_output(attStr, shell=True)
    else:
        print("[~] Proceeding to attack using existing bus status")
        time.sleep(1)
        print("[~] Assuming (i) Firewall is disabled and/or, (ii) Malware is already installed.")
        time.sleep(1)
        print("[~] Now you will have access to the Substation Computer, and three logical devices ")
        time.sleep(1)
        print("[!] You will need to have sudo access to this computer for rest of the simulation. Enter your password in the \"Sudo\" xterm ")
        time.sleep(1)
        print("[i] Terminal \"h1\" represents the main Substation computer. Activate the Anomaly Detection System in substation computer by typing \"./ADS\"")
        time.sleep(1)
        print("[i] Terminal \"h3\" represents the victim device that has been infected. Activate the malware by typing \"./malware\" in either h1, h2, or h3. To have ADS and Malware in same computer, you will need to type \"xterm h1\" in the sudo terminal once again.")
        time.sleep(1)
        #os.system("sudo mn -x --mac --topo single,3 --switch ovsk")
        #subprocess.call(['xterm', '-e', 'mn -x --mac --topo single,3 --switch ovsk'], shell=True)
        #subprocess.check_output("sudo mn -x --mac --topo single,3 --switch ovsk", shell=True)
        subprocess.check_output("xterm -e sudo mn -x --mac --topo single,3 --switch ovsk", shell=True)
        #os.system("pingall")
        #attack("10.0.0.2")


def attack(victim):
    p=IP(dst=victim,id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
    ls(p)
    print "[~] Sending Packets in 0.3 second intervals for timeout of 4 sec"
    ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
    print "[i] Summary of answered & unanswered packets"
    ans.summary()
    unans.summary()
    print "[i] Source port flags in response"
    #for s,r in ans:
    # print r.sprintf("%TCP.sport% \t %TCP.flags%")
    ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))


def doTCPComm(data):
    ip=IP(src="10.0.0.1", dst="10.0.0.2")
    TCP_SYN=TCP(sport=1500, dport=80, flags="S", seq=100)
    TCP_SYNACK=sr1(ip/TCP_SYN)

    my_ack = TCP_SYNACK.seq + 1
    TCP_ACK=TCP(sport=1500, dport=80, flags="A", seq=101, ack=my_ack)
    send(ip/TCP_ACK)

    my_payload=data
    TCP_PUSH=TCP(sport=1500, dport=80, flags="PA", seq=102, ack=my_ack)
    try:
        send(ip/TCP_PUSH/my_payload)
    except:
        print("Sorry not working")


if __name__ == '__main__':
    v = 0
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    filename = arguments['<model>']
    #filename = "".join([filename,".p"])

    #if options['--verbose']:
    #    v = 1

    os.system("clear")
    print(" - - - - - - - - - - - - - - - -")
    print(" - Canvass Power Flow - DEMO   -")
    print(" - - - - - - - - - - - - - - - -")




    #getInfo(data1)
    choice = arguments['<busnumber>'] #bus name is being called 'choice' for some reason.
    print("[!] This will launch a Denial of Service Attack on a bus breaker of %s" %choice)
    openWS = raw_input("[!] To monitor the packets and ports, you need Wireshark.\n[?] Do you want to open Wireshark? [PRESS 1 to CONFIRM, any other key to Quit] >>> ")
    if openWS == "1":
        print("[~] Opening Wireshark")
        try:
            if sys.platform == 'darwin':
                os.system("open -a wireshark")
            elif sys.platform == 'linux2':
                os.system("wireshark &")
                print("[!] Type 'bg' and hit enter to continue using Canvass in this session.")
        except:
            print("[E] Problem with launching Wireshark.\n[i] Please make sure that Wireshark is installed before you use this option again.\n[i] Quitting Canvass.")

    launchDOS(filename, choice)
