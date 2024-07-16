from file_operations import read_file, write_to_file, append_to_file

# Test file operations
file_name = "test.txt"

# Write data to file
write_to_file(file_name, "Hello, this is a test file.")
print(read_file(file_name))  # Output: Hello, this is a test file.

# Append data to file
append_to_file(file_name, "This is the second line.")
print(read_file(file_name))
# Output:
# Hello, this is a test file.
# This is the second line.
