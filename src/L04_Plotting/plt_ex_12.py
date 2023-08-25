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


# twelfth trial - changing scales
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')
plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.legend()
plt.title('Cubic vs. Exponential')
