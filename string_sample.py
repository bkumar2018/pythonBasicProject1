
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


