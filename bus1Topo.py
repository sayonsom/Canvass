#!/usr/bin/python

"""
Custom Smart Substation Communication Topology
----------------------------------
Model built using Sayon (a MIT License Software).
----------------------------------
W A R N I N G:
----------------------------------
--> Please make sure you know Mininet Python API very well before editing this file.
--> Read Mininet Python API Documentation Here: http://mininet.org/walkthrough/#custom-topologies
--> This program may not work properly if this file gets messed up.
--> To troubleshoot, ask questions on StackOverflow with tags "sayon" and/or "mininet",
--> 24x7 Email Support: <support@ailien.space> or, <sayon@ieee.org>
"""


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost
from mininet.log import setLogLevel, info
from mininet.link import TCLink


class bus1Topo(Topo):

	def __init__(self):


		#initializing topology
		Topo.__init__(self, link=TCLink)

		#Add Switches
		s1 = self.addSwitch('s1')

		#Add Hosts
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')


		#Adding Links and Their properties

		self.addLink(s1,h1,bw=400, delay='0ms', loss= 0, use_htb=True)
		self.addLink(s1,h2,bw=20, delay='5ms', loss= 2, use_htb=True)
		self.addLink(s1,h3,bw=20, delay='1ms', loss= 4, use_htb=True)
		self.addLink(h1,h3,bw=648, delay='1ms', loss= 0, use_htb=True)





def perfTest():
	topos = { 'bus1topo': ( lambda: bus1Topo() )}

if __name__ == '__main__':
    setLogLevel( 'info' )
    # Prevent test_simpleperf from failing due to packet loss
    perfTest()
