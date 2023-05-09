from pandas import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

df = read_csv("../EV-Data/clean_data.csv")

model_counts = df['Model'].value_counts()

multi_year_models = model_counts[model_counts > 1].index.tolist()

filtered = df[df['Model'].isin(multi_year_models)]

filtered.to_csv("multi_year_models.csv", index=False)