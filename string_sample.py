
#Strings  are ordered, imutable, text representations

# str = "Hello World"
# ch = str[-1]
# #str[0] = 'c'  --> Error can not be changed as immutable
# print(ch)

# my_string = "Hello String"
# #sub = my_string[::-1]
# sub = my_string[0:3]
# print(sub)


# greeting = "Hello John"
# for x in greeting:
#     print(x)

# greeting = "Hello John"
# if 'e' in greeting:
#     print('yes')
# else:
#     print('no')

# greeting = "Hello John"
# if 'ell' in greeting:
#     print('yes')
# else:
#     print('no')

# mystring = "       Hello John          "
# mystring = mystring.strip()
# print(mystring)


mystring = "       Hello John          "
mystring = mystring.strip()
print(mystring)
print(mystring.startswith("Hello"))
print(mystring.endswith("Hello"))
print(mystring.find('o'))
print(mystring.find('llo'))
print("count letter 'o' appears: ", mystring.count('o'))
print(mystring.replace('World', 'Universe'))

#Convert string to list
#mystring = "Welcome to the world of python"
#mylist  = mystring.split()
#print(mylist)

mystring = "Welcome, to, the, world, of, python"
mylist  = mystring.split(',')
print(mylist)

mystring = "Welcome, to, the, world, of, python"
mylist  = mystring.split(',')
print(mylist)
#convert back list to string
new_string = ' '.join(mylist)
print(new_string)

from timeit import default_timer as timer

mylist = ['a'] * 6
print(mylist)

#bad
start = timer()
new_string = ''
for i in mylist:
    new_string == i
stop = timer()
print(new_string)
print(stop-start)

#good
start = timer()
my_string = ''.join(mylist)
stop = timer()
print(my_string)
print(stop-start)


#String formatter
myname = "Birender"
age = 24
print('{}, {}'.format(myname, age))
print(f'{myname}, {age}')



