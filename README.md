# EV-Data-Project
Modeling of Electric Vehicle Ownership Data in Washington State

This project is for Gonzaga Universities CPSC 222- Introduction to Data Science course. In this project Jake Snitily and Luke Sahlin are modeling electric vehicle data in Washington State, with the intent to predict future data.

Google Slides of our presentation's, First to Final product:
  https://docs.google.com/presentation/d/1jHYPYOee2PZutKMwLYdf8FO_ix_bWlbAmy465RthxqA/edit?usp=sharing

**Technical Report:**
  
  Our Project was created based of both our interest in electric vehicles and their evolution in Washigton. We both were interested in the mechanical evolution of their batteries and range systems leading us to research datasets related to electric vehicles in washington. We came across a dataset on Data.gov what seemed to be a reliable source with complete data that had a datasheet with the information of all the electric vehicles registered in washington state. the dataset format we chose to download was the csv format as it was the one we were most familiar with and had practiced with the most in python and c++. over the course of our project we have created 11 different tables or graphs. The data that we havve in our graph include VIN (1-10), County, City, State	Postal Code, Model Year, Make Model, Electric Vehicle Type,	Clean Alternative Fuel Vehicle (CAFV) Eligibility,	Electric Range,	Base MSRP,	Legislative District,	DOL Vehicle ID, Vehicle Location, Electric Utility, 2020 Census Tract. there was originally 114601 instances of this data in our dataset. With the process of evaluating this data we can predict the evolution of the range of electric vehicles and subsequently the growth of electric vehicles in washington as a whole.


Our dataset was obtained from Data.gov (https://catalog.data.gov/dataset/electric-vehicle-population-data)
This dataset is riddled with errors, some of which include 97% empty values in the [Base MSRP], many empty values (0) in the [Electric Range], and most vehicles after 2020 having inaccurate/empty data.

To deal with these inconsistincies, initially we cleaned out our data in our individual projects, but that was very inefficient. We then decided to create a different set of files for our clean data, and this was made up of vehicles without any missing values excluding MSRP. 

We used time aggregation, attempting to update our data as we went along, however the data we used never really improved over time, so we had to make due with what we got.

We made a series of Visualizations, but the most informative are the ones we concluded with: ExponentialFunctionFit.png (Group of High Range EV's, modeled used an exponential growth function), LowerGroupExponential.png (Group of Low Range EV's, modeled used an exponential growth function), electric_range_vs_model_year_by_car_model.png (Scatter Plot of every individual Car Model, and their average EV Range, with line of best fit between their instances)

Our statistical Hypothesis is that the EV Range of the aggregate of all EV Models will go up overtime

We utilized our datasets [Model Year], [Electric Range], [Model], and [Base MSRP]. We are predicting the changes in Electric Range based on the Model Year.

We hypothesize that our prediction has been proved so far, and with the addition of newer data in years to come, a comparison of our slopes for [Electric Range] rate of growth, and the new values will add aditional insight into our results.

Our dataset was very subpar, probably because it was free from a governemet website, this dataset included a range of factors that describe a vehicle from VIN number, to Model, to Electric Range. However this dataset was very incomplete and at times inaccurate.

We utilized Pandas, Matplotlib for our visualiztions, and sciKit for a variety of functions

Anyone interested in purchasing an EV will be interested in these results, as they show the quality of a technology increasing overtime, for the past ~10 years. 
