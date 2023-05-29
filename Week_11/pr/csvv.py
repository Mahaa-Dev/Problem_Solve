import csv

# Sample data
data = [["Name", "Age", "Salary"],
        ["John Smith", "35", "50000"],
        ["Jane Doe", "28", "60000"],
        ["Bob Johnson", "42", "75000"]]

# Open a new file in write mode
with open("employees.csv", "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the data to the file
    writer.writerows(data)

print("CSV file created successfully!")
