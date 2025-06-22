from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    remove_rows_with_missing_values,
    encode_categorical_columns,
    fill_missing_values,
    normalize_numerical_columns
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=remove_rows_with_missing_values,
            inputs="dataset",
            outputs="data_without_missing_gender_rows",
            name="remove_rows_with_missing_gender_values"
        ),
        node(
            func=encode_categorical_columns,
            inputs="data_without_missing_gender_rows",
            outputs="encoded_data",
            name="encode_categorical_variables"
        ),
        node(
            func=fill_missing_values,
            inputs="encoded_data",
            outputs="imputed_data",
            name="fill_missing_data"
        ),
        node(
            func=normalize_numerical_columns,
            inputs="imputed_data",
            outputs="normalized_data",
            name="normalize_data"
        )
    ])
