""" This module contains functions to load the data, directly from the source. """

import pandas as pd


def load_data_raw() -> tuple[pd.DataFrame, pd.Series]:
    """Load the data and return the features and target variable."""
    data = pd.read_csv("../data/Transaction data training.csv")
    target_column = "IsFraud"
    x = data.drop(target_column, axis=1)
    y = data[target_column]
    return x, y


def load_test_raw_data() -> pd.DataFrame:
    """Load the test data."""
    data = pd.read_csv("../data/Transaction data test.csv")
    return data
