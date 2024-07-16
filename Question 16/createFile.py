def write_employee_details(file_name):
    """
    Function to write employee details to a text file.
    
    Parameters:
    file_name (str): Name of the text file to create or write into.
    """
    # Employee details
    employees = [
        {"name": "John Doe", "age": 30, "salary": 50000},
        {"name": "Jane Smith", "age": 28, "salary": 45000},
        {"name": "Michael Johnson", "age": 35, "salary": 60000},
        {"name": "Emily Davis", "age": 32, "salary": 55000}
    ]
    
    # Open the file in write mode ('w')
    with open(file_name, 'w') as file:
        for employee in employees:
            # Write each employee's details as a line in the file
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: ${employee['salary']}\n")

    print(f"Employee details have been written to '{file_name}' successfully.")

# File name to create/write into
file_name = "employees.txt"

# Call the function to write employee details to the file
write_employee_details(file_name)
