"""Usage: readfile.py <filename>

Options:
    -o  open this file
"""


import docopt
import time, sys

def insertBlanks():
    f.write("\n\n")

def loading(name):
    print "Building Mininet Cyber-Models for --> " +name+ " <--"
    for i in range(0, 100):
        time.sleep(0.01)
        width = (i + 1) / 3
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print

def createNewFile(name,i):

    datafile = open(filename, 'r')
    try:
        for line in datafile.readlines()[i:]:
            try:
                columns = line.split("| ")
                name=columns[0]
                loading(name)
                f=open("".join((name,"Topo.py")), 'w')
                f.write("#!/usr/bin/python\n\n\"\"\"\nCustom Smart Substation Communication Topology\n----------------------------------\nModel built using Sayon (a MIT License Software).\n----------------------------------\nW A R N I N G:\n----------------------------------\n--> Please make sure you know Mininet Python API very well before editing this file.\n--> Read Mininet Python API Documentation Here: http://mininet.org/walkthrough/#custom-topologies\n--> This program may not work properly if this file gets messed up.\n--> To troubleshoot, ask questions on StackOverflow with tags \"sayon\" and/or \"mininet\",\n--> 24x7 Email Support: <support@ailien.space> or, <sayon@ieee.org>\n\"\"\"\n\n\nfrom mininet.topo import Topo\nfrom mininet.net import Mininet\nfrom mininet.util import dumpNodeConnections\nfrom mininet.log import setLogLevel\nfrom mininet.link import TCLink\n\n\n")
                #insertBlanks()
                #print i
                f.write("class "+name+"Topo(Topo):\n\n\tdef __init__(self):\n")

                #i=i+1


                switches = columns[3]
                print switches
                switchlist = switches.split(",")
                f.write("\n\n\t\t#initializing topology\n\t\tTopo.__init__(self, link=TCLink)\n\n\t\t#Add Switches\n")
                for i in range(len(switchlist)):
                    f.write("\t\t"+switchlist[i]+" = " +"self.addSwitch(\'" +switchlist[i]+"\')\n")
                hosts = columns[5]
                addresses = columns[6]
                hostlist = hosts.split(",")
                f.write("\n\t\t#Add Hosts\n")
                for i in range(len(hostlist)):
                    f.write("\t\t"+hostlist[i]+" = " +"self.addHost(\'" +hostlist[i]+"\')\n")
                links = columns[7]
                delays = columns[8]
                bandwidths = columns[9]
                loss=columns[10]
                maxQueueSize=columns[11]
                linkLists = links.split(") ")
                bwlists = bandwidths.split(",")
                losslists = loss.split(",")
                delaylist = delays.split(",")
                queuelist = maxQueueSize.split(",")
                f.write("\n\n\t\t#Adding Links and Their properties\n\n")
                for i in range(len(linkLists)-1):
                    f.write("\t\tself.addLink"+linkLists[i]+",bw=" +bwlists[i]+", delay=\'" +delaylist[i]+"\', loss= " +losslists[i]+ ", use_htb=True)\n")

                f.write("\n\n")
                f.write("topos = { \'" +name+ "topo\': ( lambda: "+name+"Topo() )}\n")
                f.close()
            except:
                continue
    finally:
        f.close()


def readInputData(filename):
    i=1
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i:]:

        columns = line.split("| ")
        createNewFile(str(columns[0].strip()),i)
        break









def createCyberModel():
    '''
    This function is used to create the cyber of the substation.
    '''
    g = open("".join((inputfilename,".py")), 'w')
    g.write("#!/usr/bin/python\n\nfrom mininet.topo import Topo\nfrom mininet.net import Mininet\nfrom mininet.util import dumpNodeConnections\nfrom mininet.log import setLogLevel\n\n")

if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__)

        filename = arguments['<filename>']

    # Handle invalid options
    except docopt.DocoptExit as e:
        print e.message

    readInputData(filename)
