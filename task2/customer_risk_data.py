from solution.established import FaceToFaceEstablished
from solution.industry_risk import IndustryRiskCalculator
from solution.country_risk import CountryRiskAssessment
from solution.length_of_relationship import RelationshipLengthCalculator

class CustomerRiskData:
    def calculate_risk(self):
        # Create an instance of the class
        risk_calculator = IndustryRiskCalculator()
        # Call the method
        risk_dict = risk_calculator.calculate_risk()

        # Create an instance of the class
        face_to_face_established = FaceToFaceEstablished()
        # Call the method
        face_to_face_data = face_to_face_established()

        # Create an instance of the class
        country_risk_assessment = CountryRiskAssessment()
        # Call the method
        country_risk_assessment.assess_risk()

        # Create an instance of the class
        relationship_length_calculator = RelationshipLengthCalculator()
        # Call the method
        relationship_length = relationship_length_calculator()

        # Get all the keys from the dictionaries
        all_keys = set(risk_dict.keys()).union(face_to_face_data.keys()).union(country_risk_assessment.country_risk_category.keys()).union(relationship_length.keys())

        # Create a dictionary to store the final result
        final_result = {}
        for key in all_keys:
            final_result[key] = [risk_dict.get(key, 0), face_to_face_data.get(key, 0), country_risk_assessment.country_risk_category.get(key, 0), relationship_length.get(key, 0)]

        return final_result
    
# Write this data to a CSV file
customer_risk_data = CustomerRiskData().calculate_risk()
import csv
with open('task2/customer_risk_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['CustomerID', 'IndustryRisk', 'FaceToFaceEstablished', 'CountryRisk', 'RelationshipLength'])
    for key, value in customer_risk_data.items():
        writer.writerow([key, value[0], value[1], value[2], value[3]])