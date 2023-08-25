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


# tenth trial
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.plot(mySamples, myQuadratic, 'r', label='quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=4.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=5.0)
plt.legend()
plt.title('Cubic vs. Exponential')
