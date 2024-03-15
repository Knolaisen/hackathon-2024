import csv

filenames = ["task1\Company Customers.csv", "task1\Private Customers.csv"]
column_index = 14  # 15th column (0-based index)
no = 0

for filename in filenames:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index and row[column_index] == "No":
                no += 1

print("Total count of 'no' in the 15th column:", no)