#!/usr/bin/python

"""Usage:
    pf.py <model> [--verbose]
    pf.py <model> getinfo [--verbose]
    pf.py <model> getinfoX [--verbose]
    pf.py <model> flipBusBreaker <busnumber> [--scada]
    pf.py <model> flipBusBreakerX <busnumber> [--scada]
    pf.py <model> changeLineStatus <linename>
    pf.py <model> runALoadProfile <profile>
    pf.py <model> changeTranformerStatus <trafoname>
Options:
    -h --help   This file is used to operate the power system model.
    --version   (c) Sayonsom Chanda, 2017. Canvass 0.0.1
                MIT License. Attribution required.
                Software provided AS IS. No WARRANTIES.
    --verbose   This prints out a very detailed log of whats going on.
                Helpful for debugging purposes.
    --scada     Write to a simulated SCADA server. Default configured to be
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
"""

#from __future__ import unicode_literals
import pprint
import pickle as pickle
import os
import numpy as np
import pandas as pd
from shutil import *
from docopt import docopt
import os
import pandapower as pp
import pandapower.networks as pn
import pandapower.plotting as plot
import matplotlib.pyplot as plt
import sys
import time



pd.options.mode.chained_assignment = None  # default='warn'


def recordData():
    pass



def runALoadProfile(data1, profile):
    """
    inputs an array of n values.
    modifies load values n times
    runs powerflow n times
    prints array for final output
    """
    profile = profile.split(',')
    profile = map(float, profile)
    iter = 0
    print "[i] This will make ', len(profile), 'changes to the power system model, and run power flow each time. It may take some time. Wait."

    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]]
    buses = data1["load"]["bus"].values
    #print (noBuses)
    #bus_p_kw = {}  #data1["load"]["p_kw"]
    X = []
    for i in profile:
        iter = iter + 1
        data1["load"]["p_kw"] = data1["load"]["p_kw"]*i
        pickle.dump(data1, open(filename, "wb"))
        print("[i] Physical Model of Smart Grid updated")
        y = open( filename, "rb" )
        data1 = pickle.load(y)
        newloads = printPFResults(filename, 0)
        #print("Outputs")
        #print(newloads.values[:,0])
        Z = np.array(newloads.values[:,0])
        Y = np.hstack((X,Z))
        X = Z
        #print Y


    #df = DataFrame(Y)
    #print df
    #i = 0
    #print Zvert
    #print len(Y)/(len(buses)+1)

    T = np.split(Y,len(Y)/len(buses))
    fig = plt.figure()
    plt.plot( np.arange(0,len(T[0]),1), T[0],'r--+',np.arange(0,len(T[1]),1), T[1],'g-.')
    fig.suptitle('Load Profile at All Buses')
    plt.xlabel('Bus Number (Indexes)')
    plt.ylabel('Real Power (kW)')
    plt.show()


def controllability():
    """
    When a cyber model is built, a sandbox config file is also built.
    It represents integrity of the system.
    """
    f = open('config.txt', 'r')
    good = f.readline().strip()
    f.close()
    #print good
    return good # if good = 1, system is not hackable.



def changeBusStatus(choice, data1, filename):
    """
    Modify the substation bus breaker status.
    """
    print("[!] Bus Breaker Status will be changed.")
    i = int(choice) - 1
    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]].values
    changeLoadServiceStatus(data1,loadInfo,choice, filename)


def getInfoX(data1, choice, fname, *args, **kwargs):
    """
    This function gets information about the model.
    It works with PIPES and subprocesses.
    """
    print("Here")

    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]]
    print (loadInfo)
    data = sys.stdin.readline()
    sys.stdout.write("[!] Physical Model is saying -- I am being hacked.\n")
    sys.stdout.flush()
    pass

def getInfo(data1, choice, fname, *args, **kwargs):
    """
    This function gets information about the model.
    """


    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]]
    print (loadInfo)
    #Ask to create cyber model
    #choice = int(choice)
    #changeLoadServiceStatus(data1,loadInfo,choice)
    pass

def printPFResults(fname,v):
    net = pp.from_pickle(fname)

    #print net
    pp.runpp(net)
    #print("\nBus Flows\n-----------------\n")
    busflow = net.res_bus
    #print (net.res_bus)
    #print("\nLine Flows\n----------------\n")
    lineflows = net.res_line
    #print (net.res_line)
    #print("\nLoad Measurements\n------------------\n")
    loadmeasures = net.res_load
    #print (net.res_load)
    #os.system("mkdir Output")
    f = open('Output/output.txt','w')
    net.res_load.to_csv(f,sep=' ', index=False, header=False)

    if v == 1:

        print("\nBus Flows\n-----------------\n")
        print (net.res_bus)
        print("\nLine Flows\n----------------\n")
        print (net.res_line)
        print("\nLoad Measurements\n------------------\n")
        print (net.res_load)


    return net.res_load
    #raw_input("Did you observe the change?")
    #os.system("echo -n \"[?] Repeat? > \"")
    #print net.line.index

def changeLoadServiceStatus(data1,loadInfo,choice, filename):
    """
    This function changes the load status from being connected to disconnected.
    """

    if loadInfo[int(choice)][3] == True:
        print("[!] State of Breaker at Bus %s is CLOSED. Changing state to OPEN. " %choice)
        data1["load"]["in_service"][int(choice)] = False

    elif loadInfo[int(choice)][3] == False:
        print("[!] State of Breaker at Bus %s is OPEN. Changing state to CLOSED. " %choice)
        data1["load"]["in_service"][int(choice)] = True

    modifyFile = raw_input("[?] Do you want to modify the file? [PRESS 1 to CONFIRM, any other key to Quit] >>> ")

    if modifyFile == "1":
        print("[~] Modifying the model to reflect changes ...")
        pickle.dump(data1, open(filename, "wb"))
        print("[i] Physical Model of Smart Grid updated")
        y = open( filename, "rb" )
        data1 = pickle.load(y)
        print(data1["load"][["bus","p_kw","q_kvar","in_service"]])

        #ask to run power flow
        runPF = raw_input("[?] Do you want to run power flow after new changes? [PRESS 1 to CONFIRM, any other key to Quit] >>> ")

        #if yes, create new model and run power Flow
        if runPF == "1":
            print("[~] Building Model ...")
            printPFResults(filename,1)

def printBanner():
    print(" - - - - - - - - - - - - - - - -")
    print(" - Canvass Power Flow - DEMO   -")
    print(" - - - - - - - - - - - - - - - -")


if __name__ == '__main__':
    v = 1
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    filename = arguments['<model>']
    filename = "".join([filename,".p"])

    if options['--verbose']:
       v = 1

    good = controllability()
    #print good
    if good != "1":
        #os.system("clear")
        printBanner()
        print("[!] Compromised system. Cannot continue without resetting config.txt file for your device")
        print("[i] Your Canvass session is terminated.")
        sys.exit()

    #print filename
    x = open(filename, "rb")
    data1 = pickle.load(x)



    print("[i] Physical Model File Opened")
    #getInfo(data1)
    choice = arguments['<busnumber>'] #bus name is being called 'choice' for some reason.

    if options['--scada']:
        print("SCADA connection is believed to exist.")
        # try:
        #     import OpenOPC
        #     opc = OpenOPC.open_client('localhost')
        #     print opc.servers()
        #     opc.connect('Matrikon.OPC.Simulation')
        #     print opc['Square Waves.Real8']
        #     opc.close()
        # except:
        #     print("Error in SCADA. Don't use this until SCADA is fixed.")

    if arguments['flipBusBreaker']:
        os.system("clear")
        printBanner()
        print("[~] Substation under focus is --> %s"%choice)
        print("[!] This action will change the status of bus breakers")
        changeBusStatus(choice, data1, filename)

    if arguments['runALoadProfile']:
        profile = options['<profile>']
        runALoadProfile(data1, profile)



    if arguments['flipBusBreakerX']:
        #print("[~] Substation under focus is --> %s"%choice)
        print("[!] This action will change the status of bus breakers")
        changeBusStatus(choice, data1, filename)

    elif arguments['getinfo']:
        os.system("clear")
        printBanner()
        print("[i] Getting Details about %s" %filename)
        getInfo(data1, choice, filename)

    elif arguments['getinfoX']:
        print("[i] Getting Details about %s" %filename)
        getInfo(data1, choice, filename)


    x.close()
