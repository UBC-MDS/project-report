# author: Austin Shih
# date: 2022-11-23

"""Takes clean dataset from clean.py and produce produce prediction scores from various ML models 

Usage: predictions.py --clean_data=<clean_data> --output_file=<output_file>

Options:
--clean_data=<clean_data>       Relative path of cleaned dataset 
--output_file=<output_file>     Relative path to output file directory
"""
# python predictions.py --clean_data=../data/clean/LLCP2015_cleaned.csv --output_file='../results'

# Imports 
from docopt import docopt
import os
import pandas as pd
import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    RandomizedSearchCV,
    cross_validate,
    train_test_split,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import (
    OneHotEncoder,  
    StandardScaler,
    OrdinalEncoder
)
from scipy.stats import loguniform, randint, uniform
from sklearn.metrics import f1_score, recall_score, accuracy_score

# docopt 
opt = docopt(__doc__)

def main(clean_data, output_file):
    # create result directory
    if os.path.exists(output_file) == False:
        print('Results directory does not exist, creating directory...')
        os.mkdir(output_file)
    else:
        print('Results directory exists')

    # read clean csv
    try:
        df = pd.read_csv(clean_data)        # df = pd.read_csv(../data/clean/LLCP2015_cleaned.csv)
        print("read dataset complete")
    except FileNotFoundError:
        print("Input csv file of train set does not exist.")
        os._exit()

    # change target to binary, 1 for diabetes, 0 for non-diabetes
    df['Diabetes_012'] = df['Diabetes_012'].replace([1.0], int(0))
    df['Diabetes_012'] = df['Diabetes_012'].replace([2.0], int(1))
    df['Diabetes_012'] = df['Diabetes_012'].replace([0.0], int(0))
    df_s = df.sample(1000, random_state=123 )       # take random sample of 1000 to train model

    # train test split, 20% test, 80% train
    train_df, test_df = train_test_split(df_s, test_size=0.2, random_state=123)
    # X_train, y_train, X_test, y_test
    X_train, X_test = train_df.drop(columns=['Diabetes_012']), test_df.drop(columns=['Diabetes_012'])
    y_train, y_test = train_df['Diabetes_012'], test_df['Diabetes_012']

    # Lists of feature names
    numeric_features = ['BMI', 'PhysHlth', 'GenHlth', 'Age', 'Education', 'Income', 'MentHlth']
    pass_features = train_df.drop(columns=(numeric_features + ['Diabetes_012']) ).columns.to_list()

    assert len(numeric_features + pass_features + ['Diabetes_012']) == len(train_df.columns.to_list()), 'feature list is wrong'

    # Create the column transformer
    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        ('passthrough', pass_features)
    )

    # create classifiers
    models = {
        "Dummy": DummyClassifier(),
        "Decision Tree": DecisionTreeClassifier(random_state=123),
        "KNN": KNeighborsClassifier(),
        "RBF SVM": SVC(class_weight='balanced', random_state=123),
        "Logistic Regression": LogisticRegression(class_weight='balanced', max_iter=1000, random_state=123)
    }

    # scoring metrics
    score_metrics = ['accuracy', 'recall', 'f1']

    # cross validation to narrow down the better models
    print("starting cross validation...")
    cross_val_res = {}
    def pipe(model):
        return make_pipeline(preprocessor, model)
    for model in models:
        cross_val_res[model] = pd.DataFrame(
            cross_validate(pipe(models[model]), X_train, y_train, cv = 5, n_jobs=-1, return_train_score=True, scoring=score_metrics)
            ).agg('mean').round(3)
    cross_val_res_df = pd.DataFrame(cross_val_res)      # Save validation scores in dataframe
    print("complete")

    # random search hyperparameter tuning SVM and Logistic Regression
    # recall will be prioritized in this model
    # models for tuning
    models_tune = {
        "RBF SVM": SVC(class_weight='balanced', random_state=123),
        "Logistic Regression": LogisticRegression(class_weight='balanced', max_iter=1000, random_state=123)
    }
    # hyperparameters to be tuned
    svc_param = {
        "svc__C": 10.0 ** np.arange(-20, 10),
        "svc__gamma": 10.0 ** np.arange(-20, 10)
    }
    log_param = {
        "logisticregression__C": loguniform(1e-3, 1e3),
    }
    hyper_param = {
        "RBF SVM": svc_param,
        "Logistic Regression": log_param
    }   
    # function to run preprocessor and model
    def pipe(model):
        return make_pipeline(preprocessor, model)
    # save best estimator to dictionary
    rs_results = {}
    print("starting hyperparameter optimization...")
    for model in models_tune:
        random_search = RandomizedSearchCV(
            pipe(models_tune[model]), param_distributions=hyper_param[model], n_jobs=-1, n_iter=100, cv=5, random_state=123, refit=True, scoring='recall')
        random_search.fit(X_train, y_train)
        rs_results[model] = random_search.best_params_
    print("complete")

    # add tuned models to results dataframe
    # tuned models with best hyperparameters
    best_models = {
        "RBF SVM Tune": SVC(class_weight='balanced', random_state=123, C=rs_results['RBF SVM']['svc__C'], gamma=rs_results['RBF SVM']['svc__gamma']),
        "Logistic Regression Tune": LogisticRegression(class_weight='balanced', max_iter=1000, random_state=123, C=rs_results['Logistic Regression']['logisticregression__C'])
    }
    for model in best_models:
        cross_val_res[model] = pd.DataFrame(
            cross_validate(pipe(best_models[model]), X_train, y_train, return_train_score=True, scoring=score_metrics)
        ).agg('mean').round(3)
    cross_val_res_df = pd.DataFrame(cross_val_res)

    # save cross validation results
    try:
        cross_val_res_df.to_csv(output_file + '/' + 'cross_val_results.csv')
        print("cross validation csv file generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))

    # use best model on test data
    # score on full dataset 
    final_results = {}
    print('fit predict best model to test data...')
    for model in best_models:
        pipe(best_models[model]).fit(X_train, y_train)
        prediction = pipe(best_models[model]).predict(X_test)
        f1 = f1_score(y_test, prediction)
        recall = recall_score(y_test, prediction)
        accuracy = accuracy_score(y_test, prediction)
        final_results[model] = pd.DataFrame([{
            'Accuracy Score': accuracy,
            'f1 Score': f1,
            'Recall Score': recall
        }]).round(3)
    final_test = pd.concat(final_results, axis=1)
    print('complete')

    # save final test results
    try:
        final_test.to_csv(output_file + '/' + 'final_test_results.csv')
        print("final test results csv file generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))

if __name__ == "__main__":
    main(opt["--clean_data"], opt["--output_file"])