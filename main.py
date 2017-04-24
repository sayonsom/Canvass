from components.components import *
import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os
import argparse

parser = argparse.ArgumentParser(description='Please read the documentation on www.ailien.space/smartgrid/tool or email Sayon at sayon@ieee.org. To run an example, just type xxx at the command line')
parser.add_argument('-p', '--physical', help='This helps create only the physical grid')
parser.add_argument('-c', '--cyber', help='This helps create only the cyber network of the smart grid')
parser.add_argument('-cp', '--cyberphysical',help='This helps create a model of the cyber-physical network of the smart grid')

def main():

    args = parser.parse_args()
    if args.physical:
        newwd = input("[physical]\n-----------\nCreate a new  working directory:  ")
        comm1 = " ".join(("sh startup.sh", newwd))
        os.system(comm1)
        createPhysicalModel()
    elif args.cyberphysical:
        newwd = input("[cyber-physical]\n-------------\nCreate a new working directory:  ")
        comm1 = " ".join(("sh startup.sh", newwd))
        os.system(comm1)
        createCyberModel()
        createPhysicalModel()

    printHeader()
    runPowerFlow()


AllLoads = []
AllBuses = []
AllTransformers = []
AllLines = []
AllSwitches = []
AllCircuitBreakers = []
AllGenerators = []
AllShunts = []

loadsdf = pd.read_csv('loads.csv')
subdf = pd.read_csv('buses.csv')
transdf = pd.read_csv('transformers.csv')
linesdf = pd.read_csv('lines.csv')
switchesdf = pd.read_csv('switches.csv')
gendf = pd.read_csv('generators.csv')
shuntdf = pd.read_csv('shunt.csv')

f = open('pandafile.py', 'w')
f.write(
    'import pandapower as pp\nimport pandapower.networks\nnet = pp.create_empty_network()\n\n')





def createBusObjects(name, desc, node, vLevel, typ):
    substationObject = Substation.Bus(name, desc, node, vLevel, typ)
    AllBuses.append(substationObject)
    stringToWrite = name + " = pp.create_bus(net, name = \"" + str(desc).strip() + "\", vn_kv = " + str(vLevel) + ", type = \""+str(typ).strip()+"\")\n"
    f.write(stringToWrite)
    return substationObject

def createTransformerObjects(name, node, desc, hvBus, lvBus, typ):
    stringToWrite = name + " = pp.create_transformer(net, "+ str(hvBus) + "," + str(lvBus) + ", name =" + str(desc) + ", std_type= " + str(typ).strip() + ")\n"
    f.write(stringToWrite)
    return 0 #transformerObject


def createLineObjects(name, conductor, fromBus, toBus, length):
    stringToWrite = name + " = pp.create_line(net, " + str(fromBus) + "," + str(toBus) + ", length_km = " + str(length) + ", std_type = \"" + str(conductor) + "\")\n"
    f.write(stringToWrite)
    return 0

def createSwitchObjects(name, fromComp, toComp, ET, typ, Status):
    stringToWrite = name + " = pp.create_switch(net, " + str(fromComp) + "," + str(toComp) + ", et = \"" + str(ET).strip() + "\", type = \"" + str(typ).strip() + "\", closed = " + str(Status) + ")\n"
    f.write(stringToWrite)
    return 0

def createStaticGeneratorObjects(name, GenBus, pkw, qkvar):
    stringToWrite = "pp.create_sgen(net, " + str(GenBus) + ", p_kw = " + str(pkw) + ", q_kvar = " + str(qkvar) + ", name = \"" + str(name).strip() + "\")\n"
    f.write(stringToWrite)
    return 0

def createVCGeneratorObjects(name, GenBus, pkw, qkvar,qkvarmin, vmpu):
    stringToWrite = "pp.create_gen(net, " + str(GenBus) + ", p_kw = " + str(pkw) + ", max_q_kvar = " + str(qkvar) + ", min_q_kvar = " + str(qkvarmin) + ", vm_pu = " + str(vmpu) + ", name = \"" + str(name).strip() + "\")\n"
    f.write(stringToWrite)
    return 0

'''def createShuntObjects(name, ShuntBus, toBus, :
    stringToWrite = "pp.create_shunt(net, " + str(ShuntBus) + "," + str(toBus) + ", q_kvar= " + str(length) + ", p_kw = " + str(conductor) + ", name = \"" + str(name) +"\")\n"
    f.write(stringToWrite)
    return 0'''

def createLoadObjects(name, LoadBus, pkw, qkvar, scaling):
    stringToWrite = "pp.create_load(net, " + str(LoadBus) + ", p_kw=" + str(pkw) + ", q_kvar=" + str(qkvar) + ", scaling=" + str(scaling) + ", name = \"" + str(name).strip() + "\")\n"
    f.write(stringToWrite)
    return 0


def createNetwork():
    return 0

def createPhysicalModel():

    '''
    This function is used to create the physical model of the network
    '''

    printHeader()

    print("To run the entire cyber system model")

    extbus =      raw_input('External (Slack) Bus of the Grid              : ')
    extbusvpu =   raw_input('Voltage at External/Slack Bus                 : ')
    extbusshift = raw_input('Voltage Angle (Degrees) of External Grid Bus  : ')


    f.write("\n#Network Buses (Note: A substation can have multiple buses)\n\n")

    for i in range(len(subdf)):
        createBusObjects(subdf.iloc[i]['Name'], subdf.iloc[i]['Description'],subdf.iloc[i]['Node'], subdf.iloc[i]['Voltage'], subdf.iloc[i]['Type'])

    f.write("\n#Adding Transformers to the Network\n\n")

    for i in range(len(transdf)):
        createTransformerObjects(transdf.iloc[i]['Name'], transdf.iloc[i]['Node'], transdf.iloc[i]['Description'], transdf.iloc[i]['HVBus'], transdf.iloc[i]['LVBus'], transdf.iloc[i]['Type'])

    f.write("\n#Lines\n\n")

    for i in range(len(linesdf)):
        createLineObjects(linesdf.iloc[i]['Name'], linesdf.iloc[i]['ConductorType'], linesdf.iloc[i]['FromBus'], linesdf.iloc[i]['ToBus'], linesdf.iloc[i]['Length(km)'])

    f.write("\n#Switches\n\n")

    for i in range(len(switchesdf)):
        createSwitchObjects(switchesdf.iloc[i]['Name'], switchesdf.iloc[i]['FromComponent'], switchesdf.iloc[i]['ToComponent'], switchesdf.iloc[i]['ET'], switchesdf.iloc[i]['Type'], switchesdf.iloc[i]['Status'])

    f.write("\n#Generators\n\n")

    for i in range(len(gendf)):
        if gendf.iloc[i]['Type'] == "Static":
            createStaticGeneratorObjects(gendf.iloc[i]['Name'], gendf.iloc[i]['GenBus'], gendf.iloc[i]['P(kW)'], gendf.iloc[i]['Q(kVar)'])
        else:
            createVCGeneratorObjects(gendf.iloc[i]['Name'], gendf.iloc[i]['GenBus'], gendf.iloc[i]['P(kW)'], gendf.iloc[i]['Q(kVar)'], gendf.iloc[i]['Q(kVar)Min'],gendf.iloc[i]['vm_pu'])

    f.write("\n#Shunts\n\n")

    #for i in range(len(shuntdf)):
        #print "Shunts Not Printing For a while"
        #createShuntObjects(shuntdf.iloc[i]['Name'], shuntdf.iloc[i]['ShuntBus'], shuntdf.iloc[i]['P(kW)'],shuntdf.iloc[i]['Q(kVar)'])

    f.write("\n#Loads\n\n")

    for i in range(len(loadsdf)):
        createLoadObjects(loadsdf.iloc[i]['Name'],loadsdf.iloc[i]['LoadBus'], loadsdf.iloc[i]['P(kW)'], loadsdf.iloc[i]['Q(kVAR)'], loadsdf.iloc[i]['Scaling'])

    f.write("pp.create_ext_grid(net," + str(extbus) + ", vm_pu = " + str(extbusvpu).strip() + ", va_degree="+str(extbusshift)+")\n")

    return 0

def runPowerFlow():
    f.write("pp.runpp(net)")
    f.write("\nprint \"Power Flow Results At The Buses\"")
    f.write("\nprint \"-------------------------------\"")
    f.write("\nprint net.res_bus")
    f.close()
    os.system("python pandafile.py")

def createCyberModel():

    '''
    This function is used to create the cyber of the substation.
    '''
    g = open('cyberfile.py', 'w')
    g.write("#!/usr/bin/python\n\nfrom mininet.topo import Topo\nfrom mininet.net import Mininet\nfrom mininet.util import dumpNodeConnections\nfrom mininet.log import setLogLevel\n\n")

def printHeader():
    os.system("clear")
    print("\n|---------------------------------------------------------------------------------|")
    print("|     W S U   C Y B E R P H Y S I C A L   P O W E R  S Y S T E M   T O O L        |")
    print("|---------------------------------------------------------------------------------|")
    print("|Version: 0.0.1              Author: Sayonsom Chanda       Update: April 4, 2017 |")
    print("|---------------------------------------------------------------------------------|")




if __name__ == "__main__":
    """
    Entry point of the program
    """
    main()
