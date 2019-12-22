

x = 'frog'
print(x[1])
print(x[:3])
print(x[1:])
print(x[-1])
print(x[-3:])
print(x[:-2])
print(x[::-1])
# print("Till lenght of string data type")
# for i in range(0,len(x)):
#     print(x[i])

str1 = "horse" + "shoe"
print(str1)
print('bug'*3)

lst = ['pune','mumbai','delhi']
print(lst)
print(lst[2])
print([1,2]*3)

#checking member of items or string
x='horse'
print('o' in x) #True
print('f' in x) #False
print('pune' in lst) #True
print('mumbai' not in lst) #False - it is in list

#iterating
for i in lst:
    print(i*2)

#indexing using enumerate
num = [8,3,9,4]
for index, item in enumerate(num):
    print(index, item)

#len
print(len(x))
print(len(lst))
print(len(num))

#min
print(min(x))
print(min(lst))
print(min(num))

#max
print(max(x))
print(max(lst))
print(max(num))

#sum
print(sum(num))

#sorted
print(sorted(x))
print(sorted(lst))
print(sorted(num))

y  = sorted(lst)
print(y)

#count
ct = 'apple'
print(ct.count('p'))

lst.append('pune')
lst.append('pune')
print(lst)
print(lst.count('pune'))

#check index
print(x.index('r'))
print(lst.index('mumbai'))

#unpacking
unpack = ['sun','mon','tue']
print(unpack)
a,b,c = unpack
print(a)
print(b)
print(c)

#list comperehansion
lst1 = [m for m in range(8)]
print(lst1)

#set
set1 = {3,4,5,4,3,2,6}
noduplist = list(set1)
print(noduplist)

#set comerehansion
set2 = {3*x for x in range(10) if x>5}
print(set2)
set2.add(6)
print(set2)

#dictionary

dict1 = dict(sunday=1, monday=2, tuesday=3)
print(dict1)
print(dict1.keys())
print(dict1.values())

dict1['wednesday'] = 4
print(dict1)
print(len(dict1))

for key in dict1:
    print(key,dict1[key])
print('--'*10)
for k , v in dict1.items():
    print(k,v)









