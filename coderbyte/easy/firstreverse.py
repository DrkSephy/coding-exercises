# Challenge:
# Have the function FirstReverse(str) take the str parameter 
# being passed and return the string in reversed order. 

def FirstReverse(str): 
	return ''.join(reversed(str))

print FirstReverse(raw_input()) 