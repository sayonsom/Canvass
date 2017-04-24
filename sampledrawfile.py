import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import random

plt.axis([0, 24, 0.94, 1.06])
plt.ion
x = np.linspace(0,24,1440)
y = []
for i in range(1440):
    y.append(random.uniform(0.96,1.02))

#y_load =
#y_gen =
#y_brkr =

plt.plot(x,y)
plt.show()
