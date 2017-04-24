import pandapower as pp
import pandapower.networks
net = pp.create_empty_network()

bus1 = pp.create_bus(net, name = "HV Busbar", vn_kv = 110, type = "b")
bus2 = pp.create_bus(net, name = "HV Busbar 2", vn_kv = 110, type = "b")
bus3 = pp.create_bus(net, name = "HV Transformer Bus", vn_kv = 110, type = "n")
bus4 = pp.create_bus(net, name = "MV Transformer Bus", vn_kv = 20, type = "n")
bus5 = pp.create_bus(net, name = "MV Main Bus", vn_kv = 20, type = "b")
bus6 = pp.create_bus(net, name = "MV Bus 1", vn_kv = 20, type = "b")
bus7 = pp.create_bus(net, name = "MV Bus 2", vn_kv = 20, type = "b")


line1 = pp.create_line(net, bus1,bus2, length_km = 10, std_type = "N2XS(FL)2Y 1x300 RM/35 64/110 kV")
line2 = pp.create_line(net, bus5,bus6, length_km = 2.0, std_type = "NA2XS2Y 1x240 RM/25 12/20 kV")
line3 = pp.create_line(net, bus6,bus7, length_km = 3.5, std_type = "48-AL1/8-ST1A 20.0")
line4 = pp.create_line(net, bus7,bus5, length_km = 2.5, std_type = "NA2XS2Y 1x240 RM/25 12/20 kV")


trafo1 = pp.create_transformer(net, bus3,bus4, name ="110kV/20kV transformer", std_type= "25 MVA 110/20 kV")


pp.create_shunt(net, bus3, q_kvar= -960, p_kw = 0, name = "Shunt")


pp.create_sgen(net, bus7, p_kw = -2000, q_kvar = 500, name = "static generator")
pp.create_gen(net, bus6, p_kw = -6000, max_q_kvar = 3000, min_q_kvar = -2000, vm_pu = 1.03, name = "generator")


sw1 = pp.create_switch(net, bus2,bus3, et = "b", type = "CB", closed = True)
sw2 = pp.create_switch(net, bus4,bus5, et = "b", type = "CB", closed = True)
sw3 = pp.create_switch(net, bus5,line2, et = "l", type = "LBS", closed = True)
sw4 = pp.create_switch(net, bus6,line2, et = "l", type = "LBS", closed = True)
sw5 = pp.create_switch(net, bus6,line3, et = "l", type = "LBS", closed = True)
sw6 = pp.create_switch(net, bus7,line3, et = "l", type = "LBS", closed = False)
sw7 = pp.create_switch(net, bus7,line4, et = "l", type = "LBS", closed = True)
sw8 = pp.create_switch(net, bus5,line4, et = "l", type = "LBS", closed = True)


pp.create_load(net, bus7, p_kw=2000, q_kvar=4000, scaling=0.6, name = "load")


