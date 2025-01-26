target = input()
guess = input()

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

print(''.join(masked))

