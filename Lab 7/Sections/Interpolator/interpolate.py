# Find the K values by looking up the values in table
# if the values are not in the table, use linear interpolation

import numpy as np
import pandas as pd


def interpolate(x0, x, y):
    # x0: the value to be interpolated
    # x: the array of x values
    # y: the array of y values

    # Check if x0 is in x
    if x0 in x:
        return y[np.where(x == x0)[0][0]]
    else:
        # Find the two x values that x0 is between
        x1 = 0
        x2 = 0
        y1 = y[0]
        y2 = y[0]
        for i in range(len(x)):
            if x[i] < x0:
                x1 = x[i]
                y1 = y[i]

            elif x[i] > x0:
                x2 = x[i]
                y2 = y[i]
                break

        # Linear interpolation
        return y1 + (x0 - x1) * (y2 - y1) / (x2 - x1)


data = pd.read_csv(r"Lab 7\Sections\Interpolator\rotameter.csv")
orfice = data["Orifice"]

K = pd.read_csv(r"Lab 7\Sections\Interpolator\K.csv")
x = K["P"]
y = K["K"]

print(interpolate(orfice[0], x, y))

# use lambda function to find the K value
data["K"] = data["Orifice"].apply(lambda x0: interpolate(x0, x, y))

# save the data to a new csv file
data.to_csv(r"Lab 7\Sections\Interpolator\rotameter_K.csv", index=False)
