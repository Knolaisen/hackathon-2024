from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.svm import SVC
from src.features.ml_service import prepare_data, prepare_test_data
import sys
import os

# Get the current working directory
current_working_directory = os.path.dirname(__file__)

# Add the parent directory to sys.path
sys.path.append(current_working_directory)

# Change directory to task5/notebooks
os.chdir(os.path.join(current_working_directory, "notebooks"))

# Load data
x_train, x_val, x_test, y_train, y_val, y_test = prepare_data()

# Train data
svm = SVC(kernel="linear", C=1.0)
svm.fit(x_train, y_train)

# Make prediction
y_val_pred = svm.predict(x_val)

# Evaluate the model
accuracy = accuracy_score(y_val, y_val_pred)
precision = precision_score(y_val, y_val_pred)
recall = recall_score(y_val, y_val_pred)
f1 = f1_score(y_val, y_val_pred)

print("Evaluation metrics on validation set:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")
