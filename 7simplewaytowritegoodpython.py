
#Scenario1
# list of city, and we walk trough list, we want position and items from list.

cities = ['Marseille', 'Amsterdam', 'New york', 'London']

#the bad way
# i = 0
# for city in cities:
#     print(i,city)
#     i = i+1

#good way
#enumerate return list of index with list item
for i, city in enumerate(cities):
    print(i, city)

#Scenario2
# we have 2 or more lists and when we walk through these list as same time. use zip.
x_list = [1,2,3]
y_list = [2,4,6]

#bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x,y)

#good way
for x, y in zip(x_list,y_list):
    print(x,y)

#Secnario 3
#swap variable

#Bad way
x = 10
y = -10

# print("Before ", x, y)
# tmp = x
# x = y
# y = tmp
# print("After ",x, y)

x , y = 10, -10
print("Before swap", x, y)
x, y = y, x
print("Good way swap", x, y)

#Secnario 4
#When we need to check a key or item in dictornay is present ot not, then use .get method
ages = {
    'Mary' : 31,
    'John' : 28,
    'Dick' : 51
}

#Bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'unknown'

print("Dick is %s year old" %age)

#Good way
age = ages.get('Dick', 'Unknown')
print("Dick is %s year old" %age)


#Secnario 5
# To check a item is present in a list

needle = 'd'
haystack = ['a', 'b', 'c',]

#Bad
found = False
for letter in haystack:
    if needle == letter:
        print('Found')
        found = True
        break
if not found:
    print('Not found')

#Good
for letter in haystack:
    if needle == letter:
        print("Found")
        break
else:  #If no break occured, without marker variable
    print("Not found")


#Secnario 6

#Bad
f = open('test.txt')
text = f.read()

for line in text.split('\n'):
    print(line)
f.close()

#Good
f = open('test.txt')
for line in f:
    print(line)
f.close()

# with open, we need to bother clean up, or f.close()
with open("test.txt") as f:
    for line in f:
        print(line)

#Secanrion 7

#print('converting')
#print(int('x'))
#print('Done!')


print('converting')
try:
    print(int('1'))
except:
    print('Conversation failed!')
else: #If no-except
    print('Conversation pass!')
finally: #Allways
    print('Done!')


print('converting')
try:
    print(int('x'))
finally: #Allways  we can have clean up code here
    print('Done!')

