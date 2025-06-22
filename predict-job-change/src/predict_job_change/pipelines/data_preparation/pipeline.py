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
    clean_missing_values,
    encode_and_scale
    # split_features_target,
    # split_train_test,
    # train_model,
    # evaluate_model
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=clean_missing_values,
            inputs="main_dataset",
            outputs="clean_data",
            name="clean_missing_values_node"
        ),
        node(
            func=encode_and_scale,
            inputs="clean_data",
            outputs="encoded_scaled_data",
            name="encode_and_scale_node"
        )
        # node(
        #     func=split_features_target,
        #     inputs="encoded_scaled_data",
        #     outputs=["X", "y"],
        #     name="split_features_target_node"
        # )
        # ),
        # node(
        #     func=split_train_test,
        #     inputs=["X", "y"],
        #     outputs=["X_train", "X_test", "y_train", "y_test"],
        #     name="split_train_test_node"
        # ),
        # node(
        #     func=train_model,
        #     inputs=["X_train", "y_train"],
        #     outputs="trained_model",
        #     name="train_model_node"
        # ),
        # node(
        #     func=evaluate_model,
        #     inputs=["trained_model", "X_test", "y_test"],
        #     outputs="model_accuracy",
        #     name="evaluate_model_node"
        # )
    ])
