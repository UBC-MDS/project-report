# Predicting if a person has diabete or not

Contributors:  
- Flora Ouedraogo
- Austin Shih
- Roan Raina
- Mehdi Naji
## Goal: This project aims to build a model which will be able to predict if a patient has diabete or not given some information about his/her health indicators.

## Introduction

Diabete is a disease which affects many people around the world. This disease is the result of the lack of insulin in the body. Insulin is a hormone produced by your pancreas whose role is to regulate the amount of glucose in the blood. Blood sugar must be carefully regulated to ensure that the body functions properly. Too much blood sugar can damage some organs, like blood vessels and nerves. Our body also needs insulin in order to use sugar for energy. According to the International Diabetes Federation “In 2021, Approximately 537 million adults (20-79 years) are living with diabetes. The total number of people living with diabetes is projected to rise to 643 million by 2030 and 783 million by 2045”.
With these alarming figures, many experts claim that it is important to have a good  lifestyle, i.g. physical activity and good eating habits, in order to avoid this disease or avoid its complicated form. Can we really tell if a person is suffering from diabetes or not, given some health information about the person's lifestyle?

## Research Question 
Given a person's health indicators (BMI, smoker, physical activity), is he or she having diabete?

## Accessing the data

Please run the following command to automatically download the dataset used in this study

## The Data Set

The data set used in to predict diabete is called the Diabetes Health Indicators Dataset. This information in this dataset has been obtain through a survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services from the year 2015.  This dataset has been released by the Centers for Disease Control and Prevention (CDC) . Details of this dataset can be found [here.](https://www.cdc.gov/brfss/annual_data/annual_2015.html)
Each row in our dataset represents health indicators from every respondent. There are several observations and 22 features. The target variable Diabetes_012 has 3 classes. 0 is for no diabetes or only during pregnancy, 1 is for prediabetes, and 2 is for diabetes. There is class imbalance in this dataset. This dataset has 21 feature variables.

The folowing is a list of the features in this dataset:

HighBP; 
HighChol: Cholesterol level
CholCheck: When was cholesterol level
BMI: Body Mass Index
Smoker: Have you smoked at least 100 cigarettes in your entire life? 
Stroke: Had a stroke?
HearDiseaseofAttack: Coronary heart disease(CHD) or myocardial infarction(MI)?
PhysActivity: Physical activity in past 30 days - not including job?
Fruits: Consume fruit 1 or more times per day?
Veggies: Consume vegetables 1 or more times per day?
HvyAlcoholConsump: Heavy drinker?
AnyHealthcare: Any kind of heath care coverage?
NoDocbcCost: Was there a time in past 12 months, you needed to see a doctor but could not due to the cost?
GenHlth: Your health scale?
MentHlth: How many days of poor mental health during last 30 days?
PhysHlth: How many days of poor physical health during last 30 days?
DiffWalk: Do you have serious difficulty walking or climbing stairs?
Sex: gender 
Age: 13-level age category
Education:6-level education category
Income:8-level income category

## Project Plan

To answer the above project question, We start by conducting an exploratory data analysis(EDA) on the dataset. Through the EDA, we will be exploring the features more in details to help us make decisions like scaling cilumns or dropping some columns. The problem that we will be tackling in this study is a classification problem. Since it is a classification problem, the possible supervised learning techniques that we might end up exploring will include DecisionTree, Logistic Regression and SVC. After chosing the machine learning technique, we will do hyperparameter tuning to find the best parameter combinations. Since, we are trying to predict wether a person has diabete or not based on health indicators, it is important to analyze feature importance in order to find the feature which is crucial in determining if a person has a diabete or not.
After choosing our final model, we will re-fit the model on the entire training data set after preprocessing and evaluate its performance on the test data set. We will then look at overall accuracy and how our model classified the test data observations. We will use a confusion matrix to present the results of the classification of our model.

## EDA discussion



## Dependencies

Python:
-ipykernel
-matplotlib>=3.2.2
-scikit-learn>=1.1.3
-requests>=2.24.0
-graphviz
-python-graphviz
-eli5
-shap
-jinja2
-altair_saver
-selenium<4.3.0
-pandas<1.5
-imbalanced-learn
-pip
-lightgbm


## License 

This project ( diabete prediction) is  licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). If re-using/re-mixing please provide attribution and link to this webpage.
## References

The diabete dataset Diabetes Health indicator dataset is publicly available for research. The details are described [here.](https://www.cdc.gov/brfss/annual_data/annual_2015.html)
