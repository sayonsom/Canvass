#Careful --> There are copyright holders.
import pandapower as pp
import pandapower.networks as pn
net = pn.case9()


pp.runpp(net)

print ("Canvass NR Power Flow Results At The Buses")
print ("------------------------------------------")
print (net.res_bus)


#Load Info -->
loadInfo = net.load[["bus","p_kw","q_kvar","in_service"]].values
#print(loadInfo[0][3])
df = net.load[["bus","p_kw","q_kvar","in_service"]]
print df

net.load[["bus","p_kw","q_kvar","in_service"]].ix[2,'in_serice'] = False#.set_value('2', 'in_service', False)
df2 = net.load[["bus","p_kw","q_kvar","in_service"]]
print df2
pp.runpp(net)
print (net.res_bus)


#["load"]["in_service"][choice] = False
