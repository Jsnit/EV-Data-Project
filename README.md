# EV-Data-Project
Modeling of Electric Vehicle Ownership Data in Washington State

This project is for Gonzaga Universities CPSC 222- Introduction to Data Science course. In this project Jake Snitily and Luke Sahlin are modeling electriv vehicle data in Washington State, with the intent to predict future data.

ppt for the project through presentation 1 to final product:
  https://docs.google.com/presentation/d/1jHYPYOee2PZutKMwLYdf8FO_ix_bWlbAmy465RthxqA/edit?usp=sharing

Technical Report:
  
  Our Project was created based of both our interest in electric vehicles and their evolution in Washigton. We both were interested in the mechanical evolution of their batteries and range systems leading us to research datasets related to electric vehicles in washington. We came across a dataset on Data.gov what seemed to be a reliable source with complete data that had a datasheet with the information of all the electric vehicles registered in washington state. the dataset format we chose to download was the csv format as it was the one we were most familiar with and had practiced with the most in python and c++. over the course of our project we have created 11 different tables or graphs. The data that we havve in our graph include VIN (1-10), County, City, State	Postal Code, Model Year, Make Model, Electric Vehicle Type,	Clean Alternative Fuel Vehicle (CAFV) Eligibility,	Electric Range,	Base MSRP,	Legislative District,	DOL Vehicle ID, Vehicle Location, Electric Utility, 2020 Census Tract. there was originally 114601 instances of this data in our dataset. With the process of evaluating this data we can predict the evolution of the range of electric vehicles and subsequently the growth of electric vehicles in washington as a whole.
 
 
    Include a brief description of the attributes
    What are you trying to classify in the dataset
    What are potential impacts of the results
    Who are stakeholders interested in your results

Data Analysis: Provide details about the dataset, data preparation, exploratory data analysis, and statistical analysis. More specifically:
What cleaning of the dataset did you need to perform (e.g.. are there missing values and how did you handle the missing values)
How are you merging the tables
What are challenges with data preparation
What data aggregation techniques are you applying
What visualizations informatively present the attributes and relationships
What statistical hypothesis tests are you computing
Make sure you set your null and alternative hypotheses up correctly. Please come see me if you have questions about how to do this

Our dataset was obtained from Data.gov (https://catalog.data.gov/dataset/electric-vehicle-population-data)
This dataset is riddled with errors, some of which include 97% empty values in the [Base MSRP], many empty values (0) in the [Electric Range], and most vehicles after 2020 having inaccurate/empty data.

To deal with these inconsistincies, initially we cleaned out our data in our individual projects, but that was very inefficient. We then decided to create a different set of files for our clean data, and this was made up of vehicles without any missing values excluding MSRP. 

Classification Results: Describe the classification approach you developed and its performance. More specifically:
What attribute are you using as class information (i.e., what attribute or attributes are you predicting)
What is the distribution of the class labels? (e.g. 50% yes, 50% no; or 70% weekday, 30% weekend, etc.)
What are your hypotheses about the predictions
How are you evaluating performance of your kNN and decision tree classifier? How do their results compare?
What are challenges with classification

Conclusion: Provide a brief conclusion of your project, including:
A short summary of the dataset you used
The classification approach you developed, your classifiers’ performance, and any ideas you have on ways to improve performance. 
Describe the potential impacts of your work (including ethical impacts) for the stakeholder’s you described in the introduction.
