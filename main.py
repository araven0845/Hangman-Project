import random
import hangman_art
from hangman_art import stages
from hangman_art import logo
from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)




# print welcome logo and explain rules of game
print(hangman_art.logo)

print ("Hello! Welcome to Hangman!\nHere's how to play:")
print ("Guess a letter. If it is in the word, you keep going!\nIf not, you lose a life and try again.")
print ("Once you either guess the word or run out of lives, the game is over!")

# Initialize variables and list
lives = 6
word_list = []
correct_letters = []
guessed_letters = []
game_over = False

# move all the words from web2lowerset file to word_list
for i in range(len(web2lowerset)):
    word_list.append(web2lowerset.pop())

# Choose a random word, and begin game
chosen_word = random.choice(word_list)
print("Word has " + str(len(chosen_word)) + " letters.")
placeholder = ""
word_length = len(chosen_word)

# Create blanks for each letter in the word
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


# Create loop for game function
while not game_over:
    valid_guess = False
    print(hangman_art.stages[lives])
    print(f"{lives} LIVES LEFT")
    guess = input("Guess a letter: ").lower()

    # Takes input until the letter guessed is valid
    while (not guess.isalpha() or len(guess) != 1):
        print("You did not guess a valid letter, please try again!")
        guess = input("Guess a letter: ").lower()
    valid_guess = True

    # If this letter has not been guessed before, add to guessed_letters list
    if (guess not in guessed_letters):
        guessed_letters.append(guess)

    # If the letter has been guessed, take input until a valid new letter is inputted
    elif (guess in guessed_letters):
        valid_guess = False
        while (valid_guess is False):
            print(f"You have already guessed '{guess}'!, please enter a valid letter")
            guess = input("Guess a letter: ").lower()
            if (guess not in guessed_letters):
                valid_guess = True
                guessed_letters.append(guess)

    #initialize display (_ for unguessed letters, or the actual letter when properly guessed
    display = ""

    # If guessed letter in word, update display and add to correct letters
    # list. else if not the guess, but in the word, add the letter to display. else put a _
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    # If guess is not in the word, let the user know, and decrement # of lives.
    if (guess not in chosen_word):
        print ("You guessed " + str(guess) + ". That isnt in the word. You lose a life")
        lives -= 1

        # If no lives left, end game and output the word
        if lives == 0:
            game_over = True

            print("YOU LOSE")
            print("The word was: " + chosen_word)
            
    # Output the letters that have been guessed so far
    print("Letters guessed: ")
    print(guessed_letters)

    if "_" not in display:
        game_over = True
        print("YOU WIN")

