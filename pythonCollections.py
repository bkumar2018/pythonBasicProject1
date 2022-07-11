from collections import Counter

str = "aaabbbbccddde"
mycounter = Counter(str)
print(mycounter)
print(mycounter.keys())
print(mycounter.values())
print(mycounter.items())
print(mycounter.most_common(1))
