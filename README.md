
# Car Price Estimation

This project was created to meet the needs of our client, a car dealer, who wanted an application that could estimate the price of a car.

## Objectives
As a data scientist, our mission is to:

- analyze and clean the dataset provided
- model the problem of car price estimation
- optimize the parameters of our model
- develop the application to make the model usable by the end user

## File organization

The project is organized into several directories:

*notebooks* : contains the different notebooks used for the various tasks of the project
- *car_price_cleaning.ipynb*: cleans the original dataset
- *car_price_analysis.ipynb*: analyzes the data, creates new features, transforms  the data, and generates a data visualization file (car_price_analysis.html)
- *car_price_prediction_models.ipynb*: builds and trains different car price estimation models, and exports the models in .joblib format

*csv*: contains the different CSV files used in the project:
- *car_price.csv*: original dataset provided by the client
- *car_price_clean.csv*: dataset cleaned by the car_price_cleaning.ipynb notebook
- *car_price_analyze.csv*: dataset updated by the various operations of the *car_price_analysis.ipynb* notebook and used in the prediction model

*models*: contains the final car price estimation model in .joblib format 

*car_price_app.py*: script of the web application created using the Streamlit framework, which allows the end user to estimate the price of a car based on its features.

## Requirements 
The required packages for running this project are listed in the requirements.txt file. To install these packages, run the following command in a terminal: `pip install -r requirements.txt`

## How to use the application ?
To use the web application, simply navigate to the streamlit directory and run the following command in a terminal: `streamlit run car_price_app.py`.  
This will launch the application in the default web browser. Simply enter the car's features to estimate its price.

