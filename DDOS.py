import sys
import os
from scapy.all import *
#conf.verb=0


f = open("config.txt","w+")
f.write("You are Hacked.")
f.close()


print "Field Values of packet sent"
p=IP(dst=sys.argv[1],id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
ls(p)
print "Sending Packets in 0.3 second intervals for timeout of 4 sec"
ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
print "Summary of answered & unanswered packets"
ans.summary()
unans.summary()
print "source port flags in response"
#for s,r in ans:
# print r.sprintf("%TCP.sport% \t %TCP.flags%")
ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))
