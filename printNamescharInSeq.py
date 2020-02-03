
name = "Birender"

list1 = list(name)

for index in range(0, len(list1)+1):
    for x in range(0,index):
        print(list1[x],  end = '', flush=True)   #for python2 --> print(list1[x]),
    print("\n")
