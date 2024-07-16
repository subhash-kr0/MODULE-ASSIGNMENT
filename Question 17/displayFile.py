def display_file_contents(file_name):
    """
    Function to open and display contents of a text file line by line.
    
    Parameters:
    file_name (str): Name of the text file to open and read.
    """
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read and display each line in the file
            print(f"Contents of '{file_name}':")
            for line in file:
                print(line.strip())  # Strip to remove newline characters
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# File name to open and display
file_name = "inventory.txt"

# Call the function to display contents of the file
display_file_contents(file_name)
