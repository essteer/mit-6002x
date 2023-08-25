# import numpy as np
import pylab as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential


# sixth trial
plt.figure('lin')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')
