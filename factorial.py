


def factorial(n):
	return 1 if( n == 1 or n == 0) else n*factorial(n-1)

fact = input("Enter a number to calculate it factorial: ")
num = int(fact)
print(factorial(num))

