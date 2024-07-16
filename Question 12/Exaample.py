from calculator import add, subtract, multiply, divide

# Perform calculations
print("Addition:", add(5, 3))  # Output: 8
print("Subtraction:", subtract(5, 3))  # Output: 2
print("Multiplication:", multiply(5, 3))  # Output: 15
print("Division:", divide(5, 3))  # Output: 1.6666666666666667

# Handling division by zero
try:
    result = divide(5, 0)
except ZeroDivisionError as e:
    print("Error:", e)  # Output: Error: Division by zero is not allowed.
