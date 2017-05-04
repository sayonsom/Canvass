# There are copyright holders. 
import pandapower as pp
import pandapower.networks as pn
net = pn.case9()


pp.runpp(net)

print ("Canvass NR Power Flow Results At The Buses")
print ("------------------------------------------")
print (net.res_bus)