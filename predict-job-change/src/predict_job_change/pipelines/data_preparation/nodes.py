"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.13
"""

import pandas as pd

def merge_datasets(df_initial: pd. DataFrame, df_new: pd. DataFrame) -> pd. DataFrame:
    return pd.concat ( [df_initial, df_new])

def clean_data(df: pd. DataFrame) -> pd. DataFrame:
    # Remove duplicates
    return df.drop_duplicates (subset= ["Date"])

def generate_datetime_features(df: pd.DataFrame) -> pd.DataFrame:

    ### Extract date time features
    df ['Date'] = pd.to_datetime(df[' Date'])

    # Add a column for year
    df['year_num'] = df['Date'].dt.year

    # Add a column for month
    df['month _num'] = df['Date'].dt.month

    # Add a column for day of week
    df['dayofweek num'] = df['Date'].dt.dayofweek

    # Add a column for day of month
    df['dayofmonth'] = df['Date'].dt.day

    # Add a column for day of year
    df['dayofyear_num'] = df['Date'].dt.day_of_year

    return df