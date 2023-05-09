import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../EV-Data/clean_data.csv")

HighRangedf = df[df['Electric Range'] >= 170]

HighRangedf = HighRangedf[~((HighRangedf['Model'] == 'MODEL S') & (HighRangedf['Model Year'] == 2012))]

ShortRangedf = df[df['Electric Range'] < 170]

longgrouped_df = HighRangedf.groupby('Model')

shortGrouped_df = ShortRangedf.groupby('Model')

for name, group in longgrouped_df:
    plt.scatter(group['Model Year'], group['Electric Range'], label=name)

plt.title('Electric Range >= 170 vs. Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')

plt.legend()
plt.show()

for name, group in shortGrouped_df:
    plt.scatter(group['Model Year'], group['Electric Range'], label=name)

plt.title('Electric Range < 170 vs. Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')

plt.legend()
plt.show()
