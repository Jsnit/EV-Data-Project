import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../EV-Data/clean_data.csv")

models = df['Model'].unique()

fig, ax = plt.subplots(figsize=(10, 6))
line_handles, line_labels = [], []
with open('slope_values.dat', 'w') as f:
    for model in models:
        model_data = df[df['Model'] == model]
        x = model_data['Model Year']
        y = model_data['Electric Range']
        
        model = LinearRegression()
        model.fit(x.values.reshape(-1, 1), y.values.reshape(-1, 1))
        y_pred = model.predict(x.values.reshape(-1, 1))
        
        ax.scatter(x, y)
        line, = ax.plot(x, y_pred)
        
        line_handles.append(line)
        line_labels.append(model_data.iloc[0]['Model'])
        
        f.write(f"{model_data.iloc[0]['Model']}: {model.coef_[0][0]}\n")
    
    ax.set_xlabel("Model Year")
    ax.set_ylabel("Electric Range")
    ax.set_title("Electric Range vs Model Year by Car Model")
    
    ax.legend(handles=line_handles, labels=line_labels)
    
    fig.savefig("electric_range_vs_model_year_by_car_model.png")
    
plt.show()