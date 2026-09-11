"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import evaluate_model, train_model, split_data


def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline([
        node(
            func=split_data,
            inputs=["model_input_table","params:model_options"],
            outputs=["X_train","X_test","y_train","y_test"],
        ),
        node(
            func=train_model,
            inputs=["X_train","y_train"],
            outputs="regressor",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor","X_test", "y_test"],
            outputs=None,
        ),
    ])

    ds_pipeline_1 = pipeline(
        pipeline_instance,
        inputs="model_input_table",
        namespace="active_modelling_pipeline",
    )
    ds_pipeline_2 = pipeline(
        pipeline_instance,
        inputs="model_input_table",
        namespace="candidate_modelling_pipeline",
    )

    return ds_pipeline_1 + ds_pipeline_2