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


# Question 2 plots
# a) --------------------------------------------------
q2a = pd.read_csv(r"Lab 3\matplotlib\Q2.csv")

caliper = q2a['caliper']
measurement = q2a['measurement']

x = measurement
y = caliper

# polynomial fit of degree 3
coeff = np.polyfit(x, y, 3)

# plot caliper readings
plt.figure(5)
plt.plot(x, y, 'ko', label='Experimental Data', markersize=6, markerfacecolor='none')
plt.plot(x, np.polyval(coeff, x), 'k--', label='Polynomial Fit')
plt.text(1.5, 0.25, '$x$ = ' + str(round(coeff[0], 2)) + '$V^3$ + ' + str(round(coeff[1], 2)) + '$V^2$ + ' + str(round(coeff[2], 2)) + '$V$ + ' + str(round(coeff[3], 2)))
plt.xlabel(r'$V$, Transducer Voltage (V)')
plt.ylabel(r'$x$, Caliper Displacement (mm)')
plt.legend(loc='upper right')

plt.savefig(r"Lab 3\matplotlib\Q2a.png", dpi=300)

# b) --------------------------------------------------
displacement = q2a['displacement']
x = y

plt.figure(6)
plt.plot(x, displacement, 'ko', label='Displacement', markersize=6, markerfacecolor='none')
plt.xlabel(r'$x$, Caliper Displacement (mm)')
plt.ylabel(r'$x_\mathrm{Hall}$, Hall Effect Displacement (mm)')
plt.legend(loc='upper left')

plt.savefig(r"Lab 3\matplotlib\Q2b.png", dpi=300)

# c) --------------------------------------------------
q2c = pd.read_csv(r"Lab 3\matplotlib\Q2.csv")

x = q2c['caliper']
y = q2c['measurement']

coeff = np.polyfit(x, y, 3)

plt.figure(7)
plt.plot(x, y, 'ko', label='Voltage', markersize=6, markerfacecolor='none')
plt.plot(x, np.polyval(coeff, x), 'k--', label='Polynomial Fit')
plt.text(1.25, 2.75, '$V$ = ' + str(round(coeff[0], 2)) + '$x^3$ + ' + str(round(coeff[1], 2)) + '$x^2$ + ' + str(round(coeff[2], 2)) + '$x$ + ' + str(round(coeff[3], 2)))
plt.xlabel(r'$x$, Caliper Displacement (mm)')
plt.ylabel(r'$V$, Transducer Voltage (V)')
plt.legend(loc='upper right')

plt.savefig(r"Lab 3\matplotlib\Q2c.png", dpi=300)

# Question 3 plots
# a) --------------------------------------------------
q3a = pd.read_csv(r"Lab 3\matplotlib\Q3.csv")

displacement = q3a['displacement']
large_acc = q3a['large acc']
small_acc = q3a['small acc']
large_rep = q3a['large rep']
small_rep = q3a['small rep']

plt.figure(8)
plt.plot(displacement, large_acc, '--ko', label='Large Accuracy', markersize=6, markerfacecolor='none')
plt.plot(displacement, small_acc, '--k^', label='Small Accuracy', markersize=6, markerfacecolor='none')
plt.xlabel(r'$x$, Displacment (mm)')
plt.ylabel(r'$x_\mathrm{Sensor}$, Sensor Displacement (mm)')
plt.legend(loc='upper left')

plt.savefig(r"Lab 3\matplotlib\Q3acc.png", dpi=300)

plt.figure(9)
plt.plot(displacement, large_rep, '--ko', label='Large Repeatability', markersize=6, markerfacecolor='none')
plt.plot(displacement, small_rep, '--k^', label='Small Repeatability', markersize=6, markerfacecolor='none')
plt.xlabel(r'$x$, Displacment (mm)')
plt.ylabel(r'$x_\mathrm{Sensor}$, Sensor Displacement (mm)')
plt.legend(loc='upper left')

plt.savefig(r"Lab 3\matplotlib\Q3rep.png", dpi=300)

plt.show()