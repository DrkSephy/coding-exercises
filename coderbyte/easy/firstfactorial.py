# Challenge:

# Implement the FirstFactorial function such that it returns 
# the factorial of the given input

def FirstFactorial(num): 
	result = 1
	for i in range(1, num):
		result *= i
	return result
    

print FirstFactorial(5) 