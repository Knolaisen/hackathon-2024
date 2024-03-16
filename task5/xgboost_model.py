from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import GridSearchCV
import pandas as pd
import xgboost as xgb


def load_data(path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Temporary data load
    """

    data = pd.read_csv(path)

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Encode data
    X = pd.get_dummies(X, columns=[
        "Origin_Currency", "Currency", "CDB_Location_Country_x",
        "CDB_Location_CountryCode", "Opposite_party_Country",
        "Transaction_Type", "Transaction_Location", "Deposit_Withdrawal"
    ])

    # Drop unnecessary columns
    X.drop([
        "Origin_Date", "System_Date", "Completed_Date",
        'TransactionID', 'CustomerID', 'Merchant_Code', 'Opposite_party_ID',
        'Opposite_party_Name', 'Opposite_party_Adress', 'Opposite_party_City',
        'Transaction_Text', 'Transaction_Description_0', 'Transaction_Description_1',
        'Transaction_Description_2'
    ], axis=1, inplace=True)

    # print(X)
    # print(X.dtypes)
    # exit()

    return X, y


# Load training data
X, y = load_data("task5/data/Transaction data training.csv")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Hyperparameter optimization
param_grid = {
    "max_depth": [3],  # , 5, 7],
    "n_estimators": [50],  # , 100, 150],
    "learning_rate": [0.05],  # , 0.1, 0.2],
    "subsample": [0.5],
    "colsample_bytree": [0.5],
    "gamma": [1],
    "random_state": [42],
}

grid_search = GridSearchCV(
    estimator=xgb.XGBClassifier(), param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
print(f"Best parameters: {best_params}")

# Train optimized model
model = xgb.XGBClassifier(**best_params)
model.fit(X_train, y_train)

# Make prediction
y_pred = (model.predict(X_test) >= 0.5).astype(int)

# Evaluate accuracy and precision
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Number of positives: {sum(y_pred)}")
