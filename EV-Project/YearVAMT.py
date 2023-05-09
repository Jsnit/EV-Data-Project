import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("../EV-Data/clean_data.csv")
data = data1.to_dict('records')

#for row in range((len(data))):
    #if (row >= len(data)):
        #break
    #if data[row]['Electric Range'] <= 0:
        #del data[row]
    #if (data[row]['State'] != 'WA'):
       # del data[row]


modelYear = []
for i in range(len(data)):
    modelYear.append(data[i]['Model Year'])

make = []
for i in range(len(data)):
    make.append(data[i]['Make'])

model = []
for i in range(len(data)):
    model.append(data[i]['Model'])

evType = []
for i in range(len(data)):
    evType.append(data[i]['Electric Vehicle Type'])

batteryRange = []
for i in range(len(data)):
    batteryRange.append(data[i]['Electric Range'])

year1997 = modelYear.count(1997)
year1998 = modelYear.count(1998)
year1999 = modelYear.count(1999)
year2000 = modelYear.count(2000)
year2001 = modelYear.count(2001)
year2002 = modelYear.count(2002)
year2003 = modelYear.count(2003)
year2004 = modelYear.count(2004)
year2005 = modelYear.count(2005)
year2006 = modelYear.count(2006)
year2007 = modelYear.count(2007)
year2008 = modelYear.count(2008)
year2009 = modelYear.count(2009)
year2010 = modelYear.count(2010)
year2011 = modelYear.count(2011)
year2012 = modelYear.count(2012)
year2013 = modelYear.count(2013)
year2014 = modelYear.count(2014)
year2015 = modelYear.count(2015)
year2016 = modelYear.count(2016)
year2017 = modelYear.count(2017)
year2018 = modelYear.count(2018)
year2019 = modelYear.count(2019)
year2020 = modelYear.count(2020)
year2021 = modelYear.count(2021)
year2022 = modelYear.count(2022)
year2023 = modelYear.count(2022)

years = (1997, 2000, 2003, 2006, 2009, 2012, 2015, 2018, 2019)
amtPerYear = [year1997, year2000, year2003,year2006, year2009, year2012, year2015,year2018,year2019]
plt.plot(years, amtPerYear)

plt.xlabel('model-Year')

plt.ylabel('amt of model')

plt.title('Model Year vs Amt of years model sold in WA')

plt.show()

#total = 0
#for i in range(len(amtPerYear)):
#    total += amtPerYear[i]
#print(total)
