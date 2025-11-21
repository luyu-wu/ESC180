from math import pi

digit = 0
def next_digit_pi():
	global digit
	num = pi
	for i in range(digit):
		num = 10*(num-int(num))
	digit += 1
	return int(num)

print (next_digit_pi())
print (next_digit_pi())
print (next_digit_pi())


