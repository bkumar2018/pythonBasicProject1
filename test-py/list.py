
list1 = [1,3,6,0,4,5,0,1,3,2]
list1.append(10)
print(list1)

def find_duplicates(s):
    nonduplicate = set()
    duplicates = []

    for item in s:
        if item not in nonduplicate:
            nonduplicate.add(item)
        else:
            duplicates.append(item)
    return duplicates

print(find_duplicates(list1))
stringlist = ['apple', 'banana', 'orange', 'apple']
print(find_duplicates(stringlist))
print(find_duplicates('Hello'))

dict1 = {'id':1233, 'name':'Birender'}

print(dict1['id'])
print(dict1['name'])




