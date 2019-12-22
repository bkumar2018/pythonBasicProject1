
i = 0
num = []

while i < 6:
	print(f"At the top i is {i}")
	num.append(i)

	i = i+1
	print (f"Numbers now: {num}")

print("The numbers: ")
for nums in num:
	print(f"{nums}")

