# """
# This is a boilerplate pipeline 'data_preparation'
# generated using Kedro 0.19.13
# """
#
# from kedro.pipeline import node, Pipeline, pipeline  # noqa
# from .nodes import merge_datasets, clean_data, generate_datetime_features
#
#
# def create_pipeline(**kwargs) -> Pipeline:
#     return pipeline([
#         node(
#             func=merge_datasets,
#             inputs=["data1", "data2"],
#             outputs="merged_data",
#             name="merge_datasets_node"
#         ),
#         node(
#             func=clean_data,
#             inputs="merged_data",
#             outputs="cleaned_data",
#             name="cleaned_datasets_node"
#         ),
#         node(
#             func=generate_datetime_features,
#             inputs="cleaned_data",
#             outputs="features_data",
#             name="generate_features_node"
#         )
#     ])



"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.13
"""

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
            inputs="main_dataset",
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
