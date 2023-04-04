from pandas import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = read_csv("../EV-Data/Electric_Vehicle_Population_Data.csv")
#delete rows that are not from washigton
df[df['State'] == 'WA']

#convert to lict of dicts
dict_rows = df.to_dict('records')

# empty list for filtered dictionaries
filted_Dicts = []

# Filter out rows of hybrid vehicles
for row in dict_rows:
    if (row['Electric Vehicle Type']) == 'Battery Electric Vehicle (BEV)':
        filted_Dicts.append(row)

filtered = []

# Filter out models made after 2020
for row in filted_Dicts:
    if int(row['Model Year']) < 2020:
        filtered.append(row)

filtered_Dicts = []

# filter out rows with Electric Range < 0
for row in filtered:
    if int(row['Electric Range']) > 0:
        filtered_Dicts.append(row)

# plot the data

x = np.array([float(d['Model Year']) for d in filtered_Dicts])
y = np.array([float(d['Electric Range']) for d in filtered_Dicts])

plt.scatter(x, y, label='Data')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')

# gaussian function to fit
def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# perform the curve fit
popt, pcov = curve_fit(gaussian, x, y, p0=[1, np.mean(x), np.std(x)])

# generate a curve fit line
x_fit = np.linspace(min(x), max(x), 100)
y_fit = gaussian(x_fit, *popt)

plt.plot(x_fit, y_fit, 'r-', label='Curve fit')

plt.legend()
plt.show()