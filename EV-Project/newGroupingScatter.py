import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../EV-Data/clean_data.csv")

grouped_df = df.groupby('Model')

for name, group in grouped_df:
    plt.scatter(group['Model Year'], group['Electric Range'], label=name)

plt.title('Electric Range vs. Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')

plt.legend()
plt.show()
