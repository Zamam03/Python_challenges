target = input()
guess = input()

for i in range(len(target)):
    if target[i] == guess[i]:
        print(guess[i], end='', sep='')
    elif guess[i] in target:
        lower = chr(ord(guess[i]) + 32)
        print(lower, end='', sep='')
    else:
        print('.', end='', sep='')
print()
