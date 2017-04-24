"""The loadflow command."""

from json import dumps
from .base import Base
#from components import *
import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os



class Loadflow(Base):
    """Welcome to Sayon: Easiest Smart Grid Tool."""

    def run(self):
        datafile = self.options["<datafile.txt>"][0]
        outputfile = self.options["<outputfile.txt>"][0]
        os.system("clear")
        printHeader()
        #x = Line("ddd","conductory", 1, 2, 3)
        #print x.conductor
        readInputData(datafile)
        createPhysicalModel()
        runPowerFlow()



loadsdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/loads.csv')
subdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/buses.csv')
transdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/transformers.csv')
linesdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/lines.csv')
switchesdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/switches.csv')
gendf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/generators.csv')
shuntdf = pd.read_csv('~/Dropbox/MyModules/SubstationProject/shunt.csv')

f = open('pandafile.py', 'w')
f.write(
    'import pandapower as pp\nimport pandapower.networks\nnet = pp.create_empty_network()\n\n')





def createBusObjects(name, desc, node, vLevel, typ):
    stringToWrite = name + " = pp.create_bus(net, name = \"" + str(desc).strip() + "\", vn_kv = " + str(vLevel) + ", type = \""+str(typ).strip()+"\")\n"
    f.write(stringToWrite)
    return 0

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
    f.write("\nprint(\"Power Flow Results At The Buses\")")
    f.write("\nprint(\"-------------------------------\")")
    f.write("\nprint(net.res_bus)")
    f.close()
    os.system("python pandafile.py")




def printHeader():
    os.system("clear")
    print("|---------------------------------------------------------------------------------|")
    print("|  S A Y O N   C Y B E R P H Y S I C A L   P O W E R  S Y S T E M   T O O L       |")
    print("|---------------------------------------------------------------------------------|")
    print("|Version: 0.0.2          Author: Sayonsom Chanda       Last Update: April 4, 2017 |")
    print("|---------------------------------------------------------------------------------|")
