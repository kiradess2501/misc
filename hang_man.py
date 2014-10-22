"""
Hangman game by Matthew Warren
Created by following guide at: http://inventwithpython.com/chapter9.html
Converted to Python 2.7 with a few minor changes including: colors, cosmetic
fixes, extra animal names, and extra documentation/comments.
Last updated Oct 20, 2014
"""

import random


def get_random_word(word_list):
    """
    Return a random word out of a list of words.

    Keyword arguments:
    word_list -- list of words

    Returns: string
    """
    return random.choice(word_list)


def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    """
    Draw the game board to the screen. Clear the screen, then show the
    appropriate hangman image for the current state of the game, as well as
    number of letters in the word, missed guesses, and correct guesses.

    Keyword arguments:
    hangman_pics -- list containing all possible images to be drawn
    missed_letters -- string composed of all incorrect letter guesses so far
    correct_letters -- string composed of all correctly guesses letters so far
    secret_word -- string: randomly selected word to be guessed

    Returns: None
    """
    print chr(27) + "[2J" # escape sequence to clear screen

    print hangman_pics[len(missed_letters)] # draws appropriate hangman img
    print ""

    print " Missed letters: ",
    for letter in missed_letters: # print out all missed guesses so far
        print ("%c " % letter), # on the same line
    print ""
    print ""

    blanks = ('_' * len(secret_word)) # a '_' for every letter in secret_word

    for i in range(len(secret_word)): # replace blanks with current
        if secret_word[i] in correct_letters: # correctly guessed letters
            blanks = blanks[:i] + secret_word[i] + blanks[(i + 1):]

    print ' ',
    for letter in blanks: # print those to screen, seperated by ' 's
        print (str(letter) + ' '),
    print ""
    print ""


def get_guess(already_guessed):
    """
    Return the letter that the player entered. This function makes sure the
    player entered a single letter, and not something else.

    Keyword arguments:
    already_guessed -- string: (missed_letters + correct_letters)

    Returns: Char, lowercase and in the alphabet (a-z)
    """
    while True: # continue until correct input received
        print " Guess a letter."
        guess = (raw_input("> ")).lower()

        if len(guess) != 1: # check that it is a single character
            display_board(hangman_pics, missed_letters, correct_letters, \
            secret_word) # refreshing display here keeps graphic visible...
            # display in red
            print " %c[31mPlease enter a single letter." % chr(27),
            # then reset color mode
            print "%c[0m" % chr(27)
        elif guess in already_guessed: # in missed_letters or correct_letters
            display_board(hangman_pics, missed_letters, correct_letters, \
            secret_word) # otherwise, repeatedly inputting wrong inputs...
            print " %c[31mYou have already guessed that letter." % chr(27),
            print "%c[31mChoose again." % chr(27),
            print "%c[0m" % chr(27)
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            display_board(hangman_pics, missed_letters, correct_letters, \
            secret_word) # will push it up off the screen
            print " %c[31mPlease enter a letter." % chr(27),
            print "%c[0m" % chr(27)
        else:
            return guess


def play_again():
    """
    Check if player wants to play again or not. Return True if inputted char or
    string begins with 'Y' or 'y'.

    Keyword arguments: none

    Returns: Boolean
    """
    print " Do you want to play again? (yes or no)"
    return (raw_input("> ")).lower().startswith('y')


###############################################################################

hangman_pics = ["""
 H A N G M A N


   +---+
   |   |
       |
       |
       |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
       |
       |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
   |   |
       |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
  /|   |
       |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
  /|\  |
       |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
 =========""", """
 H A N G M A N


   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
 ========="""]

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar " +\
"coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk " +\
"lion lizard llama mole monkey moose mouse mule newt otter owl panda " +\
"parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep " +\
"skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel " +\
"whale wolf wombat zebra"

extra_words = "alpaca antelope baboon badger cheetah crab dolphin dove " +\
"eel elephant falcon fish gorilla giraffe hamster heron ibex ibis jackal " +\
"jaguar kangaroo koala leopard lobster manatee meerkat narwhal octopus " +\
"ostrich panther pelican quail quetzal racoon reindeer seahorse shrew " +\
"termite viper vulture wallaby walrus yak"

word_list = words.split() + extra_words.split()

###############################################################################

missed_letters = ""
correct_letters = ""
secret_word = get_random_word(word_list) # pick word to be guessed
game_is_done = False

while True:
    display_board(hangman_pics, missed_letters, correct_letters, secret_word)

    # let the player type in a letter
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word: # if correct guess
        correct_letters = correct_letters + guess # add it

        # check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break;
        if found_all_letters:
            display_board(hangman_pics, missed_letters, correct_letters, \
            secret_word)
            print " %c[32mThat's right!" % chr(27),
            print "%c[32mThe secret word was \"%s\"!" % (chr(27), secret_word),
            print "%c[32mYou win!%c[0m" % (chr(27), chr(27))
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # check if the player has guessed too many times and lost
        if len(missed_letters) == len(hangman_pics) - 1:
            display_board(hangman_pics, missed_letters, correct_letters, \
            secret_word)
            print " You have run out of guesses!"
            print " You had %d missed guesses and %d correct guesses" % \
            (len(missed_letters), len(correct_letters))
            print " The word was %s." % secret_word
            game_is_done = True

    # if game is over, ask the player if they want to play again
    if game_is_done:
        if play_again(): # reset everything and continue while loop
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word = get_random_word(word_list) # new word
        else:
            break; # break while loop, go to end of program
