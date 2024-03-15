import pandas as pd

# Read the data from the CSV files that lie next to this script using the absolute path
data1 = pd.read_csv('task1/CompanyCustomers.csv')
data2 = pd.read_csv('task1/PrivateCustomers.csv')

# Get the unique countries from the data and add each to a set
unique_countries1 = set(data1['Country'])
unique_countries2 = set(data2['Country'])

# Combine the unique countries from both datasets and remove duplicates
unique_countries = unique_countries1.union(unique_countries2)

print(f"There are {len(unique_countries)} different countries in the data.")