import csv

# Initialize variables
total_salary = 0
employee_count = 0

# Open the CSV file
with open("employees.csv", "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Iterate through each row
    for row in reader:
        try:
            # Get the salary value
            salary = int(row[2])
            # Add the salary to the total
            total_salary += salary
            # Increment the employee count
            employee_count += 1
        except ValueError:
            # Handle invalid salary value
            print(f"Invalid salary value for {row[0]}")
        except IndexError:
            # Handle missing salary value
            print(f"Missing salary value for {row[0]}")

# Calculate the average salary
if employee_count > 0:
    average_salary = total_salary / employee_count
    print(f"The average salary is ${average_salary:.2f}")
else:
    print("No valid salary data found.")
