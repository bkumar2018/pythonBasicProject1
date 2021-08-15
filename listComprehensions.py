nums = [1,2,3,4,5,6,7,8,9,10]


# I want 'n' for each 'n' in nums
# myList = []
# for n in nums:
#     myList.append(n)
# print(myList)

#List comprehension
# myList = [ n for n in nums]
# print(myList)


# I want 'n*n' for each 'n' in nums
# myList = []
# for n in nums:
#     myList.append(n*n)
# print(myList)

#List comprehension
# myList = [ n*n for n in nums]
# print(myList)

#Using Map and lambda
# myList = map(lambda n: n*n, nums)
# print(list(myList))


# I want 'n' for each 'n' in nums if 'n' is even
# myList = []
# for n in nums:
#     if n%2 == 0:
#         myList.append(n)
# print(myList)

#using comprehension
# myList = [n for n in nums if n%2 == 0]
# print(myList)

#Using the filter + lambda
# myList = filter(lambda n: n%2 ==0, nums)
# print(list(myList))


# I want a (letter, num) pair of each letter in 'abcd' and each number in '0123'
# myList = []
# for letter in 'abcd':
#     for num in range(4):
#         myList.append((letter, num))
# print(myList)

#list comprehension
# myList = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(myList)


#Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# print(list(zip(names,heros)))

# myDict = {}
# for name, hero in zip(names, heros):
#     myDict[name] = hero
# print(myDict)

# myDict = {name: hero for name, hero in zip(names,heros)}
# print(myDict)
#
# #If name not equal to Peter
# myDict = {name: hero for name, hero in zip(names,heros) if name!='Peter'}
# print(myDict)


#Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,9,7,8]
# mySet = set()
# for n in nums:
#     mySet.add(n)
# print(mySet)

#using comprehension set
# mySet = {n for n in nums}
# print(mySet)


#Generatr Expressions
# I want to yeild 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# myGen = gen_func(nums)

myGen = (n*n for n in nums)
for i in myGen:
    print(i)
