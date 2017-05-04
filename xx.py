from matplotlib.pyplot import figure, show
import numpy

fig = figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)


x = numpy.random.randn(20, 20)
#x[5] = 0.
#x[:, 12] = 0.

ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)


show()
