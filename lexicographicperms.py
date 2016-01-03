from itertools import permutations 

a =  [0,1,2,3,4,5,6,7,8,9]

perms = [perm for perm in permutations(a)]

perms = sorted(perms)
print perms[999998:1000001], len(perms)
