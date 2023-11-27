import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m,):
    return m * x


# Question 2
# plot the function y= 0.8*3.3/(2)*(x+1) +0.1*3.3
# % 2) See Page 6 of the data sheet. The output of the sensor depends on the supply 
# % voltage of the sensor. Plot the expected voltage output of your sensor as a 
# % function of pressure over the range of the sensor if the supply voltage is 3.3 V 
# % and if it is 5V. Put both lines on the same plot. [2 marks]. Calculate the 
# % sensitivity of the sensor for each supply voltage. [1 mark]
x = np.linspace(1, -1, 100)
y_33 = 0.8*3.3/(2)*(x+1) +0.1*3.3
y_5 = 0.8*5/(2)*(x+1) +0.1*5
plt.plot(x, y_33, 'k--', label='Supply Voltage = 3.3V')
plt.plot(x, y_5, 'k-.', label='Supply Voltage = 5V')
plt.xlabel('$P$, Applied Pressure (kPa)')
plt.ylabel('$V_{3.3}, V_{5.0}$, Output Voltage (V)')
plt.text(0, 1, '$V_{3.3} = 1.32*(P+1) + 0.33$')
plt.text(0, 4, '$V_{5.0} = 2*(P+1) + 0.5$')
plt.legend()

#save
plt.savefig(r'Lab 5/matplotlib/q2VoltageOutputPlot.png', dpi = 300)
