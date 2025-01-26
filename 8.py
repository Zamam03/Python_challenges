def filter_words(dictionary, guess, feedback):
    banned = list()
    for i, (letter, outcome) in enumerate(zip(guess, feedback)):
        if outcome == '.':
            # no letter in the word
            banned.extend([x for x in dictionary if letter in x])
        elif 'a' <= outcome <= 'z':
            # letter present, but not in current place
            banned.extend([x for x in dictionary if letter not in x])
            banned.extend([x for x in dictionary if x[i] == letter])
        else:
            # letter present in current place
            banned.extend([x for x in dictionary if x[i] != letter])

    new_dict = list()
    banned = set(banned)
    for word in dictionary:
        if word not in banned:
            new_dict.append(word)
    return new_dict


dictionary = list()
word = input()
while word != '###':
    dictionary.append(word)
    word = input()

n_guesses = int(input())
current = dictionary
for i in range(n_guesses):
    guess = input()
    feedback = input()
    current = filter_words(current, guess, feedback)

current.sort()
for word in current:
    print(word)
