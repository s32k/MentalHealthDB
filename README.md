# MentalHealthDB

Data Management System for Counseling at Schools
Built as part of Borealis AI's 'Let's Solve It' program.

user_input.py (Shriya)

Main file: uses the deployed models from 'models'.
Takes user input for Population, Number of LTC Homes & Province of city.
Returns an estimate for Number of LTC Beds needed using Linear Regression.
datasets (Simi/Kevin)

Contains datasets for each Canadian province in CSV format.
maxmin.csv contains max & min values of relevant features for every provinces.
models (Shriya)

Contains a folder per province with 2 Multiple Linear Regression Models.
m1 returns the Number of Beds based on the current data.
m2 returns an adjustment to be added to the value above.
building_model.py contains the code used to build & save the said models.
visualizations (Theodora)

Contains visualizations for Ontario as sample.
models_visualized: 3D graphs created using matplotlib with plane of fit.
line_graphs: Line graphs (population vs Number of Beds/Homes etc.)
Accuracies.png: Box-plots for 5 provinces showing accuracy of models.
