#EXERCISE 3
#Takes n as input, returns its factorial
def fatt(n):
	if (n == 0) or (n == 1):
		return n
	else:
		return n * fatt(n - 1)
