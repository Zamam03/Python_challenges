dictionary = list()
word = input()
while word != '###':
    dictionary.append(word)
    word = input()
word = input()
if word in dictionary:
    print("Valid")
else:
    print("Invalid")
