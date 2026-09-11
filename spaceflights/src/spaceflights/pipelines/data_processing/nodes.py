"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.0.0
"""
import pandas as pd

def _is_true(c: pd.Series) -> pd.Series:
    return c == "t"

def parse_percent(c: pd.Series) -> pd.Series:
    return c.str.replace("%","").astype(float)

def parse_money(c: pd.Series) -> pd.Series:
    return c.str.replace("$","").str.replace(",","").astype(float)

def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    df["iata_approved"] = _is_true(df["iata_approved"])
    df["company_rating"] = parse_percent(df["company_rating"])
    return df

def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    df["d_check_complete"] = _is_true(df["d_check_complete"])
    df["moon_clearance_complete"] = _is_true(df["moon_clearance_complete"])
    df["price"] = parse_money(df["price"])
    return df

def create_model_input_table(
        shuttles: pd.DataFrame,
        companies: pd.DataFrame,
        reviews: pd.DataFrame,
) -> pd.DataFrame:
    rated_shuttles = shuttles.merge(reviews, left_on = "id", right_on = "shuttle_id")
    model_input_table = rated_shuttles.merge(companies, left_on = "company_id", right_on = "id")
    return model_input_table.dropna()