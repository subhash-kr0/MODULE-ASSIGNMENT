def count_word_occurrences(file_name):
    """
    Function to read a text file, count occurrences of each word, and display results alphabetically.
    
    Parameters:
    file_name (str): Name of the text file to read.
    """
    word_count = {}
    
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            
            # Tokenize the content into words (split by whitespace and punctuation)
            words = content.split()
            
            # Count occurrences of each word
            for word in words:
                # Remove punctuation and convert to lowercase for consistency
                clean_word = word.strip().strip('.,?!').lower()
                
                if clean_word:
                    if clean_word in word_count:
                        word_count[clean_word] += 1
                    else:
                        word_count[clean_word] = 1
        
        # Display word counts in alphabetical order
        print("Word counts (alphabetical order):")
        for word in sorted(word_count.keys()):
            print(f"{word}: {word_count[word]}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# File name containing the paragraph to read
file_name = "paragraph.txt"

# Call the function to count word occurrences and display results
count_word_occurrences(file_name)
