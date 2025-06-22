# """
# This is a boilerplate pipeline 'data_preparation'
# generated using Kedro 0.19.13
# """
#
# import pandas as pd
#
# def merge_datasets(df_initial: pd. DataFrame, df_new: pd. DataFrame) -> pd. DataFrame:
#     return pd.concat ( [df_initial, df_new])
#
# def clean_data(df: pd. DataFrame) -> pd. DataFrame:
#     # Remove duplicates
#     return df.drop_duplicates (subset= ["Date"])
#
# def generate_datetime_features(df: pd.DataFrame) -> pd.DataFrame:
#
#     ### Extract date time features
#     df ['Date'] = pd.to_datetime(df[' Date'])
#
#     # Add a column for year
#     df['year_num'] = df['Date'].dt.year
#
#     # Add a column for month
#     df['month _num'] = df['Date'].dt.month
#
#     # Add a column for day of week
#     df['dayofweek num'] = df['Date'].dt.dayofweek
#
#     # Add a column for day of month
#     df['dayofmonth'] = df['Date'].dt.day
#
#     # Add a column for day of year
#     df['dayofyear_num'] = df['Date'].dt.day_of_year
#
#     return df



"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.13
"""

import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

def remove_rows_with_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna(subset=["gender"])
    return data


def encode_categorical_columns(data: pd.DataFrame) -> pd.DataFrame:
    mappings = {
        "gender": {"Other": 0, "Female": 1, "Male": 2},
        "relevent_experience": {"No relevent experience": 0, "Has relevent experience": 1},
        "enrolled_university": {"no_enrollment": 0, "Part time course": 1, "Full time course": 2},
        "education_level": {"Primary School": 0, "High School": 1, "Graduate": 2, "Masters": 3, "Phd": 4},
        "major_discipline": {"No Major": 0, "Other": 1, "Humanities": 2, "Arts": 3, "Business Degree": 4, "STEM": 5},
        "experience": {"<1": 0, ">20": 21},
        "company_size": {"<10": 0, "10/49": 1, "50-99": 2, "100-500": 3, "500-999": 4, "1000-4999": 5, "5000-9999": 6,
                         "10000+": 7},
        "company_type": {"Funded Startup": 0, "Early Stage Startup": 1, "Pvt Ltd": 2, "Public Sector": 3, "NGO": 4,
                         "Other": 5},
        "last_new_job": {"never": 0, ">4": 5}
    }
    for col, mapping in mappings.items():
        if col in data.columns:
            data[col] = data[col].map(mapping)
    return data


def fill_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    num_imputer = SimpleImputer(strategy="median")
    cat_imputer = SimpleImputer(strategy="most_frequent")

    if "education_level" in data.columns and "major_discipline" in data.columns:
        data.loc[(data["education_level"].isin([0, 1])) & (data["major_discipline"].isna()), "major_discipline"] = 0

    categorical_columns = ["enrolled_university", "education_level", "company_size", "company_type", "major_discipline"]
    for col in categorical_columns:
        if col in data.columns:
            data[col] = cat_imputer.fit_transform(data[[col]])

    numerical_columns = ["experience", "last_new_job"]
    for col in numerical_columns:
        if col in data.columns:
            data[col] = num_imputer.fit_transform(data[[col]])
    return data


def normalize_numerical_columns(data: pd.DataFrame) -> pd.DataFrame:
    scaler = MinMaxScaler()
    data["training_hours"] = scaler.fit_transform(data[["training_hours"]])
    return data

