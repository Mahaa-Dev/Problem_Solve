# Prompt user for file name
file_name = input("Enter the file name: ")

# Prompt user for word to search for
word_to_search = input("Enter the word to search for: ")

# Initialize count to 0
count = 0

# Open the file in read mode
with open(file_name, "r") as file:
    # Read all the lines of the file
    lines = file.readlines()
    # Iterate through each line
    for line in lines:
        # Split the line into words
        words = line.split()
        # Iterate through each word
        for word in words:
            # Compare the word with the word to search for
            if word == word_to_search:
                # If match found, increment the count
                count += 1

# Print the count
print(f"The word '{word_to_search}' occurred {count} times in the file.")
