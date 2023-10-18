import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question 1 plots
# a) --------------------------------------------------
# # caliper readings
q1df = pd.read_csv(r"Lab 3\matplotlib\Q1a.csv")
caliper = q1df['caliper']
voltages = q1df['voltage']

# linear fit
coeff = np.polyfit(voltages, caliper, 1)
poly = np.poly1d(coeff)

# plot caliper readings
plt.figure(1)
plt.plot(voltages, caliper, 'ko', label='Experimental Data', markersize=6, markerfacecolor='none')
plt.plot(voltages, poly(voltages), 'k--', label='Linear Fit')
plt.text(0.5, 20, '$x$ = ' + str(round(coeff[0], 2)) + '$V$ + ' + str(round(coeff[1], 2)))
plt.xlabel(r'$V$, Transducer Voltage (V)')
plt.ylabel(r'$x$, Caliper Displacement (mm)')
plt.legend(loc='upper left')

# save
plt.savefig(r"Lab 3\matplotlib\Q1a.png", dpi=300)

# b) --------------------------------------------------
q1deviation = pd.read_csv(r"Lab 3\matplotlib\q1deviation.csv")
caliper = q1deviation['caliper']
deviation = q1deviation['deviation']

# linear fit
coeff = np.polyfit(caliper, deviation, 1)
poly = np.poly1d(coeff)

# plot caliper readings
plt.figure(2)
plt.plot(caliper, deviation, 'ko', label='Experimental Data', markersize=6, markerfacecolor='none')
plt.plot(caliper, poly(caliper), 'k--', label='Linear Fit')
plt.text(0.5, -0.1, '$\Delta V$ = ' + str(round(coeff[0], 7)) + '$x$ + ' + str(round(coeff[1], 4)))
plt.xlabel(r'$x$, Caliper Displacement (mm)')
plt.ylabel(r'$\Delta x$, Displacement Deviation (mm)')
plt.legend(loc='lower right')

# save
plt.savefig(r"Lab 3\matplotlib\Q1b.png", dpi=300)

# c) --------------------------------------------------
q1c = pd.read_csv(r"Lab 3\matplotlib\q1c.csv")
time = q1c['time']
displacement = q1c['displacement']
center_diff = q1c['center diff']

plt.figure(3)
plt.plot(time, displacement, 'ko', label='Displacement', markersize=6, markerfacecolor='none')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$x$, Displacement (mm)')
plt.legend(loc='upper right')

plt.savefig(r"Lab 3\matplotlib\Q1cDisplacement.png", dpi=300)

plt.figure(4)
plt.plot(time, center_diff, 'ko', label='Velocity', markersize=6, markerfacecolor='none')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$\dot{x}$, Center Difference Velocity (mm/s)')
plt.legend(loc='upper left')
plt.savefig(r"Lab 3\matplotlib\Q1cVelocity.png", dpi=300)

#plt.show()