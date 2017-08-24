"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contains any char.
"""
def XO(str):
	str.lower()
	is_same=True
	number_x=0
	number_o=0
	for i in str:
		if i=="x":
			number_x += 1
		elif i=="o":
			number_o += 1
	if number_o==number_x:
		return True
	else:
		return False

print(XO("xxcono"))
