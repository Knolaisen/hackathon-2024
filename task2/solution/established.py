import pandas as pd
import pandas as pd

class FaceToFaceEstablished:
    def __call__(self):

        # Read the data from the CSV files that lie next to this script using the path "task1/CompanyCustomers.csv"
        company_customers = pd.read_csv('task1/CompanyCustomers.csv')
        private_customers = pd.read_csv('task1/PrivateCustomers.csv')

        face_to_face = {}
        for i in range(len(company_customers)):
            face_to_face[company_customers['CustomerID'][i]] = company_customers['Face_to_Face_Establishment'][i]

        for i in range(len(private_customers)):
            face_to_face[private_customers['CustomerID'][i]] = private_customers['Face_to_Face_Establishment'][i]

        # Convert the face_to_face_established to 0 or 1
        face_to_face_established = {}
        for key, value in face_to_face.items():
            if value == 'Yes':
                face_to_face_established[key] = 1
            else:
                face_to_face_established[key] = 0

        return face_to_face_established
