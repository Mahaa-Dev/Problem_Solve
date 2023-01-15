import random

#list of words
words = ["python","programming","computer","science","code"]

#randomly select a word from the list
word = random.choice(words)

#initialize variables
guessed_letters = []
remaining_guesses = 6
display_word = ["_"] * len(word)

#game loop
while remaining_guesses > 0:
    #get player's guess
    guess = input("Guess a letter: ").lower()
    #check if the guess has already been made
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    #add the guess to the list of guessed letters
    guessed_letters.append(guess)
    #check if the guess is in the word
    if guess in word:
        #update the display word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        #check if the player has won
        if "_" not in display_word:
            print("Congratulations! You won!")
            print("The word was: " + "".join(display_word))
            break
    else:
        #decrement remaining guesses
        remaining_guesses -= 1
        #display the hangman
        print("Incorrect. You have {} guesses remaining.".format(remaining_guesses))
    #display the current state of the game
    print(" ".join(display_word))

#end game message
if remaining_guesses == 0:
    print("Sorry, you lost. The word was: " + word)
