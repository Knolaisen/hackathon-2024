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

country_risk_assessment = {}
for i in range(len(company_customers)):
    # Find the country of the customer
    country = company_customers['Country'][i]
    
    # Convert the country to the country risk assessment
    for j in range(len(country_risk)):

        if country_risk['Country'][j] == country.upper():
            risk = country_risk['coface_country_risk_assessment'][j]
            country_risk_assessment[company_customers['CustomerID'][i]] = risk

# Do the same for private customers
for i in range(len(private_customers)):
    # Find the country of the customer
    country = private_customers['Country'][i]
    
    # Convert the country to the country risk assessment
    for j in range(len(country_risk)):

        if country_risk['Country'][j] == country.upper():
            risk = country_risk['coface_country_risk_assessment'][j]
            country_risk_assessment[private_customers['CustomerID'][i]] = risk

# print(country_risk_assessment)

# Find the unique coface_country_risk_assessment values
unique_risk = country_risk['coface_country_risk_assessment'].unique()
# print(unique_risk)

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

# Place all with country_risk_assessment_score under 5 in risk category "Low"
# Place all with country_risk_assessment_score between 5 and 7 in risk category "Medium"
# Place all with country_risk_assessment_score above 7 in risk category "High"
    
# Create a dictionary with CustomerID as keys and risk category as values
country_risk_category = {}

for key, value in country_risk_assessment_score.items():
    if value < 5:
        country_risk_category[key] = "Low"
    elif value >= 5 and value <= 7:
        country_risk_category[key] = "Medium"
    else:
        country_risk_category[key] = "High"

print(country_risk_category)

# Find the sizes of the risk categories
low_risk = 0
medium_risk = 0
high_risk = 0

for key, value in country_risk_category.items():
    if value == "Low":
        low_risk += 1
    elif value == "Medium":
        medium_risk += 1
    else:
        high_risk += 1

print(low_risk, medium_risk, high_risk)
    