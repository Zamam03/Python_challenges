def is_harshad(x):
	sum = 0
	for c in str(x):
	    sum += ord(c) - ord('0')
	return x % sum == 0


N = int(input())
for i in range(N):
	x = int(input())
	if is_harshad(x):
		print("True")
	else:
		print("False")
		


