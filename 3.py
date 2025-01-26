
target = input()
guess = input()
matches = 0
for i in range(len(target)):
    if target[i] == guess[i]:
        matches += 1
print(matches)

