
import json

#json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

jsonStr1 = ['foo', {'bar': ('baz', None, 1.0, 2)}]

for list1 in jsonStr1:
    if type(list1) == dict :
        print ("is dict")
        for x in range(0,len(list1["bar"])):
            print(list1["bar"][x])
    else:
        print(list1)

print("***************************************")
jsonStr2 = [{'fruits':('apple','orange')},'foo', {'bar': ('baz', None, 1.0, 2)},[10,20,30,40]]
print(jsonStr2)

for list2 in jsonStr2:
    if type(list2)==dict:
        if "fruits" in list2.keys():
            for x in range(0,len(list2["fruits"])):
                print(list2["fruits"][x])        
        elif "bar" in list2.keys():
            for x in range(0,len(list2["bar"])):
                print(list2["bar"][x])
        else:
            pass
    elif type(list2)==list:
        for x in list2:
            print(x)
    else:
        print(list2)



# list2 = [1,3,5,7,9]
# for x in list2:
#     print(x)
