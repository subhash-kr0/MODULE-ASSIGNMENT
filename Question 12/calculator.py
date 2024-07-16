# calculator.py

def add(x, y):
    """
    Function to add two numbers.
    
    Parameters:
    x (float or int): First number.
    y (float or int): Second number.
    
    Returns:
    float or int: Sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Function to subtract two numbers.
    
    Parameters:
    x (float or int): First number.
    y (float or int): Second number.
    
    Returns:
    float or int: Difference of x and y (x - y).
    """
    return x - y

def multiply(x, y):
    """
    Function to multiply two numbers.
    
    Parameters:
    x (float or int): First number.
    y (float or int): Second number.
    
    Returns:
    float or int: Product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Function to divide two numbers.
    
    Parameters:
    x (float or int): Numerator.
    y (float or int): Denominator.
    
    Returns:
    float: Result of division (x / y).
    
    Raises:
    ZeroDivisionError: If y is 0.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y
