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
from mininet.log import setLogLevel
from mininet.link import TCLink


class bus2Topo(Topo):

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

		self.addLink(s1,h1,bw=14, delay='0ms', loss= 0, use_htb=True)
		self.addLink(s1,h2,bw=20, delay='5ms', loss= 0, use_htb=True)
		self.addLink(s1,h3,bw=20, delay='1ms', loss= 0, use_htb=True)
		self.addLink(h2,h3,bw=48, delay='1ms', loss= 0, use_htb=True)


topos = { 'bus2topo': ( lambda: bus2Topo() )}
