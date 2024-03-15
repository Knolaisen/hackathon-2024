import pandas as pd

customer_risk_data = pd.read_csv('task2/customer_risk_data.csv')

# Create an empty dictionary to store the risk assessment result
risk_assessment = {}

# Iterate over each row in the customer risk data
for index, row in customer_risk_data.iterrows():
    # Extract the relevant columns from the row
    customer_id = row['CustomerID']
    industry_risk = row['IndustryRisk']
    face_to_face_established = row['FaceToFaceEstablished']
    country_risk = row['CountryRisk']
    relationship_length = row['RelationshipLength']
    
    # Perform the risk assessment based on the given criteria
    if industry_risk == 0 and face_to_face_established == 1 and country_risk == 0 and relationship_length > 5:
        risk = 'Low'
    elif industry_risk == 2 or face_to_face_established == 0 or country_risk == 2 or relationship_length <= 5:
        risk = 'High'
    else:
        risk = 'Medium'
    
    # Store the risk assessment result in the dictionary
    risk_assessment[customer_id] = risk

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