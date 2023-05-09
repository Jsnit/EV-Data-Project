import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../EV-Data/clean_data.csv")

HighRangedf = df[df['Electric Range'] >= 170]

HighRangedf = HighRangedf[~((HighRangedf['Model'] == 'MODEL S') & (HighRangedf['Model Year'] == 2012))]

longgrouped_df = HighRangedf.groupby('Model')

for name, group in longgrouped_df:
    plt.scatter(group['Model Year'], group['Electric Range'], label=name)

plt.title('Upper Mile Group Scatter')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')
plt.legend()
plt.show()
