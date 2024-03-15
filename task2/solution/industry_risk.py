import pandas as pd
class IndustryRiskCalculator:
    def __init__(self):
        self.industry_risk_df = pd.read_csv("task2/Industry Risk.csv", encoding='ISO-8859-1')
        self.company_customers_df = pd.read_csv('task1/CompanyCustomers.csv', encoding='ISO-8859-1')
        self.merged_df = None

    def calculate_risk(self):
        # Convert the 'code' column in industry_risk_df to string to ensure matching types for the merge
        self.industry_risk_df['code'] = self.industry_risk_df['code'].astype(str)
        # Join the DataFrames on the specified columns
        self.merged_df = pd.merge(self.company_customers_df, self.industry_risk_df, left_on='IndustrialCodeLevel3', right_on='code', how='left')
        # Give CustomerID",Risk"
        customers_with_risk = self.merged_df[['CustomerID', 'Risk']]
        # Set 'CustomerID' as the index and select the 'Risk' column, then convert to dictionary
        obj = customers_with_risk.set_index('CustomerID')['Risk'].to_dict()
        # Convert the 'Risk' column to values 0, 1 or 2 based on the risk category
        for key, value in obj.items():
            if value == 'Low':
                obj[key] = 0
            elif value == 'Medium':
                obj[key] = 1
            elif value == 'High':
                obj[key] = 2

        # If nan, set to "High"
        for key, value in obj.items():
            if value != 0 and value != 1 and value != 2:
                obj[key] = 2
        return obj