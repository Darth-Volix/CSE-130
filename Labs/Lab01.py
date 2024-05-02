# 1. Name: 
#    Nicholas Wilkins
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program will have the user guess a number between 1 and whatever positive whole 
#    integer the user chooses, store their guesses, check if the guess is correct, 
#    display the results, and loop until the right number is guessed.
# 4. What was the hardest part? Be as specific as possible.
#    The sytax of the Python script was not the hardest part for me at all as I am very familiar
#    with the sytnax, it was remembering how to structure some of the code and check for conditions.
#    I usually have to shake off some rust at the beginning of every semester. I found the program
#    itself to be a very simple one and easy to solve, the hard part was working with the template 
#    and writing my code around the comments that help create the structure of the program. I am 
#    used to having to do that myself and it is easier for me if I do on these more sumple programs.
#    There were no difficult bugs for me in this program, and the only difficulties I had with with 
#    the instructions was some of the new terminology used and creating a video demonstration of the 
#    program.
# 5. How long did it take for you to complete the assignment?
#    It took roughly 2 hours for me to complete this assignment, a good portion of it was figuring out 
#    how to do the video demonstration. 

import random

# Game introduction.
print()
print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')
print()
# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = 0
while value_max < 1:
    value_max = int(input('Pick a positive whole integer greater than 0: '))
    if value_max < 0:
        print('The number you have selected is less than 1, please try again!')    
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)
# Give the user instructions as to what he or she will be doing.
print(f'Guess a number between 1 and {value_max}.')
# Initialize the sentinal and the array of guesses.
guess_list = []
guess_count = 0
user_guess = None
# Play the guessing game.
while user_guess != value_random:
    # Prompt the user for a number.
    guess_count += 1
    user_guess = int(input('> '))
    # Store the number in an array so it can be displayed later.
    guess_list.append(user_guess)
    # Make a decision: was the guess too high, too low, or just right.
    if user_guess < value_random:
        print('         Too low!')
    elif user_guess > value_random:
        print('         Too high!')
# Give the user a report: How many guesses and what the guesses where.
print(f'You were able to find the number in {guess_count} guesses.')
print(f'The numbers you guessed were: {guess_list}')
print()