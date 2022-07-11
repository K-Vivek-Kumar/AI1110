import numpy as np
import matplotlib
import matplotlib.pyplot as plt


x = np.linspace(-4,4,80)
c1 = np.zeros(40)
c2 = np.linspace(0,1,10)
c3 = np.ones(30)
c = np.concatenate([c1, c2, c3])
simlen = int(1e6)
err = []
randvar = np.loadtxt('uni.dat',dtype='double')
for i in range(0,80):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

plt.plot(x,err,'bo')
plt.plot(x,c)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation", "Analysis"])
plt.show()