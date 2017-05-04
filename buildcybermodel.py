"""Usage:
    bcm.py <model> [--verbose]

Options:
    -h --help   This file is used to operate the power system model.
    --version   (c) Sayonsom Chanda, 2017. Canvass 0.0.1
                MIT License. Attribution required.
                Software provided AS IS. No WARRANTIES.
    --verbose   This prints out a very detailed log of whats going on.
                Helpful for debugging purposes.

"""


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
import sys
import time
import printbanner


if __name__ == '__main__':
    v = 1
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    filename = arguments['<model>']
    filename = "".join([filename,".p"])


        os.system("clear")
        printBanner()
        if v = 1:
            print("[1] Canvass can automatically generate substation communication models for you.")
            time.sleep(1)
            print("[2] A new folder will be created with the name \"{}\", where you will find a \"{}cyberfile.txt\" in Canvass format.")
            time.sleep(1)
            print("[3] For each substation, a Mininet communication file will be created which you can use to run simulations using Mininet VM in a Linux Environment.")
            time.sleep(1)
            buildCyberModel(filename,data1)
