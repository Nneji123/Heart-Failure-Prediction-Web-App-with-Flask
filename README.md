# Heart Failure Predictor Web App
[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Framework](https://img.shields.io/badge/framework-Flask-brightgreen.svg?style=flat)](http://www.pygame.org/news.html)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)

## Problem Statement
Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide.
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

So in this project I tried to develop an accurate model that could predict if a patient would die of heart failure or not given the input features. 

## Preview
![heart](https://user-images.githubusercontent.com/101701760/170781804-609d05fc-5cbb-45da-ab4b-47268024c647.gif)



## Data
The data used was gotten from kaggle https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data.

## Algorithm Used
In this project I tested 6 different classification algorithms namely:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost
5. GradientBoostClassifier
6. SupportVectorClassifier
The final model used for the app was the Gradient Boost Classifier model which had an accuracy score of 0.833.


## Requirements
To run a demo do the following:
1. Clone the repository.
2. Install the requirements from the requirements.txt file:
```
pip install -r requirements.txt
```
3. Then from your command line run:
```
python app.py
```
Then you can view the site on your local server: http://127.0.0.1:5000/ 

## Deployment
The site can be deployed to heroku and can also be viewed here: https://heart-failure-predictors.herokuapp.com/
