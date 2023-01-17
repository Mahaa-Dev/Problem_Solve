# listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # x = listA.pop(3)
# # print(listA,x)
# list2 = [i for i in listA if i % 2 == 0]
# print(list2)
#a = range(50)
# print(a)
#
# Initialize an empty dictionary
# word_freq = {}

# # Take input from the user
# text = input("Enter the text to analyze: ")

# # Convert the string to a list of words
# words = text.split()

# # Iterate through the list of words
# for word in words:
#     # Check if the word is already in the dictionary
#     if word in word_freq:
#         # Increment the frequency count by 1
#         word_freq[word] += 1
#     else:
#         # Add the word to the dictionary with a frequency count of 1
#         word_freq[word] = 1

# # Print the dictionary
# print(word_freq)


def word_frequency():
    freq = {}
    text = input("Enter a string")
    words = text.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    for key, value in freq.items():
        print(key, value)


word_frequency()
