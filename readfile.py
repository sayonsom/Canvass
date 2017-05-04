"""Usage: readfile.py <filename>

Options:
    -o  open this file
"""


import docopt

f = open('ieee14panda-hello.py', 'w')
f.write(
    'import pandapower as pp\nimport pandapower.networks\nnet = pp.create_empty_network()\n\n')

def insertBlanks():
    f.write("\n\n")

def readInputData(filename):
    print("Working here")
    print(filename)
    datafile = open(filename, 'r')
    i = 0
    names = []


    for line in datafile.readlines():
        i +=1
        #print line
        if line.strip() == "~---Bus---~":
            #names.append(datafile.readlines()[i+1])
            readBusData(i)
        elif line.strip() == "~---Line---~":
            readLineData(i)
        elif line.strip() == "~---Substation---~":
            readSubData(i)
        elif line.strip() == "~---Transformer---~":
            readTrfData(i)
        elif line.strip() == "~---Shunt---~":
            readShuntData(i)
        elif line.strip() == "~---Generator---~":
            readGenData(i)
        elif line.strip() == "~---Switch---~":
            readSwitchData(i)
        elif line.strip() == "~---Load---~":
            readLoadData(i)

def readBusData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        if line.strip() == "~---NoMoreBus---~":
            datafile.close()
            insertBlanks()
            break
        columns = line.split(", ")
        #print columns
        #"Name","Description","Node","Voltage","Type"


        stringToWrite = str(columns[0].replace("*", "")) + " = pp.create_bus(net, name = \"" + str(columns[1]).strip() + "\", vn_kv = " + str(columns[3]).strip() + ", type = \""+ str(columns[4]).strip() +"\")\n"


        f.write(stringToWrite)

def writeForPowerFlow():
    f.write("pp.create_ext_grid(net, bus1, vm_pu = 1.02, va_degree=50)\n")
    f.write("pp.runpp(net)")
    f.write("\nprint (\"Canvass NR Power Flow Results At The Buses\")")
    f.write("\nprint (\"------------------------------------------\")")
    f.write("\nprint (net.res_bus)")
    #f.close()
    #os.system("python pandafile.py")



def readLineData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        if line.strip() == "~---NoMoreLine---~":
            datafile.close()
            insertBlanks()
            break
        columns = line.split(", ")

        #"Name","ConductorType","FromBus","ToBus","Length(km)"
        stringToWrite = str(columns[0]) + " = pp.create_line(net, " + str(columns[2]).strip() + "," + str(columns[3]).strip() + ", length_km = " + str(columns[4]).strip() + ", std_type = \"" + str(columns[1]).strip() + "\")\n"
        #print columns[0]
        f.write(stringToWrite)



def readSwitchData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split(", ")
        if line.strip() == "~---NoMoreSwitch---~":
            datafile.close()
            insertBlanks()
            break

        #"Name","FromComponent","ToComponent","ET","Type","Status"
        stringToWrite = str(columns[0]) + " = pp.create_switch(net, " + str(columns[1]).strip() + "," + str(columns[2]).strip() + ", et = \"" + str(columns[3]).strip() + "\", type = \"" + str(columns[4]).strip() + "\", closed = " + str(columns[5]).strip() + ")\n"
        #print columns[0]
        f.write(stringToWrite)

def readTrfData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split(", ")
        if line.strip() == "~---NoMoreTransformer---~":
            datafile.close()
            insertBlanks()
            break
        #"Name","Node","HVBus","LVBus","Description","HV","LV","Type"
        stringToWrite = str(columns[0]).strip() + " = pp.create_transformer(net, "+ str(columns[2]).strip() + "," +str(columns[3]).strip() + ", name =" + str(columns[4]).strip() + ", std_type= " + str(columns[7]).strip() + ")\n"
        #print columns[0]
        f.write(stringToWrite)

def readShuntData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split(", ")
        if line.strip() == "~---NoMoreShunt---~":
            datafile.close()
            insertBlanks()
            break
        #"Name","ShuntBus","P(kW)","Q(kVar)"
        stringToWrite = "pp.create_shunt(net, " + str(columns[1]).strip() + ", q_kvar= " + str(columns[3]).strip() + ", p_kw = " + str(columns[2]).strip() + ", name = \"" + str(columns[0]).strip() +"\")\n"
        #print columns[0]
        f.write(stringToWrite)

def readLoadData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split(", ")
        if line.strip() == "~---NoMoreLoad---~":
            writeForPowerFlow()
            datafile.close()
            insertBlanks()
            break
        #"Name","LoadBus","P(kW)","Q(kVAR)","Scaling"
        stringToWrite = "pp.create_load(net, " + str(columns[1]).strip() + ", p_kw=" + str(columns[2]).strip() + ", q_kvar=" + str(columns[3]).strip() + ", scaling=" + str(columns[4]).strip() + ", name = \"" + str(columns[0]).strip() + "\")\n"
        f.write(stringToWrite)

def readSubData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split()
        if line.strip() == "~---NoMoreSubstation---~":
            datafile.close()
            insertBlanks()
            break

def readGenData(i):
    datafile = open(filename, 'r')
    for line in datafile.readlines()[i+1:]:
        columns = line.split(", ")
        if line.strip() == "~---NoMoreGenerator---~":
            datafile.close()
            insertBlanks()
            break
        #"Name","Type","GenBus","P(kW)","Q(kVar)","Q(kVar)Min","vm_pu"
        if str(columns[1]).strip() == 'Generator':
            stringToWrite = "pp.create_gen(net, " + str(columns[2]).strip() + ", p_kw = " + str(columns[3]).strip() + ", max_q_kvar = " + str(columns[4]).strip() + ", min_q_kvar = " + str(columns[5]).strip() + ", vm_pu = " + str(columns[6]).strip() + ", name = \"" + str(columns[0]).strip() + "\")\n"
        else:
            stringToWrite = "pp.create_sgen(net, " + str(columns[2]).strip() + ", p_kw = " + str(columns[3]).strip() + ", q_kvar = " + str(columns[4]).strip() + ", name = \"" + str(columns[0]).strip() + "\")\n"

        f.write(stringToWrite)







if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__)

        filename = arguments['<filename>']

    # Handle invalid options
    except docopt.DocoptExit as e:
        print e.message

    readInputData(filename)
