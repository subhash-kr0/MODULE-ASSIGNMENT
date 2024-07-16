# file_operations.py

def read_file(file_name):
    """
    Function to read data from a file.
    
    Parameters:
    file_name (str): The name of the file to read from.
    
    Returns:
    str: Contents of the file as a string.
    """
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def write_to_file(file_name, data):
    """
    Function to write data to a file. Creates a new file if it doesn't exist.
    
    Parameters:
    file_name (str): The name of the file to write to.
    data (str): The data to write into the file.
    
    Returns:
    str: Confirmation message after writing to the file.
    """
    with open(file_name, 'w') as file:
        file.write(data)
    return f"Data written to '{file_name}' successfully."

def append_to_file(file_name, data):
    """
    Function to append data to an existing file or create a new file if it doesn't exist.
    
    Parameters:
    file_name (str): The name of the file to append to.
    data (str): The data to append into the file.
    
    Returns:
    str: Confirmation message after appending to the file.
    """
    with open(file_name, 'a') as file:
        file.write(data + "\n")
    return f"Data appended to '{file_name}' successfully."

# Additional file operations functions can be added as needed

