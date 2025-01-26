a = int(input())
b = int(input())
x = 0
old_x = 1
y = 1
old_y = 0
r = b
old_r = a
while r != 0:
	quotient = old_r // r
	temp = r
	r = old_r - (quotient * temp)
	old_r = temp
	temp = x
	x = old_x - (quotient * temp)
	old_x = temp
	temp = y
	y = old_y - (quotient * temp)
	old_y = temp
print(old_r)
print(old_x)
print(old_y)