
# new list of items

list=[12,34,56,78,90]

for r in list:
	print(r)
list.append(100)
list.append([1,21,2,3])
print(list)


squares=[1,4,8,15,25]
print(squares)
print(squares[0])
print(squares[3])
print(squares[-1])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(letters[2:5])
#replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
#now remove them
letters[2:5] = []
print(letters)
#get length of list
print(len(letters))

a=['a', 'b', 'c']
b=[1, 2, 3]
x=[a,b]
print(x[0][1])
