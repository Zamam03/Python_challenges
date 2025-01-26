
def is_triangular(N):
	for k in range(N+1):
		t = (k * (k+1)) // 2
		if t == N:
			return True
		elif t > N:
			return False
	return False


N = int(input())
while N != -1:
	if is_triangular(N):
		print("True")
	else:
		print("False")
	N = int(input())
