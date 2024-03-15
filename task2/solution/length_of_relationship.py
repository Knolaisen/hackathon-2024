from datetime import datetime
from dateutil.parser import parse
from itertools import chain
import pandas as pd

class RelationshipLengthCalculator:
    def __call__(self):
        # Load data
        company_customers = pd.read_csv('task1/CompanyCustomers.csv', encoding='ISO-8859-1')
        private_customers = pd.read_csv('task1/PrivateCustomers.csv', encoding='ISO-8859-1')

        # Length of customer relationship in seconds
        relationship_length: dict[int, float] = {}
        for i, customer in chain(company_customers.iterrows(), private_customers.iterrows()):
            relationship_length[customer["CustomerID"]] = (
                datetime.now() - parse(customer["CustomerEstablishmentDate"]))
            # Convert to years
            relationship_length[customer["CustomerID"]] = relationship_length[customer["CustomerID"]].days / 365.25

        return relationship_length