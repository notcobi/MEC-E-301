import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Lab 7\matplotlib\hot_wire.csv')
x = df['pressure']
y = df['voltage']

plt.plot(x, y, 'ko', markersize=6, markerfacecolor='none')
# linear line
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, 'k--')
plt.xlabel('$P_v$, Dynamic pressure (mm$H_2$O)')
plt.ylabel('$V$, Anemometer voltage (V)')
plt.legend(['Data', 'Linear fit'])
plt.text(5, 8, f'$V = {m:.3f}P_v + {b:.3f}$')
plt.savefig(r'Lab 7\matplotlib\anemometer_calibration.png', dpi=300)

df_turbine = pd.read_csv(r'Lab 7\matplotlib\turbine.csv')
x_turbine = df_turbine['Q'] # m^3/s
y_turbine = df_turbine['turbine'] # hz
m_turbine, b_turbine = np.polyfit(x_turbine, y_turbine, 1)
plt.figure()
plt.plot(x_turbine, y_turbine, 'ko', markersize=6, markerfacecolor='none')
plt.plot(x_turbine, m_turbine*x_turbine + b_turbine, 'k--')
plt.xlabel('$Q$, Flow rate (m$^3$/s)')
plt.ylabel('$f$, Turbine frequency (Hz)')
plt.legend(['Data', 'Linear fit'])
plt.text(0.02, 200, f'$f = {m_turbine:.3f}Q + {b_turbine:.3f}$')
plt.savefig(r'Lab 7\matplotlib\turbine_calibration.png', dpi=300)

plt.show()