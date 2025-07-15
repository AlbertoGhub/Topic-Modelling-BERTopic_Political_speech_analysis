# THIS FILE CONTAINS ALL THE MODULES TO BE USED IN THE MAIN API

# Importing necessary libraries
import pandas as pd
import numpy as np
import re
import plotly.express as px
from cleantext import clean
from datetime import datetime


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


# Visualization function to plot the distribution of topics
def plot_topics(topic_model, topic_ids):
    """
    Generate a list of Plotly Express bar charts (figures) for each topic ID.
    You can later display them using fig.show().
    """
    figures = []

    for topic_id in topic_ids:
        # Get topic terms and probabilities
        top_words = topic_model.get_topic(topic_id)
        if not top_words:
            continue

        # Convert to DataFrame
        df_topic_words = pd.DataFrame(top_words, columns=["Word", "Probability"]).iloc[::-1]

        # Create horizontal bar chart
        fig = px.bar(
            df_topic_words,
            x="Probability",
            y="Word",
            orientation="h",
            title=f"Top Terms in Topic {topic_id}",
            color="Probability",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            xaxis_title="Probability",
            yaxis_title="Word",
            plot_bgcolor="white"
        )

        figures.append(fig)
    
    return figures

# Date formating function to convert date strings to datetime objects

def standardise_date(date_str):

    '''Standardises date format from various formats to 'DD-MM-YYYY'.
    (source: https://www.ionos.co.uk/digitalguide/websites/web-development/convert-strings-to-datetime-in-python/)'''
    
    # Remove the hours using regex
    date_str = re.sub(r'\s00:00:00$', '', date_str)
    
    # Replace '/' with '-'
    date_str = date_str.replace('/', '-')
    
    # Split the date string by '-'
    parts = date_str.split('-')
    
    # Ensure there are at least 3 parts
    if len(parts) < 3:
        return date_str  # or return None / np.nan if preferred
    
    # Check if first part has 4 digits (year)
    if len(parts[0]) == 4 and parts[0].isdigit():
        # Format: YYYY-MM-DD, swap to DD-MM-YYYY
        day, month, year = parts[2], parts[1], parts[0]
    else:
        # Format already starts with day: DD-MM-YYYY or DD-MM-YY
        day, month, year = parts[0], parts[1], parts[2]
    
    final_date = f"{int(day):02d}-{int(month):02d}-{year}"
    
    # Parse to datetime object
    return datetime.strptime(final_date, '%d-%m-%Y').date()