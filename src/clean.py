# Author: Roan Raina
# Date: 18 Nov 2022
# Attribution: This code has been adapted from Alex Teboul's Diabetes Health Indicators Dataset Notebook 
#              located at https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook


"""Cleans the CDC (2015) BRFSS Survey Data and writes the output to a file (csv)
Usage: src/clean.py --in_file=<in_file> --out_file=<out_file>
Options:
--in_file=<in_file>      Path (including filename) to raw data (XPT file)
--out_file=<out_file>    Path to directory where the processed data should be written
"""

# Imports 
from docopt import docopt
import pandas as pd
import os

# docopt CLI stuff
opt = docopt(__doc__)

#
def main(in_file, out_file):
    
    ## Import Data
    df = pd.read_sas(in_file, format='xport')

    ## CLEANING

    # select relevant columns
    # identified as relevant to diabetes prediction by Alex Teboul
    relevant_columns = [
                        'DIABETE3',
                        '_RFHYPE5',  
                        'TOLDHI2',
                        '_CHOLCHK', 
                        '_BMI5', 
                        'SMOKE100', 
                        'CVDSTRK3',
                        '_MICHD', 
                        '_TOTINDA', 
                        '_FRTLT1',
                        '_VEGLT1', 
                        '_RFDRHV5', 
                        'HLTHPLN1',
                        'MEDCOST', 
                        'GENHLTH',
                        'MENTHLTH',
                        'PHYSHLTH',
                        'DIFFWALK', 
                        'SEX',
                        '_AGEG5YR',
                        'EDUCA',
                        'INCOME2' 
                        ]
    df = df[relevant_columns]

    # Drop rows with NA values
    df = df.dropna()

    # modifying values to make more sense 
    df = modify_clean_values(df)

    # rename columns for readability
    df = df.rename(columns = {  
                                'DIABETE3':'Diabetes_012', 
                                '_RFHYPE5':'HighBP',  
                                'TOLDHI2':'HighChol',
                                '_CHOLCHK':'CholCheck', 
                                '_BMI5':'BMI', 
                                'SMOKE100':'Smoker', 
                                'CVDSTRK3':'Stroke',
                                '_MICHD':'HeartDiseaseorAttack', 
                                '_TOTINDA':'PhysActivity', 
                                '_FRTLT1':'Fruits',
                                '_VEGLT1':"Veggies", 
                                '_RFDRHV5':'HvyAlcoholConsump', 
                                'HLTHPLN1':'AnyHealthcare',
                                'MEDCOST':'NoDocbcCost', 
                                'GENHLTH':'GenHlth',
                                'MENTHLTH':'MentHlth',
                                'PHYSHLTH':'PhysHlth',
                                'DIFFWALK':'DiffWalk', 
                                'SEX':'Sex',
                                '_AGEG5YR':'Age',
                                'EDUCA':'Education',
                                'INCOME2':'Income' 
                                }
                    )

    # save cleaned df as csv
    try:
        df.to_csv(out_file, index=False)
    except:
      os.makedirs(os.path.dirname(out_file))
      df.to_csv(out_file, index = False)


def modify_clean_values(df):
    # modifying values to make more sense 
    # based on https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf


    # DIABETE3 (Diabetes)
    # (Ever told) you have diabetes (some ordinality)
    # we see some ordinality in the data, hence we will map the responses per the following:
    # 1 (yes) --> 2 (yes)
    # 2 (yes, during pregnancy) --> 0 (no)
    # 3 (no) --> 0 (no)
    # 4 (no, prediabetes) --> 1 (prediabetes)
    # 7 (dont know) --> remove
    # 9 (refused) --> remove
    df['DIABETE3'] = df['DIABETE3'].replace({2:0, 3:0, 1:2, 4:1})
    df = df[df.DIABETE3 != 7]
    df = df[df.DIABETE3 != 9]

    # _RFHYPE5 (HighBP)
    # Adults who have been told they have high blood pressure by a doctor, nurse, or other health professiona
    # 1 (no) --> 0 (no)
    # 2 (yes) --> 1 (yes)
    # 9 (dont know) --> remove
    df['_RFHYPE5'] = df['_RFHYPE5'].replace({1:0, 2:1})
    df = df[df._RFHYPE5 != 9]

    # TOLDHI2 (HighChol)
    # Have you EVER been told by a doctor, nurse or other health professional that your blood cholesterol is high?
    # 1 (yes) --> 1 (yes)
    # 2 (no) --> 0 (no)
    # 7 (dont know) --> remove
    # 9 (refused) --> remove
    df['TOLDHI2'] = df['TOLDHI2'].replace({2:0})
    df = df[df.TOLDHI2 != 7]
    df = df[df.TOLDHI2 != 9]

    # _CHOLCHK (CholCheck)
    # Cholesterol check within past five years
    # 1 (Had cholesterol checked in past 5 years) --> 1
    # 2 (Did not have cholesterol checked in past 5 years) --> 0 
    # 3 (have never had cholesterol checked) --> 0
    # 9 (don't know/not sure/refused/missing) --> remove
    df['_CHOLCHK'] = df['_CHOLCHK'].replace({3:0,2:0})
    df = df[df._CHOLCHK != 9]

    # _BMI5 (BMI)
    # Body Mass Index (BMI)
    # no changes, just note that these are BMI * 100.
    # So for example a BMI of 4018 is really 40.18)
    df['_BMI5'] = df['_BMI5'].div(100).round(0)

    # SMOKE100 (Smoker)
    # Have you smoked at least 100 cigarettes in your entire life?
    # 1 (yes) --> 1
    # 2 (no) --> 0
    # 7 (dont knows) --> remove
    # 9 (refused) --> remove
    df['SMOKE100'] = df['SMOKE100'].replace({2:0})
    df = df[df.SMOKE100 != 7]
    df = df[df.SMOKE100 != 9]

    # CVDSTRK3 (Stroke)
    # (Ever told) you had a stroke.
    # 1 (yes) -> 1
    # 2 (no) -> 0
    # 7 (dont knows) -> remove
    # 9 (refused) -> remove
    df['CVDSTRK3'] = df['CVDSTRK3'].replace({2:0})
    df = df[df.CVDSTRK3 != 7]
    df = df[df.CVDSTRK3 != 9]

    # _MICHD (HeartDiseaseorAttack)
    # Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)
    # 1 (reported having) -> 1
    # 2 (did not report having) -> 0
    df['_MICHD'] = df['_MICHD'].replace({2: 0})

    # _TOTINDA (PhysActivity)
    # Adults who reported doing physical activity or exercise during the past 30 days other than their regular job
    # 1 (had physical activity) -> 1
    # 2 (No physical activity or exercise in last 30 days) -> 0 
    # 9 (don't know/refused) -> remove
    df['_TOTINDA'] = df['_TOTINDA'].replace({2:0})
    df = df[df._TOTINDA != 9]

    # _FRTLT1 (Fruits)
    # Consume Fruit 1 or more times per day
    # 1 (Consumed fruit one or more times per day) -> 1 
    # 2 (Consumed fruit less than one time per day) -> 0 
    # 9 (Don ́t know, refused or missing values) -> remove
    df['_FRTLT1'] = df['_FRTLT1'].replace({2:0})
    df = df[df._FRTLT1 != 9]

    # _VEGLT1 (Veggies)
    # Consume Vegetables 1 or more times per day
    # 1 (Consumed vegetables one or more times per day) -> 1 
    # 2 (Consumed vegetables less than one time per day) -> 0 
    # 9 (Don ́t know, refused or missing values) -> remove
    df['_VEGLT1'] = df['_VEGLT1'].replace({2:0})
    df = df[df._VEGLT1 != 9]

    # _RFDRHV5 (HvyAlcoholConsump)
    # Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)
    # 1 (no) -> 0
    # 2 (yes) -> 1
    # 9 (Don’t know/Refused/Missing) -> remove
    df['_RFDRHV5'] = df['_RFDRHV5'].replace({1:0, 2:1})
    df = df[df._RFDRHV5 != 9]

    # HLTHPLN1 (AnyHealthcare)
    # Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare, or Indian Health Service?
    # 1 (yes) -> 1
    # 2 (no) -> 0
    # 7 (Don’t know/Not Sure) -> remove
    # 9 (Refused) -> remove
    df['HLTHPLN1'] = df['HLTHPLN1'].replace({2:0})
    df = df[df.HLTHPLN1 != 7]
    df = df[df.HLTHPLN1 != 9]

    # MEDCOST (NoDocbcCost)
    # Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?
    # 1 (yes) -> yes
    # 2 (no) -> no
    # 7 (Don’t know/Not sure) -> remove
    # 9 (refused) -> remvoe
    df['MEDCOST'] = df['MEDCOST'].replace({2:0})
    df = df[df.MEDCOST != 7]
    df = df[df.MEDCOST != 9]

    # GENHLTH (GenHlth)
    # Would you say that in general your health is: (ordinal variable)
    # 1 Excellent
    # 2 Very good
    # 3 Good
    # 4 Fair
    # 5 Poor
    # 7 Don’t know/Not Sure -> remove
    # 9 Refused -> remove
    df = df[df.GENHLTH != 7]
    df = df[df.GENHLTH != 9]

    # MENTHLTH (MentHlth)
    # Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?
    # 1-30 (number of days)
    # 88 (None) -> 0 ; because it means none (no bad mental health days)
    # 77 (Don’t know/Not sure) -> remove
    # 99 (refused) -> remove
    df['MENTHLTH'] = df['MENTHLTH'].replace({88:0})
    df = df[df.MENTHLTH != 77]
    df = df[df.MENTHLTH != 99]

    # PHYSHLTH (PhysHlth)
    # Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?
    # 1-30 (number of days)
    # 88 (None) -> 0 ; because it means none (no bad physical health days)
    # 77 (Don’t know/Not sure) -> remove
    # 99 (refused) -> remove
    df['PHYSHLTH'] = df['PHYSHLTH'].replace({88:0})
    df = df[df.PHYSHLTH != 77]
    df = df[df.PHYSHLTH != 99]

    # DIFFWALK (DiffWalk)
    # Do you have serious difficulty walking or climbing stairs?
    # 1 (yes) -> yes
    # 2 (no) -> no
    # 7 (Don’t know/Not sure) -> remove
    # 9 (refused) -> remvoe
    df['DIFFWALK'] = df['DIFFWALK'].replace({2:0})
    df = df[df.DIFFWALK != 7]
    df = df[df.DIFFWALK != 9]

    # SEX (Sex)
    # Indicate sex of respondent.
    # in other words - is respondent male (somewhat arbitrarily chose this change because men are at higher risk for heart disease)
    # 1 (Male) -> 1
    # 2 (Female) -> 0
    df['SEX'] = df['SEX'].replace({2:0})

    # _AGEG5YR (Age)
    # Fourteen-level age category (ordinal)
    # 1 (18-24yrs) : 5 year increments : 13 (80 and older).
    # 14 (Don't know/Refused/Mising) -> remove
    df = df[df._AGEG5YR != 14]

    # EDUCA (Education)
    # What is the highest grade or year of school you completed? (ordinal)
    # 1 Never attended school or only kindergarten
    # 2 Grades 1 through 8 (Elementary)
    # 3 Grades 9 through 11 (Some high school)
    # 4 Grade 12 or GED (High school graduate)
    # 5 College 1 year to 3 years (Some college or technical school)
    # 6 College 4 years or more (College graduate)
    # 9 Refused -> remove
    df = df[df.EDUCA != 9]

    # INCOME2 (Income)
    # Is your annual household income from all sources: (ordinal)
    # 1 Less than $10,000 
    # 2 Less than $15,000 ($10,000 to less than $15,000) 
    # 3 Less than $20,000 ($15,000 to less than $20,000) 
    # 4 Less than $25,000 ($20,000 to less than $25,000)
    # 5 Less than $35,000 ($25,000 to less than $35,000)
    # 6 Less than $50,000 ($35,000 to less than $50,000)
    # 7 Less than $75,000 ($50,000 to less than $75,000)
    # 8 $75,000 or more
    # 77 Don’t know/Not sure -> remove
    # 99 Refused -> remove
    df = df[df.INCOME2 != 77]
    df = df[df.INCOME2 != 99]

    return df


if __name__ == "__main__":
  main(opt["--in_file"], opt["--out_file"])