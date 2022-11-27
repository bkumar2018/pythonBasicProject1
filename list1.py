
# new list of items

list=[12,34,56,78,90]

#Print all the data inside list
for r in list:
	print(r)

#Add new element to list
list.append(100)

#Add a whole list inside the list
list.append([1,21,2,3])
print(list)


#Access individual values from the list
squares=[1,4,8,15,25]
print(squares)

#Get 0th element from the list
print(squares[0])

#Get 3rd element from the list
print(squares[3])

#Get last element from the list
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

#list of list items
x=[a,b]
<<<<<<< HEAD
print(x)

#Get 0th of list and then get 1st element from that 0th list.
print(x[0][1])  #b

#Get 1st of list and then get 2nd element from that 1st list.
print(x[1][2])  #3
=======
print(x[0][1])


list2= [10,45,67,89,09,34,12]
for x in list2:
	print(x)

>>>>>>> 8738d173d5b263e0b9959f4f2f965a35c7d879cc
