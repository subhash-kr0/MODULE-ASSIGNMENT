def calculate_total_expenses(file_name):
    """
    Function to read a text file containing expenses and calculate the total amount spent.
    
    Parameters:
    file_name (str): Name of the text file to read.
    
    Returns:
    float: Total amount spent on expenses.
    """
    total_spent = 0.0
    
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read each line in the file
            for line in file:
                # Split the line by ':' to separate expense name and amount
                parts = line.strip().split(':')
                if len(parts) == 2:
                    try:
                        amount = float(parts[1].strip())
                        total_spent += amount
                    except ValueError:
                        print(f"Ignoring line '{line.strip()}': Invalid amount format")
                else:
                    print(f"Ignoring line '{line.strip()}': Invalid format")
        
        return total_spent
    
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

# File name containing expenses to read
file_name = "expenses.txt"

# Calculate the total expenses and display the result
total_expenses = calculate_total_expenses(file_name)
if total_expenses is not None:
    print(f"Total amount spent on expenses: ${total_expenses:.2f}")
