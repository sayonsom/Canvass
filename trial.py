
import cPickle as pickle
import pprint

x = open("mv_oberrhein.p", "rb")
data1 = pickle.load(x)

pprint.pprint(data1)
