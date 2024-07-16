# string_utils.py

def reverse_string(input_string):
    """
    Function to reverse a given input string.
    
    Parameters:
    input_string (str): The string to be reversed.
    
    Returns:
    str: Reversed string.
    """
    return input_string[::-1]

def capitalize_string(input_string):
    """
    Function to capitalize the first letter of each word in a given input string.
    
    Parameters:
    input_string (str): The string to be capitalized.
    
    Returns:
    str: Capitalized string.
    """
    return ' '.join(word.capitalize() for word in input_string.split())

# Additional string manipulation functions can be added as needed
