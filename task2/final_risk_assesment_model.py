import pandas as pd
import numpy as np

customer_risk_data = pd.read_csv('task2/customer_risk_data.csv')

# Create an empty dictionary to store the risk assessment result
risk_assessment = {}

# Iterate over each row in the customer risk data
for index, row in customer_risk_data.iterrows():
    # Extract the relevant columns from the row
    customer_id = row['CustomerID']
    industry_risk = row['IndustryRisk'] # 0, 1, 2
    face_to_face_established = row['FaceToFaceEstablished'] # 0, 1
    country_risk = row['CountryRisk'] # 0, 1, 2
    relationship_length = row['RelationshipLength'] # 0, 1, 2
    
    # Perform the risk assessment based on the given criteria
    basescore = 1
    if industry_risk == 0:
        basescore *= 0.6
    elif industry_risk == 1:
        basescore *= 1.1
    elif industry_risk == 2:
        basescore *= 1.5

    if face_to_face_established == 0:
        basescore *= 1.5
    elif face_to_face_established == 1:
        basescore *= 0.6

    if country_risk == 0:
        basescore *= 0.6
    elif country_risk == 1:
        basescore *= 1.1
    elif country_risk == 2:
        basescore *= 1.5

    # Convert the relationship length to a score between 0 and 1 using negative exponential function
    relationship_score = 1 - np.exp(-relationship_length)

    basescore *= relationship_score * 2
    
    if basescore < 1.07:
        risk = 'Low'
    elif basescore > 1.5:
        risk = 'High'
    else:
        risk = 'Medium'

    # Store the risk assessment result in the dictionary
    risk_assessment[int(customer_id)] = risk

# Print the risk assessment dictionary
print(risk_assessment)

# Count the number of customers in each risk category
low_risk_count = sum(1 for value in risk_assessment.values() if value == 'Low')
medium_risk_count = sum(1 for value in risk_assessment.values() if value == 'Medium')
high_risk_count = sum(1 for value in risk_assessment.values() if value == 'High')

# Print the counts of customers in each risk category
print("Low risk count:", low_risk_count)
print("Medium risk count:", medium_risk_count)
print("High risk count:", high_risk_count)