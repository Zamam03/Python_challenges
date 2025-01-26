def is_palindrome(line):
	keep = list()
	for x in line:
		x = x.lower()
		if 'a' <= x <= 'z':
			keep.append(x)
	line = ''.join(keep)
	line2 = ''.join(reversed(keep))
	return line == line2
	


N = int(input())
for i in range(N):
	line = input()
	if is_palindrome(line):
		print("True")
	else:
		print("False")
		


