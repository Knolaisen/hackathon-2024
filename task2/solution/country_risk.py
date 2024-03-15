import pandas as pd

class CountryRiskAssessment:
    def __init__(self):
        self.company_customers = pd.read_csv('task1/CompanyCustomers.csv')
        self.private_customers = pd.read_csv('task1/PrivateCustomers.csv')
        self.country_risk = pd.read_csv('task2/Country Risk.csv')
        self.industry_risk = pd.read_csv('task2/Industry Risk.csv', encoding='ISO-8859-1')
        self.country_risk_assessment = {}
        self.country_risk_category = {}
        self.low_risk = 0
        self.medium_risk = 0
        self.high_risk = 0

    def assess_risk(self):
        for i in range(len(self.company_customers)):
            country = self.company_customers['Country'][i]
            for j in range(len(self.country_risk)):
                if self.country_risk['Country'][j] == country.upper():
                    risk = self.country_risk['coface_country_risk_assessment'][j]
                    self.country_risk_assessment[self.company_customers['CustomerID'][i]] = risk

        for i in range(len(self.private_customers)):
            country = self.private_customers['Country'][i]
            for j in range(len(self.country_risk)):
                if self.country_risk['Country'][j] == country.upper():
                    risk = self.country_risk['coface_country_risk_assessment'][j]
                    self.country_risk_assessment[self.private_customers['CustomerID'][i]] = risk

        unique_risk = self.country_risk['coface_country_risk_assessment'].unique()

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

        country_risk_assessment_score = {}

        for key, value in self.country_risk_assessment.items():
            country_risk_assessment_score[key] = risk_score[value]

        for key, value in country_risk_assessment_score.items():
            if value < 5:
                self.country_risk_category[key] = "Low"
            elif value >= 5 and value <= 7:
                self.country_risk_category[key] = "Medium"
            else:
                self.country_risk_category[key] = "High"

        # Convert the risk category to values 0, 1 or 2
        for key, value in self.country_risk_category.items():
            if value == 'Low':
                self.country_risk_category[key] = 0
                self.low_risk += 1
            elif value == 'Medium':
                self.country_risk_category[key] = 1
                self.medium_risk += 1
            else:
                self.country_risk_category[key] = 2
                self.high_risk += 1

        return self.country_risk_category
