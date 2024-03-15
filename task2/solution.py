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


