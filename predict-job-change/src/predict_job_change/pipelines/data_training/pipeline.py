from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    split_data,
    train_model,
    evaluate_model
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["normalized_data"],
                outputs=["x_train", "x_test", "y_train", "y_test"],
                name="split_data",
            ),
            node(
                func=train_model,
                inputs=["x_train", "y_train"],
                outputs="dt_model",
                name="train_model",
            ),
            node(
                func=evaluate_model,
                inputs=["dt_model", "x_test", "y_test"],
                outputs=None,
                name="evaluate_model",
            ),
        ]
    )
