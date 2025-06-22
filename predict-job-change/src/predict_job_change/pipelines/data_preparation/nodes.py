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
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

def clean_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    data["gender"] = data["gender"].fillna("No data")
    data["company_size"] = data["company_size"].fillna("No data")
    return data

def encode_and_scale(data: pd.DataFrame) -> pd.DataFrame:
    data = pd.get_dummies(data)
    scaler = MinMaxScaler()
    data[data.columns] = scaler.fit_transform(data)
    return data

# def split_features_target(data: pd.DataFrame) -> tuple:
#     X = data.drop("target", axis=1)
#     y = data["target"]
#     return X, y

# def split_train_test(X: pd.DataFrame, y: pd.Series) -> tuple:
#     return train_test_split(X, y, test_size=0.2, random_state=42)
#
# def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
#     model = RandomForestClassifier(random_state=42)
#     model.fit(X_train, y_train)
#     return model
#
# def evaluate_model(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> float:
#     y_pred = model.predict(X_test)
#     acc = accuracy_score(y_test, y_pred)
#     print(f"Accuracy: {acc:.2f}")
#     return acc
