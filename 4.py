
target = input()
guess = input()
exact_matches = 0
inexact_matches = 0
for i in range(len(target)):
    if target[i] == guess[i]:
        exact_matches += 1
    elif guess[i] in target:
        inexact_matches += 1
print(exact_matches)
print(inexact_matches)

