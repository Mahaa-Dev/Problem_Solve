import os

try:
    # Open the input file for reading
    with open("input.txt", "r") as file:
        # Read the contents of the file into a list
        words = file.readlines()
    # Strip newline characters from the words
    words = [word.strip() for word in words]
    # Sort the list of words alphabetically
    words.sort()
    # Open the output file for writing
    with open("output.txt", "w") as file:
        # Write the sorted words to the output file
        for word in words:
            file.write(word + os.linesep)
    print("File written successfully!")
except IOError as e:
    print("An error occurred:", e)
