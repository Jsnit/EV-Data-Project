import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def logistic(x, a, b, c):
    return a / (1 + np.exp(-b * (x - c)))

df = pd.read_csv("../EV-Data/clean_data.csv")
HighRangedf = df[df['Electric Range'] < 170]
HighRangedf = HighRangedf[HighRangedf['Model Year'] > 2012]

x = HighRangedf['Model Year'].values.astype(float)
y = HighRangedf['Electric Range'].values.astype(float)

plt.scatter(x, y, label='Data')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')

popt, pcov = curve_fit(logistic, x, y, p0=[170, 1, 2015], maxfev=100000)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = logistic(x_fit, *popt)

plt.plot(x_fit, y_fit, 'r-', label='Curve fit')

plt.legend()
plt.show()
