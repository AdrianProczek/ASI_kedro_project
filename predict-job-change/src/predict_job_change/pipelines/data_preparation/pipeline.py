"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import merge_datasets, clean_data, generate_datetime_features


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=merge_datasets,
            inputs=["data1", "data2"],
            outputs="merged_data",
            name="merge_datasets_node"
        ),
        node(
            func=clean_data,
            inputs="merged_data",
            outputs="cleaned_data",
            name="cleaned_datasets_node"
        ),
        node(
            func=generate_datetime_features,
            inputs="cleaned_data",
            outputs="features_data",
            name="generate_features_node"
        )
    ])