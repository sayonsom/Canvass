"""Usage:
    readingpickle.py <model> [--verbose]
    readingpickle.py <model> getinfo [--verbose]
    readingpickle.py <model> flipbusbreaker <busnumber>
    readingpickle.py <model> changeLineStatus <linename>
    readingpickle.py <model> fliploadbreaker <linename>
    readingpickle.py <model> changeTranformerStatus <trafoname>
Options:
    -h --help   This file us used to operate the power system model.
    --version   This is part of Canvass 0.1
    --verbose   This prints out a very detailed log of whats going on.
                Helpful for debugging purposes.

"""


import pprint
import pickle as pickle
import os
import pandas as pd
from shutil import *
from docopt import docopt
import os
import pandapower as pp
import pandapower.networks as pn
import pandapower.plotting as plot


pd.options.mode.chained_assignment = None  # default='warn'


#create a copy of the model
def createBackUpCopy():
    pass

#dst = "".join(("Datafiles/OriginalModel/",fname))
#copy(fname, dst)

#x = open( "GBnetwork.p", "rb" )
#data1 = pickle.load(x)

#pprint.pprint(data1)
#os.system("clear")
#jj = data1["_is_elements"]["gen"].loc[:,"in_service"]
#busesInService = data1["_is_elements"]["bus"][["name","in_service"]]
#jj = data1#["bus"]
#jj[0] = 10
#jj["name"][0] = 99
#print(jj["name"][0])
#print jj

#loadInfo = []

def changegeneratorstatus(choice, data1):
    """
    Modify the substation bus breaker status.
    """
    print("Here Now")
    i = int(choice) - 1
    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]].values
    changeLoadServiceStatus(data1,loadInfo,choice)

def getInfo(data1, *args, **kwargs):
    """
    This function gets information about the model.
    """


    loadInfo = data1["load"][["bus","p_kw","q_kvar","in_service"]].values
    print (loadInfo[0][0])
    choice = 3
    changeLoadServiceStatus(data1,loadInfo,choice)
    pass

def printPFResults(fname):
    xyz = pp.from_pickle(fname)
    #print xyz
    pp.runpp(xyz)
    print("\nBus Flows\n-----------------\n")
    print (xyz.res_bus)
    print("\nLine Flows\n----------------\n")
    print (xyz.res_line)
    print("\nLoad Measurements\n------------------\n")
    #print xyz.res_load
    #print xyz.line.index

    # try:
    #     import seaborn
    #     colors = seaborn.color_palette()
    # except:
    #     colors = ["b", "g", "r", "c", "y"]

    #plot.fuse_geodata(xyz)
    #plot.simple_plot(xyz, bus_size=0.7)

    cmap_list=[(20, "green"), (50, "yellow"), (60, "red")]
    cmap, norm = plot.cmap_continous(cmap_list)

    plot.create_generic_coordinates(xyz, respect_switches=True)

    lc = plot.create_line_collection(xyz, xyz.line.index, zorder=1, cmap=cmap, norm=norm, linewidths=2)
    plot.draw_collections([lc], figsize=(8,6))

    # plot.create_generic_coordinates(xyz, respect_switches=True)
    # plot.fuse_geodata(xyz)
    # bc = plot.create_bus_collection(xyz, xyz.bus.index, size=.2, color=colors[0], zorder=10)
    # tc = plot.create_trafo_collection(xyz, xyz.trafo.index, color="g")
    # lcd = plot.create_line_collection(xyz, xyz.line.index, color="grey", linewidths=0.5, use_line_geodata=False)
    # sc = plot.create_bus_collection(xyz, xyz.ext_grid.bus.values, patch_type="rect", size=.5, color="y", zorder=11)
    # # plot.draw_collections([lcd, bc, tc, sc], figsize=(8,6))
    #
    # closed_lines = set(xyz.line.index) - set(xyz.switch[(xyz.switch.et=="l") & (xyz.switch.closed==False)].element.values)
    # lcd = plot.create_line_collection(xyz, closed_lines, color="grey", linewidths=0.5, use_line_geodata=False)
    # plot.draw_collections([lcd, bc, tc, sc], figsize=(8,6))

    #plot.show()

    # cmap_list=[((0.975, 0.985), "blue"), ((0.985, 1.0), "green"), ((1.0, 1.03), "red")]
    # cmap, norm = plot.cmap_discrete(cmap_list)
    # bc = plot.create_bus_collection(xyz, xyz.bus.index, size=80, zorder=2, cmap=cmap, norm=norm)

    #plot.simple_plot(xyz, bus_size=0.7)
    #plot.show()



def changeLoadServiceStatus(data1,loadInfo,choice):
    """
    This function changes the load status from being connected to disconnected.
    """

    if loadInfo[choice][3] == True:
        data1["load"]["in_service"][choice] = False

    elif loadInfo[choice][3] == False:
        data1["load"]["in_service"][choice] = True

    modifyFile = raw_input("Do you want to modify the file? [1 to CONFIRM] ")

    if modifyFile == "1":
        print("Modifying the model to reflect changes ...")
        pickle.dump(data1, open("GBnetwork.p", "wb"))
        y = open( "GBnetwork.p", "rb" )
        data1 = pickle.load(y)
        print(data1["load"][["bus","p_kw","q_kvar","in_service"]])

        #ask to run power flow
        runPF = raw_input("Do you want to run power flow after new changes? [1 to CONFIRM] ")

        #if yes, create new model and run power Flow
        if runPF == "1":
            print("Building Model ...")
            printPFResults("GBnetwork.p")

            #net = pn.GBnetwork()
            #jj = net.load[["bus","p_kw","q_kvar","in_service"]].values
            #print jj
            #net = pn.GBnetwork()
            #pp.runpp(net)
            #print xyz#net.res_bus


        #else leave






def changeLoadPValue():
    pass

def changeLoadQValue():
    pass

def makeModifiedModel():
    pass

#getInfo(x)
#getInfo(data1)
#pprint.pprint(data1)
#pickle.dump(data1, open("GBnetworkmod.p", "wb"))



#GBnetwork = pp.from_pickle("GBnetwork.p")
#net = pn.GBnetwork()

#pp.runpp(net)
#print net.res_bus


if __name__ == '__main__':
    v = 0
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    filename = arguments['<model>']

    #if options['--verbose']:
    #    v = 1
    os.system("clear")
    print(" - - - - - - - - - - - - - - - -")
    print(" - Canvass 0.0.1 DEMO Version  -")
    print(" - - - - - - - - - - - - - - - -")
    print filename
    x = open(filename, "rb")
    data1 = pickle.load(x)

    #getInfo(data1)
    choice = arguments['<busnumber>']
    print choice


    if arguments['flipbusbreaker']:
        print("This action will change the status of bus breakers")
        changegeneratorstatus(choice, data1)


    x.close()

    #function to get all data
    #getAllData(filename)
    #change service status of generator
    #change service status of line
    #change service status of transformer
