import pandas as pd


df = pd.read_csv("../EV-Data/Edited-Electric_Vehicle_Population_Data.csv")


num_zeros = len(df[df["Base MSRP"] == 0])
num_nonzeros = len(df[df["Base MSRP"] != 0])

percent_zeros = (num_zeros / len(df)) * 100
percent_nonzeros = (num_nonzeros / len(df)) * 100

with open("msrp_percentages.dat", "w") as f:
    f.write("Percentage of zeros in the msrp column: {:.2f}%\n".format(percent_zeros))
    f.write("Percentage of non-zeros in the msrp column: {:.2f}%\n".format(percent_nonzeros))