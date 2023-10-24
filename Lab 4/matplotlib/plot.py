import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m,):
    return m * x


# Question 3
# Read the data from the file
q3 = pd.read_csv('Lab 4\matplotlib\Q3.csv')
strain = q3['epsilon']
quarter = q3['quarter']
half = q3['half']
full = q3['full']

# convert strain to microstrain and voltage to microvolts
strain = strain * 1e6
quarter = quarter * 1e6
half = half * 1e6
full = full * 1e6

# Plot the data
plt.plot(strain, quarter, 'ko', label= 'Quarter Bridge', markersize=6, markerfacecolor='none')
plt.plot(strain, half, 'k^', label= 'Half Bridge', markersize=6, markerfacecolor='none')
plt.plot(strain, full, 'ks', label= 'Full Bridge', markersize=6, markerfacecolor='none')
plt.xlabel('$\epsilon$, Strain ($\mu$)')
plt.ylabel('$\Delta E_0$, Voltage ($\mu$V)')

# Linear fit for all three bridges. Force the y-intercept to be 0.
quarter_fit, _ = curve_fit(linear, strain, quarter)
half_fit, _ = curve_fit(linear, strain, half)
full_fit, _ = curve_fit(linear, strain, full)


# Plot the linear fit
plt.plot(strain, linear(strain, *quarter_fit), 'k-.', label='Quarter Bridge Fit')
plt.plot(strain, linear(strain, *half_fit), 'k--', label='Half Bridge Fit')
plt.plot(strain, linear(strain, *full_fit), 'k:', label='Full Bridge Fit')

# plt.plot(strain, np.polyval(quarter_fit, strain), 'k--', label='Quarter Bridge Fit')
# plt.plot(strain, np.polyval(half_fit, strain), 'k--', label='Half Bridge Fit')
# plt.plot(strain, np.polyval(full_fit, strain), 'k--', label='Full Bridge Fit')

# Show equation for linear fit
plt.text(50, 25, '$\Delta E_{0, q}$ = ' + str(round(quarter_fit[0], 2)) + '$\epsilon$')
plt.text(45, 250, '$\Delta E_{0, h}$ = ' + str(round(half_fit[0], 2)) + '$\epsilon$')
plt.text(35, 500, '$\Delta E_{0, f}$ = ' + str(round(full_fit[0], 2)) + '$\epsilon$')
plt.legend(loc='best')
plt.savefig(r"Lab 4\matplotlib\Q3.png", dpi=300)
plt.show()