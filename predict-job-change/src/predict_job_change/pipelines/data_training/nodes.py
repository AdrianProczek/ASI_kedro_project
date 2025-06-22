
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def split_data(data: pd.DataFrame) -> tuple:
    x = data[["city_development_index", "gender", "relevent_experience", "enrolled_university", "education_level",
              "major_discipline", "experience", "company_size", "company_type", "last_new_job"]]
    y = data["target"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
    return x_train, x_test, y_train, y_test



def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:

    dt_model = DecisionTreeClassifier(max_leaf_nodes=8, random_state=1)
    dt_model.fit(x_train, y_train)
    return dt_model


def evaluate_model(
    dt_model: DecisionTreeClassifier, x_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, float]:


    y_predictions = dt_model.predict(x_test)
    y_accuracy = accuracy_score(y_test, y_predictions)

    return {"Model accuracy": y_accuracy}
