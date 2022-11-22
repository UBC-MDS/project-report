# author: Austin Shih
# date: 2022-11-22

"""Takes clean dataset from clean.py and produces exploratory data visualizations to better understand cleaned data.

Usage: diabetes_eda.py --clean_data=<clean_data> --distr_file=<distr_file> --corr_file=<corr_file>

Options:
--clean_data=<clean_data>    Relative path of cleaned dataset 
--distr_file=<distr_file>    Relative path to output file directory
--corr_file=<corr_file>      Relative path to output file directory
"""
# python diabetes_eda.py --clean_data=../data/clean/LLCP2015_cleaned.csv --distr_file=../results --corr_file=../results

# Imports 
from docopt import docopt
import pandas as pd
import altair as alt
from altair_saver import save
import os

# docopt 
opt = docopt(__doc__)

def main(clean_data, distr_file, corr_file):

    # create result directory
    if os.path.exists("../results") == False:
        print('Results directory does not exist, creating directory...')
        os.mkdir('../results')
    else:
        print('Results directory exists')

    # read clean csv
    try:
        df = pd.read_csv(clean_data)        # df = pd.read_csv(../data/clean/LLCP2015_cleaned.csv)
    except FileNotFoundError:
        print("Input csv file of train set does not exist.")
        os._exit()

    # Distributions of complete data set
    df_cols = df.columns.tolist()

    # distribution plots
    df_plot = alt.Chart(df).mark_bar().encode(
        alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=60)),
        alt.Y('count()'),
        color = 'Diabetes_012'
    ).properties(
        height=200,
        width=320
    ).repeat(
        df_cols,
        columns = 3)

    # save distribution plot
    df_plot.save(distr_file + '/' +'distribution.png')

    try:
        df_plot.save(distr_file + '/' +'distribution.png')
        print("distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))

    # correlation plots
    corr_plot = df.corr('spearman').style.background_gradient() 

    # save correlation plot
    try:
        corr_plot.to_excel(corr_file + '/' + 'correlation.xlsx')
        print("correlation csv file generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))

if __name__ == "__main__":
    main(opt["--clean_data"], opt["--distr_file"], opt["--corr_file"])
