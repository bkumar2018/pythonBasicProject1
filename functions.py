#Defining functions 


def fib(n):
    """ Print a Fibonacci series upto n. """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(10)
fib(100)
fib(1000)

#write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:

def fib2(n):
    """ Return a Fibonacci series upto n. """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f10 = fib2(10)
print(f10)

f100 = fib2(100)
print(f100)

f1000 = fib2(1000)
print(f1000)
