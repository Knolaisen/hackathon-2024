import pandas as pd

# Read the data from the CSV files that lie next to this script using the absolute path
data1 = pd.read_csv('task1/CompanyCustomers.csv')
data2 = pd.read_csv('task1/PrivateCustomers.csv')

# Find the average account balance for each customer
total_balance = data1['AccountBalance'].sum() + data2['AccountBalance'].sum()
total_average_balance = data1['AverageAccountBalance'].sum() + data2['AverageAccountBalance'].sum()
total_customers = data1['AccountBalance'].count() + data2['AccountBalance'].count()
total_average_balance = total_balance / total_average_balance
print(total_average_balance)
