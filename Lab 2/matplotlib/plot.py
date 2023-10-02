import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_csv(r'Lab 2\matplotlib\02_Digital_Data_Collection_Tables.csv')

# Sort 10-bit data
df_10bit = df[['time 10', 'voltage 10']]

# Sort 5-bit data
df_5bit = df[['time 5', 'voltage 5']]

# Plot the data
plt.plot(df_10bit['time 10'], df_10bit['voltage 10'], '-o', label='10-bit', markersize=6, markerfacecolor='none')
plt.plot(df_5bit['time 5'], df_5bit['voltage 5'], '-s', label='5-bit', markersize=6, markerfacecolor='none')

# Set the title and labels
plt.xlabel(r'$t$, Time ($\mu$s)')
plt.ylabel(r'$V$, Voltage (V)')
plt.legend(loc='upper right')

# Set x-axis ticks to integer values with tick mark rotation
#plt.xticks(np.arange(df['n'].min(), df['n'].max()+1, 1), rotation=45, ha = 'left')
plt.xticks(rotation=-45, ha = 'left')

# Show the plot
plt.show()

# Save the plots
plt.savefig(r'Lab 2\matplotlib\plot.png', dpi=300)

