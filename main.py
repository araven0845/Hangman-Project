import random
import hangman_art
from hangman_art import stages
from hangman_art import logo
from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)


#biggerst word is 28 letters
# 3-8 easy
# 8-15 medium
#15-20 hard
#21-28 expert
# Initialize variables and lists
lives = 6
word_list = []
for i in range(len(web2lowerset)):
    word_list.append(web2lowerset.pop())


print(hangman_art.logo)

print ("Hello! Welcome to Hangman!\nHere's how to play:")
print ("Guess a letter. If it is in the word, you keep going!\nIf not, you lose a life and try again.")
print ("Once you either guess the word or run out of lives, the game is over!")


chosen_word = random.choice(word_list)
print("Word has " + str(len(chosen_word)) + " letters.")
placeholder = ""
word_length = len(chosen_word)

# Create blanks for each letter in the word
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False

correct_letters = []
guessed_letters = []
while not game_over:
    valid_guess = False
    print(hangman_art.stages[lives])
    print(f"{lives} LIVES LEFT")
    guess = input("Guess a letter: ").lower()
    while (not guess.isalpha() or len(guess) != 1):
        print("You did not guess a valid letter, please try again!")
        guess = input("Guess a letter: ").lower()
    valid_guess = True
    if (guess not in guessed_letters):
        guessed_letters.append(guess)
    elif (guess in guessed_letters):
        valid_guess = False
        while (valid_guess is False):
            print(f"You have already guessed '{guess}'!, please enter a valid letter")
            guess = input("Guess a letter: ").lower()
            if (guess not in guessed_letters):
                valid_guess = True
                guessed_letters.append(guess)


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if (guess not in chosen_word):
        print ("You guessed " + str(guess) + ". That isnt in the word. You lose a life")
    print ("Letters guessed: ")
    print(guessed_letters)

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print("YOU LOSE")
            print("The word was: " + chosen_word)

    if "_" not in display:
        game_over = True
        print("YOU WIN")

