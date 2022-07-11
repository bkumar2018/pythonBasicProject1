#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# print(list(prod))
# prod = product(a,b, repeat=2)
# print(list(prod))


# from itertools import permutations
# a= [1,2,3]
# perm = permutations(a)
# print(list(perm))
# perm = permutations(a, 2)
# print(list(perm))


# from itertools import combinations, combinations_with_replacement
# a = [1,2,3,4]
# comb = combinations(a, 2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# from itertools import accumulate
# a = [1,2,3,4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

from itertools import groupby
a= [1,2,3,4]

def smaller_than_3(x):
    return x <3

# grp_obj = groupby(a, key=smaller_than_3)
# for key, value in grp_obj:
#     print(key, list(value))


#using lambad function: one liner functions
grp_obj = groupby(a, key=lambda x:x<3)
for key, value in grp_obj:
    print(key, list(value))

