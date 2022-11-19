# Predicting if a person has diabete or not

Contributors:  
- Flora Ouedraogo
- Austin Shih
- Roan Raina
- Mehdi Naji
-
## Goal: This project aims to build a model which will be able to predict if a patient has diabete or not given some information about his/her health indicators.

## Introduction

Diabete is a disease which affects many people around the world. This disease is the result of the lack of insulin in the body. Insulin is a hormone produced by your pancreas whose role is to regulate the amount of glucose in the blood. Blood sugar must be carefully regulated to ensure that the body functions properly. Too much blood sugar can damage some organs, like blood vessels and nerves. Our body also needs insulin in order to use sugar for energy. According to the International Diabetes Federation “In 2021, Approximately 537 million adults (20-79 years) are living with diabetes. The total number of people living with diabetes is projected to rise to 643 million by 2030 and 783 million by 2045”.
With these alarming figures, many experts claim that it is important to have a good  lifestyle, i.g. physical activity and good eating habits, in order to avoid this disease or avoid its complicated form. Can we really tell if a person is suffering from diabetes or not, given some health information about the person's lifestyle?

## Research Question 
The major research question which has been addressed in this project is to predict the probability of a person suffering from diabetes, according to some information about their health condition and lifestyle. Addressing the question faces several limitations. For example, we need to identify the minimum number of crucial factors that can lead to a sufficiently accurate prediction. Also, as the data set used in this project is not balanced, we need to take care of various metrics to make sure the prediction is sufficiently reliable. 



## Accessing the data
Please run the following command to automatically download the dataset used in this study


## The Data Set
The data set used in this project is the Diabetes Health Indicators Dataset, fot the year of 2015. This dataset is annually collected by the Center of Disease Control and Prevention (CDC), through the Behavioral Risk Factor Surbellance System (BRFSS), which is a health-related phone survey. This dataset can be accessed through the Kaggle and can be found [here](Diabetes Health Indicators Dataset | Kaggle)
There are three files in this dataset, each consist of 22 columns; one target and 21 features. The target variable has three classes:
* 0 : no diabetes or only during pregnancy,
* 1 : for prediabetes, 
* 2 : diabetes. 

The feature variables in this dataset includes: 

|Variabl | Type | Question | Values |
| -------|------|-----| -------|
|**HighBP** | binary | high BP? | 0 = no & 1 = yes |
|**HighChol** |binary | high cholesterol? | 0 = no & 1 = yes |
| **CholCheck**| binary| cholesterol check in 5 years?| 0 = no & 1 = yes |
|**BMI**| numeric| Body Mass Index | |
|**Smoker**| binary| smoked at least 100 cigarettes in your entire life?| 0 = no & 1 = yes |
|**Stroke** | binary| ever told you had a stroke?| 0 = no & 1 = yes|
|**HeartDiseaseofAttack**| binary| coronary heart disease(CHD) or myocardial infarction(MI)?| 0 = no & 1 = yes|
|**PhysActivity**| binary| physical activity in past 30 days - not including job?| 0 = no & 1 = yes|
|**Fruits**| binary| consume fruit 1 or more times per day?| 0 = no & 1 = yes|
|**Veggies**| binary| consume vegetables 1 or more times per day?| 0 = no & 1 = yes|
|**HvyAlcoholConsump**| binary| heavy drinker?| 0 = no & 1 = yes|
|**AnyHealthcare**| binary| any kind of heath care coverage?| 0 = no & 1 = yes|
|**NoDocbcCost**| binary| Was there a time in past 12 months, you needed to see a doctor but could not due to the cost?| 0 = no & 1 = yes|
|**GenHlth**|ordinal | your health scale? | 1 = excellent <br> 2 = very good <br> 3 = good <br> 4 = fair <br> 5 = poor|
|**MentHlth**| ordinal| how many days of poor mental health during last 30 days?| from 1 to 30|
|**PhysHlth**| ordinal| how many days of poor physical health during last 30 days?| from 1 to 30|
|**DiffWalk**| binary| do you have serious difficulty walking or climbing stairs?| 0 = no & 1 = yes|
|**Sex**| binary|| 0 = female & 1 = male|
|**Age**| ordinal|| 13-level age category|
|**Education**| ordinal|| 6-level education category|
|**Income**| ordinal| |8-level income category|


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
The data set which will be used in predicting if a patient has diabete or not is released  by the Centers for Disease Control and Prevention (CDC) . Details of this dataset can be found [here] (https://www.cdc.gov/brfss/annual_data/annual_2015.html).

## References
The diabete dataset Diabetes Health indicator dataset is publicly available for research. The details are described in [here] (https://www.cdc.gov/brfss/annual_data/annual_2015.html).

