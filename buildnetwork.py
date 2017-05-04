"""Usage:
    buildnetwork.py <model> [--verbose]
    buildnetwork.py <model>
    buildnetwork.py <model>
    buildnetwork.py <model>

Options:
    -h --help   This file us used to generate commonly available power system models.
    --version   This is part of Canvass 0.1
    --verbose
"""


from shutil import *
from docopt import docopt
import os



def askToExecute(modelname):
    resp = "N"
    try:
        resp = raw_input('Model Built. Do you want to run a NR Power Flow Now? [Y/n]')
    except:
        print("No response received. Skipping Power Flow. Model still exists. ")

    if resp == "Y" or resp == "y":
        print("Cool!")
        os.system("python activemodel.py")

def writeRemainingStuff(f):
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.write("\n\n\n#Load Info -->\nloadInfo = net.load[[\"bus\",\"p_kw\",\"q_kvar\",\"in_service\"]].values")
    #f.write("#Line Info -->\nlineInfo = net.load[[\"bus","p_kw","q_kvar","in_service"]].values")
    #f.write("#Generator Info -->\ngenInfo = net.load[[\"bus","p_kw","q_kvar","in_service"]].values")
    #f.write("#Bus Info -->\nbusInfo = net.load[[\"bus","p_kw","q_kvar","in_service"]].values")
    #f.write("")
    f.close()



def build9bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case9()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    writeRemainingStuff(f)
    #askToExecute(str(f))

def build14bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case14()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))

def build30bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case30()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))

def build39bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case39()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))

def build57bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case57()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))

def build118bus():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.case118()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))

def buildBritainNetwork():
    f = open('activemodel.py', 'w')
    f.write('#Careful --> There are copyright holders. \nimport pandapower as pp\nimport pandapower.networks as pn\nnet = pn.GBnetwork()\n\n\npp.runpp(net)\n\nprint (\"Canvass NR Power Flow Results At The Buses\")')
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    f.close()
    askToExecute(str(f))


if __name__ == '__main__':
    v = 0
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    modelname = arguments['<model>']
    if options['--verbose']:
        v = 1

    if modelname == "9bus" or modelname == "ieee9bus" or modelname == "case9" or modelname == "wscc9bus":
        build9bus()
    elif modelname == "ieee14bus" or modelname == "14bus" or modelname == "case14":
        build14bus()
    elif modelname == "ieee30bus" or modelname == "30bus" or modelname == "case30":
        build30bus()
