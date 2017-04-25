"""Usage:
    operate.py <model> flip <switchname> [--verbose]
    operate.py <model> flipbyip <switchIPAddress>
    operate.py <model> status <switchname>
    operate.py <model> statusbyip <switchIPAddress>


Options:
    -h --help   This file us used to operate the power system model.
    --version   This is part of Canvass 0.1
    --verbose   This prints out a very detailed log of whats going on.
                Helpful for debugging purposes.
"""


from shutil import *
from docopt import docopt
import os



def status(switch, v):
    f=open('ieee14bus.txt', 'r')
    if v == 1:
        print ("Checking switch status.")
        for line in f:
            if switch in line and "True" in line:
                print("%s is CLOSED." % switch)
            elif switch in line and "False" in line:
                print("%s is OPEN." % switch)
    f.close()

def flipSwitch(switch, fname, v):
    #save original model in "OriginalModel"
    if v == 1:
        print ("Creating a backup copy of your original model at ~/OriginalModel/",fname)

    if not os.path.exists("OriginalModel"):
        os.makedirs("OriginalModel")

    #create a copy of the model
    dst = "".join(("OriginalModel/",fname))
    copy(fname, dst)

    #get switch status
    status(switch,v)

    #create new model with altered switch status
    newfname = "activeModel.txt"#"".join(((os.path.splitext(fname)[0]),"-modified.txt"))


    #create a folder called "ActiveModels"
    if not os.path.exists("ActiveModel"):
        os.makedirs("ActiveModel")


    #save the modified file as the latest acitive model

    with open(fname, 'r') as input_file, open(newfname, 'w') as output_file:
        for line in input_file:
            if switch in line and "True" in line:
                line2 = line.replace("True","False")
                output_file.write(line2)
            elif switch in line and "False" in line:
                line2 = line.replace("False","True")
                output_file.write(line2)

            else:
                output_file.write(line)

    #Archive other active models
    dst = "".join(("ActiveModel/",newfname))
    copy(newfname, dst)
    os.remove(newfname)

    #Run a power flow simulation after flipping the switch
    if v == 1:
        print("1. Switch Status Flipped for ", switch)
        print("2. Creating Power Flow Model")

    os.system("python readfile.py ActiveModel/activeModel.txt")
    os.system("python activepowermodel.py")



if __name__ == '__main__':
    v = 0
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    options = docopt(__doc__, version='Canvass 0.0.1')
    filename = arguments['<model>']
    if options['--verbose']:
        v = 1



    #if arguments['flip']:
    #print("We will operate the following switching ->", arguments['<switchname>'])
    if arguments['flip']:
        flipSwitch(arguments['<switchname>'],filename,v)
    else:
        print("Not done")
