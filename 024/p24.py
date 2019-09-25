import itertools

a = [0,1,2,3,4,5,6,7,8,9]
perm_list = list(itertools.permutations(a))
print("".join(str(n) for n in perm_list[999999]))

