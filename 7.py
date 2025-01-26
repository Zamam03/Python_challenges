def read_dictionary():
    """
    Read in the dictionary from standard input and return it as a list
    :return: the dictionary
    """
    dictionary = list()
    word = input()
    while word != '###':
        dictionary.append(word)
        word = input()
    return dictionary


def compute_response(target, guess):
    """
    Given the hidden word and a guess, return a string representing whether the letters are correct (and in the correct
    place)
    :param target: the hidden word
    :param guess: the guess the user has just made
    :return: a string indicating how correct they are (see Task 6)
    """
    masked = ['.'] * len(target)
    target = [x for x in target]
    for i, (x, y) in enumerate(zip(guess, target)):
        if x == y:
            masked[i] = x
            target[i] = '.'
    for i, x in enumerate(guess):
        if x in target:
            if masked[i] == '.':
                masked[i] = x.lower()
            target[target.index(x)] = '.'

    return ''.join(masked)

def is_valid(guess, dictionary):
    """
    Given a guess by the user and the dictionary, determine whether the guess is a valid one to make (see Task 2)
    :param guess: the user's guess
    :param dictionary: a list of all words in the dictionary
    :return: True if the guess is valid; otherwise, return False
    """
    return guess in dictionary

"""
DO NOT MODIFY ANY CODE BELOW THIS LINE
"""

import random

dictionary = read_dictionary()

rng = random.Random(0)

while True:

    choice = input("Play a game? (Y/N): ")
    if choice == 'N':
        break

    target = dictionary[rng.randint(0, len(dictionary) - 1)]
    turns = 0
    MAX_TURNS = 6
    while True:
        if turns == MAX_TURNS:
            print("Game over! :(")
            print('The word was: {}'.format(target))
            break
        else:
            guess = input()
            while not is_valid(guess, dictionary):
                print('{} is not a valid word!'.format(guess))
                guess = input()

            print("You guessed: {}".format(guess))
            response = compute_response(target, guess)
            print('Response: {}'.format(response))
            if response == guess:
                # we won!
                print("You win! :)")
                break
        turns += 1
