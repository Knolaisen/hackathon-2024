""" This module contains functions to prepare the data for the model. """

from matplotlib.pyplot import sca
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np


def engineer_features(features: pd.DataFrame) -> pd.DataFrame:
    """
    Conduct the required feature engineering.

    Args:
        features: The features to engineer.

    Returns:
        The engineered features.
    """

    # One-hot encode the categorical data
    encodedTrainingData = pd.get_dummies(
        features,
        columns=[
            "Origin_Currency",
            "Currency",
            "CDB_Location_Country_x",
            "CDB_Location_CountryCode",
            "Opposite_party_Country",
            "Transaction_Type",
            "Transaction_Location",
            "Deposit_Withdrawal",
        ],
    )

    # Drop unnecessary columns from encodedTrainingData, not trainingData
    encodedTrainingData.drop(
        [
            "TransactionID",
            "CustomerID",
            "Merchant_Code",
            "Opposite_party_ID",
            "Opposite_party_Name",
            "Opposite_party_Adress",
            "Opposite_party_City",
            "Transaction_Text",
            "Transaction_Description_0",
            "Transaction_Description_1",
            "Transaction_Description_2",
        ],
        axis=1,
        inplace=True,
    )

    # Apply StandardScaler to numerical features only
    scaler = StandardScaler()

    # Scale all remaining features except 'IsFraud'
    features = encodedTrainingData.drop(
        "IsFraud", axis=1, errors="ignore"
    ).select_dtypes(include=[np.number])
    scaled_features = scaler.fit_transform(features)
    scaled_df = pd.DataFrame(
        scaled_features, index=features.index, columns=features.columns
    )

    return scaled_df
