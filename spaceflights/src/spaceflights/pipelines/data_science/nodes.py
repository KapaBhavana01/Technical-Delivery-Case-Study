"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""
from typing import Dict, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

import logging

logger = logging.getLogger(__name__)

def split_data(df: pd.DataFrame, parameters: Dict[str, any]) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X = df[parameters["features"]]
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"]
    )
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test,y_pred)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)



