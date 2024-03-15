import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pandas as pd

# Fake data
X: pd.DataFrame = pd.DataFrame()
y: pd.DataFrame = pd.DataFrame()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Define model
model = xgb.XGBClassifier(
    max_depth=3,
    n_estimators=100,
    learning_rate=0.1,
    subsample=0.5,
    colsample_bytree=0.5,
    gamma=1,
    random_state=42
)

# TODO

# Train the model
model.fit(X_train, y_train)

# Make prediction
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)


