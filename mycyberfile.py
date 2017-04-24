#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

bus1s1 = net.addSwitch('s1')
bus1h1 = net.addHost('h1')
bus1h2 = net.addHost('h2')
bus1h3 = net.addHost('h3')
bus1.addLink(s1,h1,bw=100, latency='10ms', loss= 0, use_htb=True)
bus1.addLink(s1,h2,bw=20, latency='5ms', loss= 0, use_htb=True)
bus1.addLink(s1,h3,bw=20, latency='14ms', loss= 0, use_htb=True)
bus1.addLink(h1,h4,bw=48, latency='11ms', loss= 0, use_htb=True)
