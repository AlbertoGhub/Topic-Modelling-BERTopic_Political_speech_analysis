# THIS FILE CONTAINS ALL THE MODULES TO BE USED IN THE MAIN API

# Importing necessary libraries
import pandas as pd
import numpy as np
from cleantext import clean

# Function to calculate the missing values and their percentages in a DataFrame
def missing_values_calculator_and_shape(data):
    '''CALCULATING THE MISSING VALUES, AND DATA TYPE'''
    null_values = data.isna().sum().sort_values(ascending=False)
    per_values = data.isna().mean().sort_values(ascending=False)
    names = null_values.index
    data_type = data[names].dtypes
    information = pd.DataFrame({'NAMES': names,
                        'NULL VALUE COUNT': null_values,
                        'NULL VALUES IN PERCENTAGES (%)': per_values,
                        'DATA TYPE': data_type})
    information = information.reset_index(drop=True)
    return information

# Function to remove special characters from a string
def text_cleaning_process(text):
    '''CLEANING THE TEXT DATA'''
    text = clean(str(text), punct=True, numbers = True, extra_spaces=True)  # remove punctuation, numbers                      
    text = clean(text, lowercase=True)                                      # and extra spaces      
    return text.lower()                                                     # lowercase text



