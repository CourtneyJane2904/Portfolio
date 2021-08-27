"""
TM112 21D TMA03 Q2 starter code
TM112 Module Team 17/12/2020
"""

from random import *


def show_flashcard():
    """ 
    	pulls two random keys and a list of keys from a dictionary named glossary and uses them to guide the user through a guessing game
    	The user must guess which of two definitions corresponds to random_key1 and are told off their success or failure promptly
    	Uses the random module
    """

    # Get glossary keys.
    keys = list(glossary)

    # Choose two random glossary keys.
    random_key1 = choice(keys)
    random_key2 = choice(keys)
    # Keep checking random_key2 until
    # it is different from random_key1
    while random_key2 == random_key1:
      random_key2 = choice(keys)  

    # Display random glossary key.
    print('Here is a glossary entry:', random_key1)

    correct_def = choice(['1', '2'])

    answers = {} ; ans_arr = []

    # show definitions in order according to value of correct_def and append values to array in same order

    # Choose a random order to display the definitions in
    # '2' means the correct definition
    # should printed second.
    if correct_def == '2':
    	print (glossary[random_key2], glossary[random_key1])
    	ans_arr.append(glossary[random_key2])
    	ans_arr.append(glossary[random_key1])
    # '1' means the correct definition
    #  should be printed first.
    else:
    	print (glossary[random_key1], glossary[random_key2])
    	ans_arr.append(glossary[random_key1]) 
    	ans_arr.append(glossary[random_key2])

    # a dictionary segregating the correct definition from the incorrect
    answers = {"correct":glossary[random_key1],"incorrect":glossary[random_key2]}

    # as ans_arr will have two elements with indexes 0 and 1 by default, we have to minus 1 from the guessed index value
    # guesses are based on an index starting from 1
    l = 1
    while l == 1:
	    try:
	    	guess = int(input("Do you believe definition 1 or definition 2 was correct?"))
	    	if guess > 0:	guessed_def = ans_arr[guess-1]
	    	else:	raise Exception()
	    	l = 0
	    except:
	    	print("Please guess the first definition by typing 1 or the second by typing 2.")
	    
    # if the correct definition was the value of guessed_def, tell the user they were correct
    # else they were wrong
    if answers["correct"] == guessed_def:	print("You were correct! :)")
    else:	print("Nope. :c")


# DO NOT CHANGE ANYTHING IN THE NEXT SECTION    

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
                       
