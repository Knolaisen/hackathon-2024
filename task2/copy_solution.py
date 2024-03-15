import pandas as pd

# Read the data from the CSV files that lie next to this script using the path "task1/CompanyCustomers.csv"
company_customers = pd.read_csv('task1/CompanyCustomers.csv')
private_customers = pd.read_csv('task1/PrivateCustomers.csv')
country_risk = pd.read_csv('task2/Country Risk.csv')
industry_risk = pd.read_csv('task2/Industry Risk.csv', encoding='ISO-8859-1')

# Print the keys of the first data frame
print(company_customers.keys())
print(private_customers.keys())
print(country_risk.keys())
print(industry_risk.keys())

# Using the provided data, create a dictionary with the following structure:
# {
#     "CustomerID": {
#         "coface_country_risk_assessment"": "A4",
#         "length_of_customer_relationship": 5,
#         "industry risk": 0.5,
#         "face_to_face_established": True
#     }
# }

# The "coface_country_risk_assessment" should be the value from the "Country Risk" data frame
# The "length_of_customer_relationship" should be the number of years the customer has been a customer
# The "industry risk" should be the value from the "Industry Risk" data frame
# The "face_to_face_established" should be True if the customer has had a face to face meeting with the company, False otherwise

# Now I will create a dictionary with CustomerID as keys and "coface_country_risk_assessment" as values
country_risk_assessment = {}
for i in range(len(company_customers)):
    # Find the country of the customer
    country = company_customers['Country'][i]
    
    # Convert the country to the country risk assessment
    for j in range(len(country_risk)):

        if country_risk['Country'][j] == country.upper():
            risk = country_risk['coface_country_risk_assessment'][j]
            country_risk_assessment[company_customers['CustomerID'][i]] = risk

print(country_risk_assessment)

# Find the unique coface_country_risk_assessment values
unique_risk = country_risk['coface_country_risk_assessment'].unique()
print(unique_risk)

# Score the coface_country_risk_assessment values from A1, A2, A3, A4, B, C, D, E
risk_score = {
    'A1': 1,
    'A2': 2,
    'A3': 3,
    'A4': 4,
    'B': 5,
    'C': 6,
    'D': 7,
    'E': 8
}

# Create a new dictionary with CustomerID as keys and risk_scores as values
country_risk_assessment_score = {}

for key, value in country_risk_assessment.items():
    country_risk_assessment_score[key] = risk_score[value]

print(country_risk_assessment_score)

# Now I will create a dictionary with CustomerID as keys and "face_to_face_established" as values
# face_to_face = {}
# for i in range(len(company_customers)):
#     face_to_face[company_customers['CustomerID'][i]] = company_customers['Face_to_Face_Establishment'][i]

# print(face_to_face)