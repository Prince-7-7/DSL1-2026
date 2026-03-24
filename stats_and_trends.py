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
    df = pd.read_csv(file)
    #creates a transposed dataframe of the initial database
    df_transpose = df.transpose()
    
    return df, df_transpose

            

    
#%%
#test
df, df_transpose = create_dataframes(r"C:\Users\pb25aap\OneDrive - University of Hertfordshire\Data Science Laboratory 1\lerwickdata.csv")

print(df.describe())
print(df_transpose.describe())