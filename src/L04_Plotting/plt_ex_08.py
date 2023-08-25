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


# eighth trial
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()
plt.title('Cubic vs. Exponential')
