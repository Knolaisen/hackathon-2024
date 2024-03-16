import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
import numpy as np

# Load the data
trainingData = pd.read_csv("task5\data\Transaction data training.csv")

# One-hot encode the categorical data
encodedTrainingData = pd.get_dummies(trainingData, columns=[
    "Origin_Currency", "Opposite_party_Country", 
    "Transaction_Type", "Transaction_Location", "Deposit_Withdrawal"
])

# Convert date columns to numerical value (if you haven't already)
# ...

# Drop unnecessary columns from encodedTrainingData, not trainingData
encodedTrainingData.drop([
    'TransactionID', 'CustomerID', 'Merchant_Code', 'Opposite_party_ID', 
    'Opposite_party_Name', 'Opposite_party_Adress', 'Opposite_party_City', 
    'Transaction_Text', 'Transaction_Description_0', 'Transaction_Description_1', 
    'Transaction_Description_2', "CDB_Location_Country_x", "Currency",  
    "CDB_Location_CountryCode"
], axis=1, inplace=True)

# Apply StandardScaler to numerical features only
scaler = StandardScaler()

# Scale all remaining features except 'IsFraud'
features = encodedTrainingData.drop('IsFraud', axis=1).select_dtypes(include=[np.number])
scaled_features = scaler.fit_transform(features)
scaled_df = pd.DataFrame(scaled_features, index=features.index, columns=features.columns)

# Add back the 'IsFraud' column to scaled_df
scaled_df['IsFraud'] = encodedTrainingData['IsFraud']

#Split data into features and target
X = scaled_df.drop('IsFraud', axis=1)
y = scaled_df['IsFraud']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now, scaled_df is ready for model training
print("Success! Data is ready for model training.")

# Train the model
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix: {conf_matrix}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")