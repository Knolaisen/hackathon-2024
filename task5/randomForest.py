import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

# Load the data
trainingData = pd.read_csv("task5\data\Transaction data training.csv")

# One-hot encode the categorical data
encodedTrainingData = pd.get_dummies(trainingData, columns=[
    "Origin_Currency", "Currency", "CDB_Location_Country_x", 
    "CDB_Location_CountryCode", "Opposite_party_Country", 
    "Transaction_Type", "Transaction_Location", "Deposit_Withdrawal"
])

# Drop unnecessary columns from encodedTrainingData, not trainingData
encodedTrainingData.drop([
    'TransactionID', 'CustomerID', 'Merchant_Code', 'Opposite_party_ID', 
    'Opposite_party_Name', 'Opposite_party_Adress', 'Opposite_party_City', 
    'Transaction_Text', 'Transaction_Description_0', 'Transaction_Description_1', 
    'Transaction_Description_2'
], axis=1, inplace=True)

# Apply StandardScaler to numerical features only
scaler = StandardScaler()

# Scale all remaining features except 'IsFraud'
features = encodedTrainingData.drop('IsFraud', axis=1).select_dtypes(include=[np.number])
scaled_features = scaler.fit_transform(features)
scaled_df = pd.DataFrame(scaled_features, index=features.index, columns=features.columns)

# Add back the 'IsFraud' column to scaled_df
scaled_df['IsFraud'] = encodedTrainingData['IsFraud']

print("Success! Data is ready for model training.")

# Split data into features and target
X = scaled_df.drop('IsFraud', axis=1)
y = scaled_df['IsFraud']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Success! Data is ready for model training.")

#Initialize the model for Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

#Identify the important features
importances = model.feature_importances_

#Select the important features
selector = SelectFromModel(model, threshold=0.01)
X_important_train = selector.transform(X_train)
X_important_test = selector.transform(X_test)

#Train the model with the important features
important_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
important_model.fit(X_important_train, y_train)

#Make predictions
y_pred = important_model.predict(X_important_test)

#Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy: ", accuracy)
print("Confusion Matrix: ", conf_matrix)
print("Precision: ", precision)
print("Recall: ", recall)