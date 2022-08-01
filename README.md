# MentalHealthDB

Data Management System for Counseling at Schools
Built as part of Senior Year Project for AISSCE Internals.

MainMenu.py
Main file: uses the deployed models from 'models'.
Takes user input for Population, Number of LTC Homes & Province of city.
Returns an estimate for Number of LTC Beds needed using Linear Regression.

AddDel.py
Contains datasets for each Canadian province in CSV format.
maxmin.csv contains max & min values of relevant features for every provinces.

SearchModifyMove.py
Contains a folder per province with 2 Multiple Linear Regression Models.
m1 returns the Number of Beds based on the current data.
m2 returns an adjustment to be added to the value above.
building_model.py contains the code used to build & save the said models.
