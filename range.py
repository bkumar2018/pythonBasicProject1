#Range function

for i in range(5):
    print(i)

#using len()
a = ['Mary', 'had', 'a', 'little', 'lamp']
for i in range(len(a)):
    print(i, a[i])

#break and continue
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')



for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found an odd number', num)