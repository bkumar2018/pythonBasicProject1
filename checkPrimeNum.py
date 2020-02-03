

def chkPrime(num):
    if num <= 0 or num == 1:
        print ("You have entered 0 or less then 0 or 1, please enter other then this number. ")
    elif num > 1:
        if num%2 == 0:
            print(f'The number {num} you entered is prime number.')
        else:
            print(f'The number {num} you entered is Not prime number.')


userInput = input("Enter a number to check for prime no: ")
num = int(userInput)
chkPrime(num)
