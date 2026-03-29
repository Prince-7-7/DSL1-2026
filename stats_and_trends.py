# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 05:50:44 2026

@author: pb25aap
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import stats 

def create_dataframes(file):
    """
    Function will take a file as input and return two dataframes which are 
    transposes of each other.

    Parameters
    ----------
    file : string
        the name of a csv or xlsx file.

    Returns
    -------
    Two dataframes where one is the transpose of the other.

    """
    #creates a dataframe from the file
    table = pd.read_csv(file)
    
    #cleaning the data
    df = table.dropna(axis='columns', how='all')
    df = df.dropna(axis='rows', thresh=5)
    
    # print(table2)
    # clean = []
    # for i in table2.columns:
    #     print(i)
    #     if table2[i].dtype == table2["Country Code"].dtype:
    #         clean.append(i)
            
    # df = table2.drop(clean[1:], axis=1)
    
    #creates a transposed dataframe of the initial database
    df_transpose = df.transpose()
    df_transpose.columns = df_transpose.iloc[0]
    #df_transpose.drop(df_transpose.iloc[0])
    print(df_transpose.head())
    
    return df, df_transpose

            

    
#%%
#test
df, df_transpose = create_dataframes(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Data Science Laboratory 1\stats & trends assignment\agricultural_land.csv")

print(df.head())
print(df_transpose.head())
print()
print(df.describe())
print(df_transpose.describe())

#%%
