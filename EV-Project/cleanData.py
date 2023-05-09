from pandas import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

df = read_csv("../EV-Data/Edited-Electric_Vehicle_Population_Data.csv")

df[df['State'] == 'WA']

dict_rows = df.to_dict('records')

filted_Dicts = []

for row in dict_rows:
    if (row['Electric Vehicle Type']) == 'Battery Electric Vehicle (BEV)':
        filted_Dicts.append(row)

filtered = []

for row in filted_Dicts:
    if int(row['Model Year']) < 2020:
        filtered.append(row)

filtered_Dicts = []

count = 0
for row in filtered:
    if int(row['Electric Range']) > 0:
        count += 1
        filtered_Dicts.append(row)

filename = '../EV-Data/clean_data.csv'

with open(filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Model', 'Make', 'Electric Vehicle Type', 'Model Year', 'Electric Range'])
    for row in filtered_Dicts:
        writer.writerow([row['Model'], row['Make'], row['Electric Vehicle Type'], row['Model Year'], row['Electric Range']])
